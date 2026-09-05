#!/usr/bin/env python3
"""Rétablit l'en-tête et le pied de page dans les réglages globaux.

Shrine définit les blocs du pied de page ici et non dans footer-group.json :
les omettre ferait disparaître le logo, les liens et la newsletter.
"""
import json

NERO, NERO_2, BIANCO, ROSSO = "#121212", "#1C1C1C", "#FFFFFF", "#BF092F"
s = open("config/settings_data.json", encoding="utf-8").read()
entete, d = s[:s.index("{")], json.loads(s[s.index("{"):])

d["current"]["sections"]["header"] = {"type": "header", "settings": {
    "sticky_header_type": "on-scroll-up", "show_line_separator": True,
    "color_scheme": "background-1", "logo_link": "/",
    "logo_position": "middle-center", "menu": "main-menu",
    "menu_type_desktop": "dropdown", "highlight_active_link": True,
    "highlighted_link_color_scheme": "accent-1", "products_mega_menu_links": "",
    "products_mega_menu_display_collection_products": True,
    "products_mega_menu_display_collection_images": True,
    "products_mega_menu_display_collection_images_on_mobile": True,
    "mobile_menu_title": "Menu", "secondary_menu": "",
    "menu_color_scheme": "background-1", "mobile_logo_position": "center",
    "display_search": False, "margin_bottom": 0,
    "padding_top": 18, "padding_bottom": 18}}

footer_blocks = {
    "fc645871-d789-4cfa-8584-4f8a29b6ce92": {"type": "image", "settings": {
        "image_width": 100, "alignment": "center", "url": "",
        "width_desktop": 4, "width_mobile": "2"}},
    "1c647602-cc00-4009-a058-976435c8ee9e": {"type": "link_list", "settings": {
        "heading": "Assistenza", "menu": "footer",
        "width_desktop": 4, "width_mobile": "1"}},
    "24f208fd-0898-43eb-af23-d74f8420ab37": {"type": "email_signup", "settings": {
        "heading": "Iscriviti alla newsletter",
        "subtext": "<p>Offerte riservate e novità, senza inondarti la casella.</p>",
        "button_type": "solid", "button_label": "Iscriviti",
        "button_style_secondary": False, "width_desktop": 4, "width_mobile": "2"}},
}
d["current"]["sections"]["footer"] = {"type": "footer", "blocks": footer_blocks,
    "block_order": list(footer_blocks), "settings": {
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
        "custom_colors_outline_button": BIANCO}}

open("config/settings_data.json", "w", encoding="utf-8").write(
    entete + json.dumps(d, indent=2, ensure_ascii=False) + "\n")
print("sections globales :", list(d["current"]["sections"]))
print("blocs du pied de page :", [b["type"] for b in footer_blocks.values()])
