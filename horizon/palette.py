import json, re, sys

entete = """/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin theme editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */
"""

brut = open('settings_data.origine.json', encoding='utf-8').read()
d = json.loads(brut[brut.index('{'):])

# ---- palette Titanio Vero, relevée sur le site de référence ----------------
NERO   = "#121212"   # fond général
BIANCO = "#FFFFFF"   # texte principal
GRIGIO = "#A8A8A8"   # texte secondaire
LINEA  = "#2A2A2A"   # filets et bordures
ROSSO  = "#BF092F"   # bouton d'achat, bandeau d'annonce
CREMA  = "#FFFFFF"   # tiroir panier (fond clair, comme ta capture)
CREMA_LIGNE = "#E4DDD2"

def applique(bloc):
    bloc["color_palette"] = {
        "background": NERO,
        "foreground": BIANCO,
        "color1":     GRIGIO,
        "color2":     LINEA,
    }
    # bouton principal : rouge plein, texte blanc, angles francs
    bloc["palette_primary_button_background"] = ROSSO
    bloc["palette_primary_button_text"]       = BIANCO
    bloc["palette_primary_button_border"]     = ROSSO
    bloc["primary_button_border_width"]       = 0
    bloc["button_border_radius_primary"]      = 10
    # bouton secondaire : contour clair sur fond sombre
    bloc["palette_secondary_button_background"] = "rgba(0,0,0,0)"
    bloc["palette_secondary_button_text"]       = BIANCO
    bloc["palette_secondary_button_border"]     = "#3A3A3A"
    bloc["secondary_button_border_width"]       = 1
    bloc["button_border_radius_secondary"]      = 10
    # tiroir panier : fond clair
    bloc["drawer_background_color"] = CREMA
    bloc["drawer_text_color"]       = NERO
    bloc["drawer_border_color"]     = CREMA_LIGNE
    # champs de saisie
    bloc["palette_input_background"] = "#1C1C1C"
    bloc["palette_input_text"]       = BIANCO
    bloc["palette_input_border"]     = LINEA
    bloc["inputs_border_radius"]     = 10
    # infobulles
    bloc["popover_background_color"] = "#1C1C1C"
    bloc["popover_text_color"]       = BIANCO
    bloc["popover_border_color"]     = LINEA
    # pastilles promo : rouge
    bloc["badge_sale_background_color"] = ROSSO
    bloc["badge_sale_text_color"]       = BIANCO
    bloc["badge_corner_radius"]         = 8
    bloc["badge_sold_out_background_color"] = LINEA
    bloc["badge_sold_out_text_color"]       = GRIGIO
    # sélecteur de variantes : encadré clair, sélection blanche
    bloc["palette_variant_background"] = "rgba(0,0,0,0)"
    bloc["palette_variant_text"]       = BIANCO
    bloc["palette_variant_border"]     = "#3A3A3A"
    bloc["palette_selected_variant_background"] = "rgba(0,0,0,0)"
    bloc["palette_selected_variant_text"]       = BIANCO
    bloc["palette_selected_variant_border"]     = BIANCO
    bloc["variant_button_border_width"] = 1
    bloc["variant_button_radius"]       = 10
    # ajout rapide
    bloc["quick_add_background"] = "#1C1C1C"
    bloc["quick_add_text"]       = BIANCO
    # cartes
    bloc["card_corner_radius"]    = 14
    bloc["product_corner_radius"] = 14
    # ---- typographie : échelle mesurée sur le site de référence ------------
    bloc["type_size_paragraph"] = "15"
    bloc["type_size_h1"] = "44"
    bloc["type_size_h2"] = "34"
    bloc["type_size_h3"] = "26"
    bloc["type_size_h4"] = "20"
    bloc["type_size_h5"] = "14"
    bloc["type_size_h6"] = "12"
    bloc["type_line_height_h1"] = "display-tight"
    bloc["type_line_height_h2"] = "display-tight"
    bloc["logo_height"] = 34
    bloc["logo_height_mobile"] = 30
    return bloc

applique(d["current"])
applique(d["presets"]["Horizon"])

open('settings_data.json','w',encoding='utf-8').write(entete + json.dumps(d, indent=2, ensure_ascii=False) + "\n")
print("écrit :", len(open('settings_data.json',encoding='utf-8').read()), "octets")
