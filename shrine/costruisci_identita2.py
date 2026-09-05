#!/usr/bin/env python3
"""Deuxième moitié des réglages globaux : sections globales et valeurs d'usine."""
import json

NERO, NERO_2, BIANCO, ROSSO = "#121212", "#1C1C1C", "#FFFFFF", "#BF092F"
current = json.load(open("_current.json", encoding="utf-8"))

# ---- tiroir panier : mêmes blocs que Shrine, textes en italien ------------
cart_blocks = {
    "6269cf6e-8e24-4068-8e2a-35bb4addad4e": {"type": "countdown_timer", "settings": {
        "timer_text": "<strong>Carrello riservato per [timer]</strong>",
        "timer_duration": 300, "font_size": "1.4", "color_scheme": "inverse",
        "margin_top": 0, "margin_bottom": 15}},
    "926ea95f-fd8a-43e7-b215-de4f6cbc19f9": {"type": "checkpoints_bar", "disabled": True, "settings": {
        "goal_type": "subtotal", "progress_message": "Ti mancano [amount] per [next_goal]!",
        "success_message": "Hai sbloccato tutte le promozioni!",
        "labels_mobile_text_size": 10, "labels_desktop_text_size": 12, "accent_color": "accent-1",
        "enable_goal_1": True, "goal_1_label": "Spedizione gratuita", "goal_1_text": "la spedizione gratuita",
        "goal_1_amount": 40, "goal_1_icon": "local_shipping", "goal_1_icon_filled": False,
        "enable_goal_2": True, "goal_2_label": "Sconto", "goal_2_text": "uno sconto",
        "goal_2_amount": 60, "goal_2_icon": "sell", "goal_2_icon_filled": False,
        "enable_goal_3": True, "goal_3_label": "Regalo", "goal_3_text": "un regalo",
        "goal_3_amount": 80, "goal_3_icon": "redeem", "goal_3_icon_filled": False,
        "margin_top": 15, "margin_bottom": 15}},
    "058d6d0a-ba0d-48cb-9432-de85da1e5aef": {"type": "progress_bar", "disabled": True, "settings": {
        "goal_type": "subtotal", "goal": 50,
        "progress_message": "Aggiungi [amount] per la spedizione gratuita!",
        "success_message": "Spedizione gratuita sbloccata!",
        "icon": "local_shipping", "icon_filled": False, "accent_color": "accent-1",
        "margin_top": 15, "margin_bottom": 15}},
    "097b7b4f-c0b8-4073-a06b-e6d49a5aad20": {"type": "cart_items", "settings": {
        "image_size": "20", "image_link": False, "title_size": "1.5", "title_link": False,
        "displayed_variants": "compact", "prices_position": "right",
        "displayed_compare_prices": "product", "price_color": "accent-1",
        "compare_price_color": "text", "display_single_item_prices": True,
        "enable_savings": True, "savings_text": "<strong>(Risparmi [amount])</strong>",
        "savings_color": "text", "quantity_font_size": 14, "quantity_container_padding": 0,
        "quantity_corner_radius": 8, "quantity_border_width": 1, "quantity_border_color": "#3A3A3A",
        "quantity_container_color_scheme": "background-2", "quantity_input_padding": 0.7,
        "quantity_separators_opacity": 20, "quantity_padding": 0.4,
        "quantity_btns_color_scheme": "background-2", "quantity_round_btns": True,
        "quantity_outline_btns": False, "quantity_btns_icon_size": 70,
        "margin_top": 21, "margin_bottom": 21}},
    "631b0e34-4299-400e-9f4d-c107c08cce01": {"type": "discount_field", "disabled": True, "settings": {
        "bottom_separator": True, "placeholder": "Inserisci il codice sconto", "btn_label": "APPLICA",
        "error_msg": "Inserisci un codice sconto!", "margin_top": 15, "margin_bottom": 15}},
    "4f3e2a5f-006d-40ed-8370-49b15e0e427d": {"type": "subtotals", "settings": {
        "display_total_savings": True, "savings_left_text": "<strong>Risparmio</strong>",
        "savings_right_text": "<strong>-[savings]</strong>", "savings_alignment": "spaced",
        "savings_text_color": "accent-1", "savings_text_size": 16, "savings_position": "above",
        "savings_spacing": 10, "display_subtotal": True,
        "subtotal_left_text": "<strong>Totale</strong>", "subtotal_right_text": "<strong>[subtotal]</strong>",
        "subtotal_alignment": "spaced", "subtotal_text_color": "text", "subtotal_text_size": 20,
        "display_discounts": False, "discounts_label": "<strong>Sconti:</strong>",
        "discounts_alignment": "flex-start", "margin_top": 15, "margin_bottom": 15}},
    "0935e47c-9604-4faa-b47a-d61ca49c0c16": {"type": "checkout_btn", "settings": {
        "show_additional_checkout_buttons": True, "display_price": False,
        "enable_custom_color": False, "custom_color": ROSSO, "icon_scale": 120,
        "icon_spacing": 10, "margin_top": 15, "margin_bottom": 15}},
    "68fdc0a0-cd7c-40b9-97b3-a76eb7917a47": {"type": "payment_badges", "settings": {
        "enabled_payment_types": "", "margin_top": 12, "margin_bottom": 12}},
}

current["sections"] = {
    "main-password-header": {"type": "main-password-header", "settings": {"color_scheme": "background-1"}},
    "main-password-footer": {"type": "main-password-footer", "settings": {"color_scheme": "background-1"}},
    "promo-popup": {"type": "promo-popup", "settings": {
        "mode": "disabled", "popup_seconds": 5, "popup_days": 30, "display_timer": True,
        "timer_duration": 3, "layout": "image_second", "color_scheme": "background-1",
        "heading_prefix": "Iscriviti e", "heading": "RICEVI IL 10%", "heading_size": "h1",
        "heading_suffix": "", "text": "<p>Iscriviti alla nostra newsletter per offerte riservate.</p>",
        "button_label": "Iscriviti", "dismiss_btn_label": "No, grazie", "discount_code": "ESEMPIO10",
        "success_heading_prefix": "Ecco il tuo", "success_heading": "SCONTO!", "success_heading_size": "h1",
        "success_heading_suffix": "", "success_text": "<p>Usa il codice qui sotto sul tuo ordine.</p>",
        "discount_code_label": "Codice sconto:", "copy_button_label": "Copia",
        "copy_message": "Codice copiato!", "success_dismiss_btn_label": "Chiudi",
        "success_display_image": True}},
    "scroll-to-top-btn": {"type": "scroll-to-top-btn", "settings": {
        "enable_scroll_btn": True, "display_after": 400, "color_scheme": "accent-1",
        "position": "bottom-right", "offset_x": 20, "offset_y": 20}},
    "global-music-player": {"type": "global-music-player", "settings": {
        "enabled": False, "audio_src": "", "volume": 10, "position": "bottom-left",
        "offset_x": 20, "offset_y": 20, "btn_animation": True, "color_scheme": "accent-1"}},
    "cart-drawer": {"type": "cart-drawer", "blocks": cart_blocks,
        "block_order": list(cart_blocks),
        "settings": {"test_mode": False, "heading_text": "Carrello • [count] articoli",
                     "heading_alignment": "flex-start", "desktop_width": "normal",
                     "mobile_width": "full", "enable_header_bg": False, "header_bg_color": NERO_2,
                     "enable_body_bg": False, "body_bg_color": NERO_2,
                     "enable_footer_bg": False, "footer_bg_color": NERO_2}},
}
current["content_for_index"] = []

# ---- valeurs d'usine de Shrine, laissées telles quelles -------------------
presets = {"Default": {
    "logo_width": 70, "colors_solid_button_labels": "#FDFBF7", "colors_accent_1": "#9B046F",
    "gradient_accent_1": "", "colors_accent_2": "#5E3653",
    "gradient_accent_2": "linear-gradient(320deg, rgba(134, 16, 106, 1), rgba(94, 54, 83, 1) 100%)",
    "colors_text": "#2E2A39", "colors_outline_button_labels": "#2E2A39",
    "colors_background_1": "#FDFBF7",
    "gradient_background_1": "linear-gradient(180deg, rgba(240, 244, 236, 1), rgba(241, 235, 226, 1) 100%)",
    "colors_background_2": "#EDFFA7",
    "gradient_background_2": "radial-gradient(rgba(255, 229, 229, 1), rgba(255, 224, 218, 1) 25%, rgba(215, 255, 137, 1) 100%)",
    "type_header_font": "harmonia_sans_n6", "heading_scale": 130,
    "type_body_font": "harmonia_sans_n4", "body_scale": 100, "page_width": 1200,
    "spacing_sections": 36, "spacing_grid_horizontal": 40, "spacing_grid_vertical": 40,
    "buttons_border_thickness": 1, "buttons_border_opacity": 55, "buttons_radius": 10,
    "buttons_shadow_opacity": 0, "buttons_shadow_horizontal_offset": 0,
    "buttons_shadow_vertical_offset": 4, "buttons_shadow_blur": 5,
    "variant_pills_border_thickness": 0, "variant_pills_border_opacity": 10,
    "variant_pills_radius": 10, "variant_pills_shadow_opacity": 0,
    "variant_pills_shadow_horizontal_offset": 0, "variant_pills_shadow_vertical_offset": 4,
    "variant_pills_shadow_blur": 5, "inputs_border_thickness": 1, "inputs_border_opacity": 55,
    "inputs_radius": 10, "inputs_shadow_opacity": 0, "inputs_shadow_horizontal_offset": 0,
    "inputs_shadow_vertical_offset": 4, "inputs_shadow_blur": 5,
    "card_style": "card", "card_image_padding": 0, "card_text_alignment": "center",
    "card_color_scheme": "background-1", "card_border_thickness": 0, "card_border_opacity": 10,
    "card_corner_radius": 12, "card_shadow_opacity": 5, "card_shadow_horizontal_offset": 10,
    "card_shadow_vertical_offset": 10, "card_shadow_blur": 35,
    "collection_card_style": "card", "collection_card_image_padding": 0,
    "collection_card_text_alignment": "center", "collection_card_color_scheme": "background-1",
    "collection_card_border_thickness": 0, "collection_card_border_opacity": 10,
    "collection_card_corner_radius": 12, "collection_card_shadow_opacity": 5,
    "collection_card_shadow_horizontal_offset": 10, "collection_card_shadow_vertical_offset": 10,
    "collection_card_shadow_blur": 35,
    "blog_card_style": "card", "blog_card_image_padding": 0, "blog_card_text_alignment": "center",
    "blog_card_color_scheme": "background-1", "blog_card_border_thickness": 0,
    "blog_card_border_opacity": 10, "blog_card_corner_radius": 12, "blog_card_shadow_opacity": 5,
    "blog_card_shadow_horizontal_offset": 10, "blog_card_shadow_vertical_offset": 10,
    "blog_card_shadow_blur": 35,
    "text_boxes_border_thickness": 0, "text_boxes_border_opacity": 10, "text_boxes_radius": 24,
    "text_boxes_shadow_opacity": 0, "text_boxes_shadow_horizontal_offset": 10,
    "text_boxes_shadow_vertical_offset": 12, "text_boxes_shadow_blur": 20,
    "media_border_thickness": 0, "media_border_opacity": 10, "media_radius": 12,
    "media_shadow_opacity": 10, "media_shadow_horizontal_offset": 10,
    "media_shadow_vertical_offset": 12, "media_shadow_blur": 20,
    "popup_border_thickness": 1, "popup_border_opacity": 10, "popup_corner_radius": 22,
    "popup_shadow_opacity": 10, "popup_shadow_horizontal_offset": 10,
    "popup_shadow_vertical_offset": 12, "popup_shadow_blur": 20,
    "drawer_border_thickness": 1, "drawer_border_opacity": 10, "drawer_shadow_opacity": 0,
    "drawer_shadow_horizontal_offset": 0, "drawer_shadow_vertical_offset": 4, "drawer_shadow_blur": 5,
    "badge_position": "bottom left", "badge_corner_radius": 6,
    "sale_badge_color_scheme": "accent-2", "sold_out_badge_color_scheme": "inverse",
    "accent_icons": "text", "brand_headline": "", "brand_description": "<p></p>",
    "brand_image_width": "100", "social_twitter_link": "", "social_facebook_link": "",
    "social_pinterest_link": "", "social_instagram_link": "", "social_tiktok_link": "",
    "social_tumblr_link": "", "social_snapchat_link": "", "social_youtube_link": "",
    "social_vimeo_link": "", "predictive_search_enabled": True,
    "predictive_search_show_vendor": False, "predictive_search_show_price": True,
    "currency_code_enabled": False, "cart_type": "notification", "show_vendor": False,
    "show_cart_note": True, "cart_drawer_collection": "",
    "sections": {
        "main-password-header": {"type": "main-password-header", "settings": {"color_scheme": "background-1"}},
        "main-password-footer": {"type": "main-password-footer", "settings": {"color_scheme": "background-1"}},
    }}}

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
doc = {"current": current, "presets": presets, "platform_customizations": {"custom_css": []}}
open("config/settings_data.json", "w", encoding="utf-8").write(
    ENTETE + json.dumps(doc, indent=2, ensure_ascii=False) + "\n")

# --- contrôle des jetons de licence ---------------------------------------
d = json.load(open("config/settings_data.json", encoding="utf-8"))
a, f = d["current"]["animations_type"], d["current"]["fav_collection"]
print("settings_data.json :", len(open("config/settings_data.json", encoding="utf-8").read()), "octets")
print(f"jeton animations_type : {len(a)} caractères, se termine par « {a[-12:]} »")
print(f"jeton fav_collection  : {len(f)} caractères, se termine par « {f[-12:]} »")
