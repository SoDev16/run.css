#!/usr/bin/env python3
"""Toutes les sections restantes, avec les briques natives de Shrine.

Couleurs mesurées sur le site de référence (voir PALETTE.md). Chaque section
porte les siennes par le schéma « custom ».
"""
import json

VERDE, ORO, BEIGE, BEIGE_CHIARO = "#04221A", "#A3825F", "#BDA589", "#D4C7B4"
NERO, NERO_2, BIANCO, GRIGIO, ROSSO = "#121212", "#1C1C1C", "#FFFFFF", "#A8A8A8", "#BF092F"
ICO = dict(spunta="check_circle", casella="check_box", spedizione="local_shipping",
           regalo="redeem", etichetta="sell", negozio="storefront")

def col(fond, texte):
    return {"custom_colors_background": fond, "custom_gradient_background": "",
            "custom_colors_text": texte,
            "custom_colors_solid_button_background": ROSSO,
            "custom_colors_solid_button_text": BIANCO,
            "custom_colors_outline_button": ORO}

# ---------------------------------------------------------------- bandeau
def striscia(cle, messaggi, fond=NERO, texte=ORO):
    b = {f"{cle}_{i}": {"type": "text", "settings": {"title": m}}
         for i, m in enumerate(messaggi, 1)}
    return {"type": "horizontal-ticker", "blocks": b, "block_order": list(b), "settings": {
        "visibility": "always-display", "speed": 3, "direction": "normal",
        "stop_on_hover": False, "mobile_spacing": 60, "desktop_spacing": 100,
        "color_scheme": "custom", "mobile_text_size": 16, "desktop_text_size": 18,
        "italic_text": False, "uppercase_text": True, "bold_text": False,
        "mobile_image_height": 26, "desktop_image_height": 40,
        "mobile_reviews_width": 300, "desktop_reviews_width": 400,
        "hidden_products": "", "enable_specific_display": False, "displayed_products": "",
        "mobile_padding_top": 12, "mobile_padding_bottom": 12,
        "desktop_padding_top": 16, "desktop_padding_bottom": 16,
        "custom_colors_background": fond, "custom_gradient_background": "",
        "custom_colors_text": texte}}

# ------------------------------------------------ colonnes libres (cartes)
def colonne(cle, titolo, sotto, voci, fond=NERO, texte=BIANCO, colonnes=3,
            titre_or=ORO, avec_image=False):
    b = {f"{cle}_h": {"type": "heading", "settings": {
            "column": "col_1", "visibility": "always-display", "heading": titolo,
            "title_highlight_color": titre_or, "heading_size": "h1",
            "alignment": "center", "mobile_alignment": "mobile-center",
            "margin_top": 20, "margin_bottom": 20}}}
    if sotto:
        b[f"{cle}_p"] = {"type": "richtext", "settings": {
            "column": "col_1", "visibility": "always-display",
            "text": f"<p>{sotto}</p>", "text_style": "body",
            "alignment": "center", "mobile_alignment": "mobile-center",
            "margin_top": 20, "margin_bottom": 20}}
    for i, (t, txt) in enumerate(voci, 1):
        c = f"col_{i+1}"
        if avec_image:
            b[f"{cle}_img{i}"] = {"type": "image", "settings": {
                "column": c, "visibility": "always-display", "width": 100,
                "alignment": "center", "mobile_alignment": "center",
                "border_radius": 0, "margin_top": 20, "margin_bottom": 20}}
        b[f"{cle}_v{i}"] = {"type": "icon_with_text", "settings": {
            "column": c, "visibility": "always-display",
            "icon": ICO["spunta"], "filled_icon": False, "icon_size": "m",
            "icon_position": "next-to-title", "icon_color": "accent-1",
            "icon_heading_size": "h3", "icon_text_alignment": "left",
            "title": t, "text": f"<p>{txt}</p>",
            "margin_top": 20, "margin_bottom": 20}}
    return {"type": "custom-columns", "blocks": b, "block_order": list(b), "settings": {
        "display_id": False, "visibility": "always-display",
        "color_scheme": "custom", "columns_count": colonnes + 1,
        "column_gap_desktop": 40, "row_gap_desktop": 40,
        "desktop_vertical_alignment": "center",
        "column_gap_mobile": 20, "row_gap_mobile": 30,
        "mobile_vertical_alignment": "flex-start",
        "col_1_desktop_width": 12, "col_1_mobile_width": 4, "col_1_visibility": "always-display",
        "col_2_desktop_width": 4, "col_2_mobile_width": 4, "col_2_visibility": "always-display",
        "col_3_desktop_width": 4, "col_3_mobile_width": 4, "col_3_visibility": "always-display",
        "col_4_desktop_width": 4, "col_4_mobile_width": 4, "col_4_visibility": "always-display",
        "col_5_desktop_width": 3, "col_5_mobile_width": 4, "col_5_visibility": "always-display",
        "col_6_desktop_width": 3, "col_6_mobile_width": 4, "col_6_visibility": "always-display",
        "padding_top": 36, "padding_bottom": 36, **col(fond, texte)}}

# -------------------------------------------------- vue éclatée, en vert
def strati(cle):
    voci = [
        ("Titanio puro in superficie", "Antiaderente, senza rivestimenti."),
        ("Primo strato in alluminio", "Assorbe il calore rapidamente."),
        ("Secondo strato in alluminio", "Stabilizza il calore interno."),
        ("Terzo strato in alluminio", "Distribuisce il calore fino ai bordi."),
        ("Acciaio adatto a induzione", "Resistenza e conducibilità magnetica."),
    ]
    b = {}
    for i, (t, txt) in enumerate(voci, 1):
        b[f"{cle}_s{i}"] = {"type": "icon", "settings": {
            "icon": ICO["spunta"], "filled_icon": False,
            "title": t, "text": f"<p>{txt}</p>"}}
    b[f"{cle}_h"] = {"type": "heading", "settings": {
        "title": "Costruita da dentro in fuori.",
        "title_highlight_color": BEIGE, "heading_size": "h1"}}
    b[f"{cle}_t"] = {"type": "text", "settings": {
        "text": "<p>Cinque strati, una sola superficie a contatto con il cibo.</p>",
        "text_style": "body"}}
    ordre = [f"{cle}_h", f"{cle}_t"] + [f"{cle}_s{i}" for i in range(1, 6)]
    return {"type": "icons-with-content", "blocks": b, "block_order": ordre, "settings": {
        "display_id": False, "visibility": "always-display",
        "color_scheme": "custom", "icon_size": "m",
        "icon_position": "next-to-title", "icon_color": "text",
        "icon_heading_size": "h3", "icon_text_alignment": "left",
        "icons_desktop_layout": "1-column", "icons_mobile_layout": "1-column",
        "desktop_content_alignment": "left",
        "layout": "image_first", "mobile_layout": "text_first",
        "hide_content_on_mobile": False,
        "padding_top": 36, "padding_bottom": 36, **col(VERDE, ORO)}}

# ----------------------------------------------- mosaïque photos clients
def mosaico(cle, titolo):
    b = {f"{cle}_i{i}": {"type": "image_slide", "settings": {
            "link": "", "description": "", "desc_alignment": "center",
            "desc_color_scheme": "background-2"}} for i in range(1, 7)}
    return {"type": "image-slider", "blocks": b, "block_order": list(b), "settings": {
        "display_id": False, "visibility": "always-display",
        "title": titolo, "title_highlight_color": ORO, "heading_size": "h1",
        "color_scheme": "custom", "type": "slide", "drag": "enabled",
        "autoplay": False, "autoplay_speed": 5, "center_mode": False,
        "arrows_color_scheme": "inverse", "transparent_arrows": False,
        "dots_color_scheme": "inverse", "desktop_page_width": "normal",
        "desktop_border_radius": 0, "slides_desktop": 3, "per_move_desktop": 1,
        "desktop_spacing": 28, "desktop_side_padding": 0,
        "desktop_padding_calc": True, "desktop_adaptive_height": False,
        "desktop_dots_position": "under", "desktop_arrows_position": "sides",
        "mobile_full_page": False, "mobile_border_radius": 0,
        "slides_mobile": 2, "per_move_mobile": 1, "mobile_spacing": 12,
        "mobile_side_padding": 0, "mobile_padding_calc": True,
        "mobile_adaptive_height": False, "mobile_dots_position": "under",
        "mobile_arrows_position": "sides",
        "padding_top": 36, "padding_bottom": 36,
        "custom_colors_background": NERO, "custom_gradient_background": "",
        "custom_colors_text": BIANCO}}

# --------------------------------------------- témoignages, prêts mais éteints
def testimonianze(cle):
    b = {f"{cle}_c{i}": {"type": "column", "settings": {
            "star_rating": 5, "title": "", "text": "<p></p>", "author": ""}}
         for i in range(1, 4)}
    return {"type": "testimonials", "disabled": True,
            "blocks": b, "block_order": list(b), "settings": {
        "display_id": False, "visibility": "always-display",
        "title": "Cosa dicono i clienti", "title_highlight_color": ORO,
        "heading_size": "h1", "text": "", "color_scheme": "custom",
        "image_width": "full", "image_ratio": "square",
        "column_alignment": "center", "show_stars": True,
        "inactive_stars_style": "solid", "star_color": ORO,
        "bg_star_color": "#2A2A2A", "show_quotes": True,
        "quotes_color_scheme": "accent-2", "cards_color_scheme": "custom",
        "type": "slide", "autoplay": False, "autoplay_speed": 5,
        "arrows_color_scheme": "inverse", "transparent_arrows": True,
        "dots_color_scheme": "inverse", "desktop_full_page": False,
        "columns_desktop": 3, "slider_desktop": False, "per_move_desktop": 1,
        "desktop_spacing": 40, "desktop_side_padding": 0,
        "desktop_padding_calc": True, "desktop_adaptive_height": False,
        "desktop_dots_position": "under", "desktop_arrows_position": "sides",
        "slider_mobile": True, "enable_mobile_preview": False,
        "mobile_adaptive_height": False, "mobile_dots_position": "under",
        "mobile_arrows_position": "under",
        "padding_top": 36, "padding_bottom": 36,
        "custom_colors_background": NERO, "custom_gradient_background": "",
        "custom_colors_text": BIANCO,
        "custom_cards_colors_background": NERO_2,
        "custom_cards_gradient_background": "",
        "custom_cards_colors_text": BIANCO}}

# =========================================================================
def sezioni_comuni(p):
    return {
        f"{p}striscia": striscia(f"{p}str", [
            "SENZA PFAS, PTFE E PFOA", "SPEDIZIONE GRATUITA",
            "GARANZIA A VITA", "120 GIORNI DI PROVA"]),
        f"{p}ripensare": colonne(f"{p}rip",
            "È ora di ripensare le tue padelle.",
            "Tra rischio di contaminazione e manutenzione difficile, "
            "queste superfici non reggono il confronto con il titanio.", [
                ("Antiaderente / Teflon",
                 "Rilascia PFAS, i cosiddetti «inquinanti eterni». Il "
                 "rivestimento si consuma e finisce nel cibo."),
                ("Acciaio inox",
                 "Richiede molto olio, reagisce con gli alimenti acidi e "
                 "resta difficile da pulire."),
                ("Ceramica",
                 "Perde le sue proprietà antiaderenti dopo pochi mesi di uso."),
            ], avec_image=True),
        f"{p}strati": strati(f"{p}str5"),
        f"{p}mosaico": mosaico(f"{p}mos", "Nelle cucine dei nostri clienti"),
        f"{p}amazon": colonne(f"{p}amz",
            "Né su Amazon, né altrove.",
            "Solo il nostro sito ufficiale garantisce un prodotto "
            "Titanio Vero autentico.", [], colonnes=1,
            fond=NERO, texte=ORO),
        f"{p}testimonianze": testimonianze(f"{p}tes"),
        f"{p}lettera": colonne(f"{p}let",
            "La salute è ciò che abbiamo di più prezioso.",
            "È il motivo per cui esiste Titanio Vero.", [], colonnes=1,
            fond=NERO_2, texte=BEIGE_CHIARO),
    }

for chemin, prefixe in (("templates/product.json", ""), ("templates/index.json", "h_")):
    d = json.load(open(chemin, encoding="utf-8"))
    d["sections"].update(sezioni_comuni(prefixe))
    base = d["order"]
    tete = [k for k in base if d["sections"][k]["type"] in ("main-product", "slideshow")]
    d["order"] = tete + [
        f"{prefixe}striscia",
        [k for k in base if d["sections"][k]["type"] == "icon-bar"][0],
        [k for k in base if d["sections"][k]["type"] == "icons-with-content"][0],
        f"{prefixe}ripensare",
        [k for k in base if d["sections"][k]["type"] == "comparison-table"][0],
        f"{prefixe}strati",
        f"{prefixe}mosaico",
        [k for k in base if d["sections"][k]["type"] == "custom-columns"][0],
        f"{prefixe}amazon",
        f"{prefixe}testimonianze",
        f"{prefixe}lettera",
    ]
    open(chemin, "w", encoding="utf-8").write(json.dumps(d, separators=(",", ":"), ensure_ascii=False))
    print(f"{chemin} : {len(d['order'])} sections ·",
          " · ".join(d["sections"][k]["type"] for k in d["order"]))
