#!/usr/bin/env python3
"""Vérifie un fichier de section/template Horizon contre les schémas du thème.

Contrôle trois choses que je ne peux pas voir à l'œil, faute d'accès à la
boutique : que chaque section existe, que chaque bloc est autorisé à l'endroit
où il est posé, et que chaque réglage porte un identifiant qui existe vraiment.
"""
import json, re, sys, glob, os

SRC = "/home/user/shopify/horizon"

def schema(chemin):
    s = open(chemin, encoding="utf-8").read()
    m = re.search(r"\{%\s*schema\s*%\}(.*?)\{%\s*endschema\s*%\}", s, re.S)
    return json.loads(m.group(1)) if m else {}

def ids(sch):
    out = set()
    for i in sch.get("settings", []) or []:
        if i.get("id"):
            out.add(i["id"])
    return out

def options(sch):
    """Valeurs autorisées pour chaque réglage de type « select » ou « radio »."""
    out = {}
    for i in sch.get("settings", []) or []:
        if i.get("type") in ("select", "radio") and i.get("id"):
            out[i["id"]] = {o.get("value") for o in i.get("options", [])}
    return out

SECTIONS = {os.path.basename(p)[:-7]: schema(p) for p in glob.glob(f"{SRC}/sections/*.liquid")}
BLOCS    = {os.path.basename(p)[:-7]: schema(p) for p in glob.glob(f"{SRC}/blocks/*.liquid")}

def statiques(nom):
    """Blocs posés en dur dans le code d'une section (content_for 'block'),
    donc absents de son schéma mais parfaitement légitimes."""
    p = f"{SRC}/sections/{nom}.liquid"
    if not os.path.exists(p):
        return set()
    src = open(p, encoding="utf-8").read()
    return set(re.findall(r"content_for\s+'block'\s*,\s*type:\s*'([^']+)'", src))

# réglages de mise en page injectés par Horizon dans tout bloc « présentable »
COMMUNS = {"padding-block-start","padding-block-end","padding-inline-start",
           "padding-inline-end","width","custom_width","width_mobile",
           "custom_width_mobile","height","custom_height","horizontal_alignment",
           "vertical_alignment","content_direction","vertical_on_mobile",
           "align_baseline","horizontal_alignment_flex_direction_column",
           "vertical_alignment_flex_direction_column","gap","background_media",
           "video_position","background_image_position","border","border_width",
           "border_opacity","border_radius","toggle_overlay","overlay_color",
           "overlay_style","gradient_direction","open_in_new_tab","inherit_color_scheme"}

fautes = []

def autorises(sch, section=None):
    """Types de blocs acceptés ; None = tout bloc de thème."""
    b = sch.get("blocks")
    fixes = statiques(section) if section else set()
    if b is None:
        return fixes or set()
    types = {x.get("type") for x in b}
    if "@theme" in types:
        return None
    return types | fixes

def controle_blocs(blocs, permis, ou):
    for cle, bloc in (blocs or {}).items():
        t = bloc.get("type", "")
        if t.startswith("shopify://") or t == "@app":
            continue
        if permis is not None and t not in permis:
            fautes.append(f"{ou} → bloc « {t} » ({cle}) non autorisé ici ; permis : {sorted(permis)}")
            continue
        sch = BLOCS.get(t)
        if sch is None:
            fautes.append(f"{ou} → bloc « {t} » ({cle}) n'existe pas dans Horizon")
            continue
        connus = ids(sch) | COMMUNS
        choix = options(sch)
        for r, v in bloc.get("settings", {}).items():
            if r not in connus:
                fautes.append(f"{ou} → bloc « {t} » ({cle}) : réglage inconnu « {r} »")
            elif r in choix and choix[r] and v not in choix[r]:
                fautes.append(f"{ou} → bloc « {t} » ({cle}) : « {r} » = « {v} » ; "
                              f"valeurs permises : {sorted(choix[r])}")
        controle_blocs(bloc.get("blocks"), autorises(sch), f"{ou}/{t}")

for chemin in sys.argv[1:]:
    s = open(chemin, encoding="utf-8").read()
    d = json.loads(s[s.index("{"):])
    nom = os.path.basename(chemin)
    for cle, sec in d.get("sections", {}).items():
        t = sec.get("type")
        sch = SECTIONS.get(t)
        if sch is None:
            fautes.append(f"{nom} → section « {t} » ({cle}) n'existe pas dans Horizon")
            continue
        connus = ids(sch) | COMMUNS
        choix = options(sch)
        for r, v in sec.get("settings", {}).items():
            if r not in connus:
                fautes.append(f"{nom} → section « {t} » ({cle}) : réglage inconnu « {r} »")
            elif r in choix and choix[r] and v not in choix[r]:
                fautes.append(f"{nom} → section « {t} » ({cle}) : « {r} » = « {v} » ; "
                              f"valeurs permises : {sorted(choix[r])}")
        controle_blocs(sec.get("blocks"), autorises(sch, t), f"{nom}/{t}")
    for cle in d.get("order", []):
        if cle not in d.get("sections", {}):
            fautes.append(f"{nom} → « order » cite une section absente : {cle}")

if fautes:
    print(f"✗ {len(fautes)} problème(s) :")
    for f in fautes:
        print("   -", f)
    sys.exit(1)
print("✓ tout est valide")
