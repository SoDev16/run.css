#!/usr/bin/env python3
"""Page produit et page d'accueil, avec les sections natives de Shrine.

Chaque section est copiée depuis une configuration réelle du thème puis
retraduite : aucun réglage n'est inventé, ce qui évite les refus silencieux
de themeFilesUpsert.

Palette : voir PALETTE.md. Le vert #002418 est porté par le schéma accent-2.
Aucune statistique ni témoignage inventé : la directive Omnibus les interdit.
"""
import json

VERDE_VIVO, LINEA, GRIGIO = "#1E9E5A", "#2A2A2A", "#A8A8A8"
BIANCO, NERO, ROSSO = "#FFFFFF", "#121212", "#BF092F"

# pictogrammes confirmés présents dans la configuration d'origine de Shrine
ICO = dict(spedizione="local_shipping", regalo="redeem", spunta="check_circle",
           casella="check_box", negozio="storefront", etichetta="sell")

def couleurs(fond=NERO, texte=BIANCO):
    return {"custom_colors_background": fond, "custom_gradient_background": "",
            "custom_colors_text": texte,
            "custom_colors_solid_button_background": ROSSO,
            "custom_colors_solid_button_text": BIANCO,
            "custom_colors_outline_button": BIANCO}

# =========================================================================
# Barre de garanties
# =========================================================================
def barra_garanzie(cle):
    voci = [
        (ICO["spedizione"], "Spedizione gratuita", "Su ogni ordine, senza minimo."),
        (ICO["regalo"], "120 giorni di prova", "La rendi se non ti convince."),
        (ICO["spunta"], "Garanzia a vita", "Nessun rivestimento che si stacca."),
        (ICO["casella"], "100% priva di tossine", "Senza PFAS, PTFE e PFOA."),
    ]
    blocs = {}
    for i, (ic, titre, txt) in enumerate(voci, 1):
        blocs[f"{cle}_col{i}"] = {"type": "column", "settings": {
            "icon": ic, "filled_icon": False, "title": titre,
            "text": f"<p>{txt}</p>"}}
    return {"type": "icon-bar", "blocks": blocs, "block_order": list(blocs), "settings": {
        "display_id": False, "visibility": "always-display",
        "title": "", "title_highlight_color": ROSSO, "heading_size": "h1", "text": "",
        "color_scheme": "background-1", "icon_layout": "vertical",
        "icon_size": "medium", "icon_color": "accent-1",
        "cards_color_scheme": "background-1", "type": "slide",
        "autoplay": False, "autoplay_speed": 5,
        "arrows_color_scheme": "inverse", "transparent_arrows": True,
        "dots_color_scheme": "inverse", "desktop_full_page": False,
        "columns_desktop": 4, "slider_desktop": False, "per_move_desktop": 1,
        "desktop_spacing": 40, "desktop_side_padding": 0,
        "desktop_padding_calc": True, "desktop_adaptive_height": False,
        "desktop_dots_position": "under", "desktop_arrows_position": "sides",
        "columns_mobile": "1", "slider_mobile": True,
        "enable_mobile_preview": False, "mobile_adaptive_height": False,
        "mobile_dots_position": "under", "mobile_arrows_position": "under",
        "padding_top": 36, "padding_bottom": 36,
        **couleurs(),
        "custom_cards_colors_background": NERO,
        "custom_cards_gradient_background": "",
        "custom_cards_colors_text": BIANCO}}

# =========================================================================
# Tableau comparatif
# =========================================================================
def tabella_confronto(cle):
    righe = [
        "Senza PFAS, PTFE e PFOA",
        "Antiaderente senza rivestimenti",
        "Resiste agli utensili in metallo",
        "Adatta al forno e alla lavastoviglie",
        "Garanzia a vita",
    ]
    blocs = {}
    for i, r in enumerate(righe, 1):
        blocs[f"{cle}_riga{i}"] = {"type": "row", "settings": {
            "benefit": f"<strong>{r}</strong>",
            "us": True, "others": False, "others_2": False, "others_3": False}}
    return {"type": "comparison-table", "blocks": blocs, "block_order": list(blocs), "settings": {
        "display_id": False, "visibility": "always-display",
        "title": "Titanio e gli altri", "title_highlight_color": ROSSO,
        "heading_size": "h1",
        "text": "<p>Perché il titanio puro cambia il modo di cucinare.</p>",
        "button_label": "", "link": "", "button_style_secondary": False,
        "atc_button_label": "", "atc_product": "", "atc_skip_cart": False,
        "desktop_alignment": "center", "mobile_alignment": "center",
        "color_scheme": "background-1", "layout": "table_second",
        "style": "centered", "corner_radius": 20,
        "number_of_competitors": 1,
        "us_label": "[shop_name]", "us_label_size": 18,
        "logo_width": 90, "mobile_logo_width": 60,
        "others_label": "Altre padelle", "others_label_size": 18,
        "others_logo_width": 90, "others_mobile_logo_width": 60,
        "others_2_label": "Concorrente 2", "others_2_label_size": 18,
        "others_2_logo_width": 90, "others_2_mobile_logo_width": 60,
        "others_3_label": "Concorrente 3", "others_3_label_size": 18,
        "others_3_logo_width": 90, "others_3_mobile_logo_width": 60,
        "checkmark_style": "regular", "checkmark_color": BIANCO,
        "checkmark_bg_color": VERDE_VIVO,
        "x_style": "regular", "x_color": GRIGIO, "x_bg_color": LINEA,
        "opposite_icon_colors": "original",
        "highlighted_color_scheme": "accent-1",
        "highlighted_separator_opacity": 0, "highlighted_overlay_opacity": 0,
        "other_cells_color_scheme": "background-1",
        "regular_separator_opacity": 10, "regular_overlay_opacity": 0,
        "minimalistic_border_opacity": 16,
        "padding_top": 36, "padding_bottom": 36,
        **couleurs(),
        "custom_colors_highlighted_background": ROSSO,
        "custom_colors_highlighted_text": BIANCO,
        "custom_colors_others_background": NERO,
        "custom_colors_others_text": GRIGIO}}

# =========================================================================
# Trois arguments longs
# =========================================================================
def argomenti(cle):
    voci = [
        (ICO["spunta"], "Titanio puro, il metallo più sicuro a contatto con il corpo",
         "Usato da decenni negli impianti medici per la sua biocompatibilità. "
         "Non è tossico e non reagisce con gli alimenti."),
        (ICO["casella"], "Antiaderente senza sostanze chimiche",
         "La superficie è microincisa, non rivestita. Nessuna pellicola che si "
         "stacca col tempo, perché non c'è pellicola."),
        (ICO["etichetta"], "Nessun trasferimento di metalli nel cibo",
         "Resiste agli utensili in metallo, al forno e alla lavastoviglie."),
    ]
    blocs = {}
    for i, (ic, titre, txt) in enumerate(voci, 1):
        blocs[f"{cle}_ico{i}"] = {"type": "icon", "settings": {
            "icon": ic, "filled_icon": False, "title": titre,
            "text": f"<p>{txt}</p>"}}
    blocs[f"{cle}_titolo"] = {"type": "heading", "settings": {
        "title": "Un nuovo standard di sicurezza, prestazioni e durata.",
        "title_highlight_color": ROSSO, "heading_size": "h1"}}
    blocs[f"{cle}_testo"] = {"type": "text", "settings": {
        "text": "<p>Il titanio non ha bisogno di rivestimenti per non attaccare. "
                "È questa la differenza.</p>", "text_style": "body"}}
    ordre = [f"{cle}_ico1", f"{cle}_ico2", f"{cle}_ico3",
             f"{cle}_titolo", f"{cle}_testo"]
    return {"type": "icons-with-content", "blocks": blocs, "block_order": ordre, "settings": {
        "display_id": False, "visibility": "always-display",
        "color_scheme": "background-1", "icon_size": "m",
        "icon_position": "next-to-title", "icon_color": "accent-1",
        "icon_heading_size": "h3", "icon_text_alignment": "left",
        "icons_desktop_layout": "1-column", "icons_mobile_layout": "1-column",
        "desktop_content_alignment": "left",
        "layout": "image_first", "mobile_layout": "text_first",
        "hide_content_on_mobile": False,
        "padding_top": 36, "padding_bottom": 36,
        **couleurs()}}

# =========================================================================
# Section de marque, en vert — schéma accent-2
# =========================================================================
def sezione_verde(cle):
    voci = [
        "Cucinare senza chiederti cosa finisce nel piatto.",
        "Una padella che non si rovina e non si sostituisce.",
        "Meno prodotti chimici in casa, semplicemente.",
    ]
    blocs = {f"{cle}_titolo": {"type": "heading", "settings": {
        "column": "col_1", "visibility": "always-display",
        "heading": "Il tuo corpo merita di meglio.",
        "title_highlight_color": "#BDA589", "heading_size": "h1",
        "alignment": "center", "mobile_alignment": "mobile-center",
        "margin_top": 20, "margin_bottom": 20}}}
    for i, t in enumerate(voci, 1):
        blocs[f"{cle}_voce{i}"] = {"type": "icon_with_text", "settings": {
            "column": f"col_{i+1}", "visibility": "always-display",
            "icon": ICO["spunta"], "filled_icon": False, "icon_size": "m",
            "icon_position": "next-to-title", "icon_color": "accent-1",
            "icon_heading_size": "h3", "icon_text_alignment": "left",
            "title": "", "text": f"<p>{t}</p>",
            "margin_top": 20, "margin_bottom": 20}}
    return {"type": "custom-columns", "blocks": blocs, "block_order": list(blocs), "settings": {
        "display_id": False, "visibility": "always-display",
        "color_scheme": "accent-2",     # le vert #002418 de la référence
        "columns_count": 4,
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
        "padding_top": 36, "padding_bottom": 36,
        **couleurs("#002418", "#D4C7B4")}}

# =========================================================================
# Page produit : le bloc d'achat déjà traduit, puis les sections
# =========================================================================
prod = json.load(open("templates/product.json", encoding="utf-8"))
prod["sections"]["garanzie"] = barra_garanzie("garanzie")
prod["sections"]["confronto"] = tabella_confronto("confronto")
prod["sections"]["argomenti"] = argomenti("argomenti")
prod["sections"]["merita"] = sezione_verde("merita")
prod["order"] = ["main", "garanzie", "argomenti", "confronto", "merita"]
open("templates/product.json", "w", encoding="utf-8").write(
    json.dumps(prod, separators=(",", ":"), ensure_ascii=False))

# =========================================================================
# Page d'accueil
# =========================================================================
eroe = {"type": "slideshow", "blocks": {
    "slide_1": {"type": "slide", "settings": {
        "image_overlay_opacity": 0,
        "heading": "Passa a una cucina senza sostanze tossiche.",
        "title_highlight_color": ROSSO, "heading_size": "h1",
        "subheading": "Titanio puro certificato. Niente PFAS, nessun rivestimento.",
        "button_label": "Scopri la padella",
        "link": "/products/padella-titanio-vero",
        "button_style_secondary": False,
        "atc_button_label": "", "atc_product": "", "atc_skip_cart": False,
        "box_align": "middle-center", "show_text_box": False,
        "text_alignment": "center", "color_scheme": "background-1",
        "transparent_container_color": "white",
        "text_alignment_mobile": "center", **couleurs()}}},
    "block_order": ["slide_1"], "settings": {
        "visibility": "always-display", "layout": "full_bleed",
        "slide_height": "medium", "slider_visual": "dots",
        "desktop_pagination_position": "over", "auto_rotate": False,
        "change_slides_speed": 5, "show_text_below": False,
        "mobile_pagination_position": "under",
        "accessibility_info": "Padelle in titanio puro Titanio Vero"}}

accueil = {"sections": {
    "eroe": eroe,
    "garanzie": barra_garanzie("h_garanzie"),
    "argomenti": argomenti("h_argomenti"),
    "confronto": tabella_confronto("h_confronto"),
    "merita": sezione_verde("h_merita"),
}, "order": ["eroe", "garanzie", "argomenti", "confronto", "merita"]}
open("templates/index.json", "w", encoding="utf-8").write(
    json.dumps(accueil, separators=(",", ":"), ensure_ascii=False))

for f in ("templates/product.json", "templates/index.json"):
    d = json.load(open(f, encoding="utf-8"))
    print(f"{f} : {len(open(f,encoding='utf-8').read()):6} octets · sections :",
          " · ".join(d["sections"][k]["type"] for k in d["order"]))
