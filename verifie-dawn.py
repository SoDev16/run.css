#!/usr/bin/env python3
"""Contrôle des limites Shopify sur les sections du thème Dawn.

Écrit après avoir découvert que « tv-lettera » ne s'installait pas : son nom
faisait 27 caractères pour une limite de 25. La section manquait, la page
d'accueil la référençait, et Shopify rejetait donc la page d'accueil —
d'où l'erreur 404 sur tout le site.
"""
import json, re, glob, os, sys

LIMITE_NOM = 25
LIMITE_SECTIONS = 25
LIMITE_BLOCS = 50

fautes = []
schemas = {}

for p in sorted(glob.glob('theme/sections/*.liquid')):
    nom = os.path.basename(p)[:-7]
    src = open(p, encoding='utf-8').read()
    m = re.search(r'\{%\s*schema\s*%\}(.*?)\{%\s*endschema\s*%\}', src, re.S)
    if not m:
        continue
    try:
        sch = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        fautes.append(f"{nom} : schéma JSON invalide — {e}")
        continue
    schemas[nom] = sch
    # les noms en « t:… » sont des clés de traduction résolues par Shopify :
    # la limite porte sur le texte affiché, pas sur la clé
    if not sch.get("name", "").startswith("t:") and len(sch.get("name", "")) > LIMITE_NOM:
        fautes.append(f"{nom} : nom de {len(sch['name'])} caractères « {sch['name']} » "
                      f"(limite {LIMITE_NOM}) — la section ne s'installera pas")
    for pr in sch.get("presets", []) or []:
        if not pr.get("name", "").startswith("t:") and len(pr.get("name", "")) > LIMITE_NOM:
            fautes.append(f"{nom} : preset de {len(pr['name'])} caractères « {pr['name']} » "
                          f"(limite {LIMITE_NOM})")

for p in sorted(glob.glob('theme/templates/*.json')) + sorted(glob.glob('theme/sections/*.json')):
    nom = os.path.basename(p)
    try:
        d = json.load(open(p, encoding='utf-8'))
    except json.JSONDecodeError as e:
        fautes.append(f"{nom} : JSON invalide — {e}")
        continue
    secs = d.get("sections", {})
    if len(secs) > LIMITE_SECTIONS:
        fautes.append(f"{nom} : {len(secs)} sections (limite {LIMITE_SECTIONS})")
    for cle in d.get("order", []):
        if cle not in secs:
            fautes.append(f"{nom} : « order » cite « {cle} », absent de « sections »")
    for cle, s in secs.items():
        t = s.get("type")
        if t not in schemas and not os.path.exists(f"theme/sections/{t}.liquid"):
            fautes.append(f"{nom} : section « {cle} » de type « {t} » introuvable")
            continue
        nb = len(s.get("blocks", {}) or {})
        if nb > LIMITE_BLOCS:
            fautes.append(f"{nom} : « {cle} » a {nb} blocs (limite {LIMITE_BLOCS})")
        mx = schemas.get(t, {}).get("max_blocks")
        if mx is not None and nb > mx:
            fautes.append(f"{nom} : « {cle} » a {nb} blocs, son schéma en permet {mx}")

if fautes:
    print(f"✗ {len(fautes)} problème(s) :")
    for f in fautes:
        print("   -", f)
    sys.exit(1)
print(f"✓ {len(schemas)} sections et tous les gabarits respectent les limites Shopify")
