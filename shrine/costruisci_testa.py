#!/usr/bin/env python3
"""En-tête et pied de page Titanio Vero, à partir des groupes de Shrine.

Le bandeau reprend les trois messages italiens déjà validés. Aucune remise
chiffrée : elle exigerait un prix de référence sur trente jours.
Les pictogrammes n'utilisent que des noms déjà présents dans la
configuration d'origine de Shrine, donc sûrement valides.
"""
import json

NERO, BIANCO, ROSSO = "#121212", "#FFFFFF", "#BF092F"
ENTETE = """/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin theme editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */
"""

def annuncio(testo, icona):
    return {"type": "announcement", "settings": {
        "text": testo, "text_alignment": "center",
        "mobile_text_size": 13, "desktop_text_size": 14,
        "icon": icona, "filled_icon": False,
        "mobile_icon_size": 16, "desktop_icon_size": 18,
        "desktop_layout": "horizontal", "mobile_layout": "horizontal",
        "hidden_products": "", "enable_specific_display": False,
        "displayed_products": ""}}

annunci = {
    "annuncio_lancio":   annuncio("Saldi di lancio Titanio Vero", "sell"),
    "annuncio_garanzie": annuncio("Spedizione gratuita · Garanzia a vita · 120 giorni di prova", "local_shipping"),
    "annuncio_purezza":  annuncio("Senza PFAS, PTFE e PFOA", "check_circle"),
}

header_group = {
    "name": "t:sections.header.name",
    "type": "header",
    "sections": {
        "fe1c8c67-b84c-4466-a515-70df3134c1c0": {
            "type": "announcement-bar",
            "blocks": annunci,
            "block_order": list(annunci),
            "settings": {
                "columns_desktop": 1, "columns_mobile": 1,
                "desktop_spacing": 28, "mobile_spacing": 16,
                "show_separator": False, "color_scheme": "accent-1",
                "slider_mobile": True, "slider_desktop": True,
                "type": "loop", "autoplay": True, "autoplay_speed": 4,
                "hidden_products": "", "enable_specific_display": False,
                "displayed_products": "",
                "padding_top": 11, "padding_bottom": 11,
                "custom_colors_background": ROSSO,
                "custom_gradient_background": "",
                "custom_colors_text": BIANCO}},
        "header": {
            "type": "header",
            "settings": {
                "sticky_header_type": "on-scroll-up", "show_line_separator": True,
                "color_scheme": "background-1", "logo_link": "/",
                # logo centré, comme sur le site de référence
                "logo_position": "middle-center", "menu": "main-menu",
                "menu_type_desktop": "dropdown", "highlight_active_link": True,
                "highlighted_link_color_scheme": "accent-1",
                "products_mega_menu_links": "",
                "products_mega_menu_display_collection_products": True,
                "products_mega_menu_display_collection_images": True,
                "products_mega_menu_display_collection_images_on_mobile": True,
                "mobile_menu_title": "Menu", "secondary_menu": "",
                "menu_color_scheme": "background-1", "mobile_logo_position": "center",
                # boutique mono-produit : la recherche n'a rien à chercher
                "display_search": False, "margin_bottom": 0,
                "padding_top": 18, "padding_bottom": 18}},
    },
    "order": ["fe1c8c67-b84c-4466-a515-70df3134c1c0", "header"],
}

footer_group = {
    "name": "t:sections.footer.name",
    "type": "footer",
    "sections": {
        "footer": {"type": "footer", "settings": {
            "color_scheme": "background-1", "enable_follow_on_shop": False,
            "show_social": False, "enable_country_selector": False,
            "enable_language_selector": False, "payment_enable": True,
            "enabled_payment_types": "", "show_policy": True,
            "branding_text": "<a href=\"https://shrinesolutions.io/\" target=\"_blank\" title=\"Shrine Theme\">Powered by Shrine</a>",
            "margin_top": 0, "padding_top": 44, "padding_bottom": 24,
            "custom_colors_background": NERO, "custom_gradient_background": "",
            "custom_colors_text": BIANCO,
            "custom_colors_solid_button_background": ROSSO,
            "custom_colors_solid_button_text": BIANCO,
            "custom_colors_outline_button": BIANCO}}},
    "order": ["footer"],
}

for nom, doc in (("header-group", header_group), ("footer-group", footer_group)):
    chemin = f"sections/{nom}.json"
    open(chemin, "w", encoding="utf-8").write(ENTETE + json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    print(f"{chemin} : {len(open(chemin, encoding='utf-8').read())} octets")
