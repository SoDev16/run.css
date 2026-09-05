#!/usr/bin/env python3
"""Construit templates/product.json pour le thème brouillon.

Les textes italiens viennent de TRADUZIONI.md. Toute la géométrie s'appuie
sur des blocs natifs de Horizon, pour que chaque élément reste déplaçable et
modifiable depuis le personnalisateur, sans passer par le code.
"""
import json

NERO, BIANCO, GRIGIO, LINEA, ROSSO = "#121212", "#FFFFFF", "#A8A8A8", "#2A2A2A", "#BF092F"

def testo(html, preset="rte", couleur=None, taille="1rem", align="left"):
    s = {"text": html, "width": "100%", "max_width": "normal", "alignment": align,
         "type_preset": preset, "font_size": taille, "line_height": "normal",
         "letter_spacing": "normal", "case": "none", "wrap": "pretty",
         "background": False, "corner_radius": 0,
         "padding-block-start": 0, "padding-block-end": 0,
         "padding-inline-start": 0, "padding-inline-end": 0}
    if couleur: s["text_color"] = couleur
    return {"type": "text", "settings": s, "blocks": {}}

def icona(nom, couleur=BIANCO, largeur=22):
    return {"type": "icon", "settings": {
        "icon": nom, "width": largeur, "icon_color": couleur,
        "open_in_new_tab": False}, "blocks": {}}

def gruppo(figli, direction="column", ecart=10, largeur="fill",
           align_h="flex-start", align_v="center", **extra):
    s = {"content_direction": direction, "vertical_on_mobile": direction == "column",
         "horizontal_alignment": align_h, "vertical_alignment": align_v,
         "align_baseline": False,
         "horizontal_alignment_flex_direction_column": align_h,
         "vertical_alignment_flex_direction_column": "flex-start",
         "gap": ecart, "width": largeur, "custom_width": 100,
         "width_mobile": "fill", "custom_width_mobile": 100,
         "height": "fit", "custom_height": 100, "background_media": "none",
         "border": "none", "border_width": 1, "border_opacity": 100,
         "border_radius": 0, "toggle_overlay": False, "open_in_new_tab": False,
         "padding-block-start": 0, "padding-block-end": 0,
         "padding-inline-start": 0, "padding-inline-end": 0}
    s.update(extra)
    return {"type": "group", "settings": s, "blocks": figli,
            "block_order": list(figli)}

def riga_icona(cle, nom_icona, html):
    """Une ligne « pictogramme + phrase », alignée sur la ligne de base."""
    return gruppo({f"{cle}_i": icona(nom_icona), f"{cle}_t": testo(html, couleur=GRIGIO)},
                  direction="row", ecart=12, align_v="center")

def fisarmonica(cle, righe, **extra):
    s = {"icon": "plus", "dividers": True, "divider_color": LINEA,
         "type_preset": "h5", "text_color": BIANCO, "border": "none",
         "border_width": 1, "border_opacity": 100, "border_radius": 0,
         "padding-block-start": 0, "padding-block-end": 0,
         "padding-inline-start": 0, "padding-inline-end": 0}
    s.update(extra)
    return {"type": "accordion", "settings": s, "blocks": righe,
            "block_order": list(righe)}

def riga_fisarmonica(titolo, corpo, aperta=False, icona_nome="none"):
    return {"type": "_accordion-row",
            "settings": {"heading": titolo, "open_by_default": aperta,
                         "icon": icona_nome, "width": 24},
            "blocks": {"corpo": testo(corpo, couleur=GRIGIO)},
            "block_order": ["corpo"]}

def sezione(cle, blocchi, ordine=None, **extra):
    s = {"content_direction": "column", "vertical_on_mobile": True,
         "horizontal_alignment": "center", "vertical_alignment": "center",
         "align_baseline": False,
         "horizontal_alignment_flex_direction_column": "center",
         "vertical_alignment_flex_direction_column": "center",
         "gap": 20, "section_width": "page-width", "section_height": "",
         "section_height_custom": 100, "background_media": "none",
         "background_color": NERO, "toggle_overlay": False,
         "border": "none", "border_width": 1, "border_opacity": 100,
         "border_radius": 0,
         "padding-block-start": 56, "padding-block-end": 56}
    s.update(extra)
    return {"type": "section", "blocks": blocchi,
            "block_order": ordine or list(blocchi), "settings": s}

# =========================================================================
# 1. Bloc d'achat
# =========================================================================
dettagli = {
    "recensioni_stelle": {"type": "review", "settings": {}, "blocks": {}},
    "titolo": {"type": "product-title", "settings": {}, "blocks": {}},
    "prezzo": {"type": "price", "settings": {}, "blocks": {}},
    "sottotitolo": testo(
        "<p>Cucina senza pensieri, lava senza sfregare.</p>",
        couleur=GRIGIO, taille="1rem"),
    "argomenti": gruppo({
        "a1": riga_icona("a1", "leaf",
            "<p>Senza PFAS, PTFE e PFOA. Nessun interferente ormonale.</p>"),
        "a2": riga_icona("a2", "serving_dish",
            "<p>Naturalmente antiaderente grazie alla superficie microincisa.</p>"),
        "a3": riga_icona("a3", "lock",
            "<p>Costruzione a 5 strati, con garanzia a vita e 120 giorni di prova.</p>"),
    }, ecart=12),
    "divisore": {"type": "_divider", "settings": {}, "blocks": {}},
    "misura": {"type": "variant-picker", "settings": {}, "blocks": {}},
    "acquisto": {"type": "buy-buttons", "settings": {}, "blocks": {
        "quantity": {"type": "quantity", "settings": {}, "blocks": {}},
        "add-to-cart": {"type": "add-to-cart", "settings": {}, "blocks": {}},
        "accelerated-checkout": {"type": "accelerated-checkout", "settings": {}, "blocks": {}},
    }, "block_order": ["quantity", "add-to-cart", "accelerated-checkout"]},
    "laboratorio": gruppo({
        "lab_i": icona("clipboard", GRIGIO, 20),
        "lab_t": testo("<p>Analizzata da un laboratorio indipendente — 30 sostanze testate</p>",
                       couleur=GRIGIO, taille="0.875rem"),
    }, direction="row", ecart=10),
    "pagamento": gruppo({
        "pag_t": testo("<p>Pagamento sicuro e garantito</p>", couleur=GRIGIO,
                       taille="0.875rem", align="center"),
        "pag_i": {"type": "payment-icons", "settings": {
            "horizontal_alignment": "center", "gap": 8,
            "padding-block-start": 0, "padding-block-end": 0,
            "padding-inline-start": 0, "padding-inline-end": 0}, "blocks": {}},
    }, ecart=8, align_h="center"),
    "pratiche": fisarmonica("pratiche", {
        "spedizione": riga_fisarmonica("Spedizione",
            "<p>Spedizione gratuita su ogni ordine. La preparazione richiede da uno a due "
            "giorni lavorativi; ricevi il codice di tracciamento appena il pacco parte.</p>",
            icona_nome="truck"),
        "resi": riga_fisarmonica("Resi e rimborsi",
            "<p>Hai 120 giorni per provare la padella. Se non ti convince, la rendi e ti "
            "rimborsiamo per intero.</p>", icona_nome="return"),
        "garanzia": riga_fisarmonica("Garanzia a vita",
            "<p>Il titanio non ha rivestimenti che possano staccarsi. Se la padella cede "
            "per un difetto di fabbricazione, la sostituiamo.</p>", icona_nome="lock"),
    }),
}
ordine_dettagli = ["recensioni_stelle", "titolo", "prezzo", "sottotitolo", "argomenti",
                   "divisore", "misura", "acquisto", "laboratorio", "pagamento", "pratiche"]

acquisto = {
    "type": "product-information",
    "blocks": {
        "media-gallery": {"type": "_product-media-gallery", "static": True, "settings": {
            "media_presentation": "carousel",
            "slideshow_controls_style": "thumbnails",
            "slideshow_mobile_controls_style": "thumbnails",
            "thumbnail_position": "bottom", "thumbnail_width": 68, "thumbnail_radius": 8,
            # format carré imposé et image jamais recadrée : c'est ce qui empêche
            # une photo au mauvais ratio de décaler la page
            "aspect_ratio": "1", "media_fit": "contain",
            "constrain_to_viewport": True, "media_radius": 16,
            "zoom": True, "video_loop": True, "hide_variants": False,
            "image_gap": 8, "icons_style": "chevron", "extend_media": False,
            "padding-block-start": 0, "padding-block-end": 0,
            "padding-inline-start": 0, "padding-inline-end": 0}, "blocks": {}},
        "product-details": {"type": "_product-details", "static": True, "settings": {
            "width": "fill", "custom_width": 100, "width_mobile": "fill",
            "custom_width_mobile": 100, "height": "fit",
            "details_position": "flex-start", "gap": 18,
            "sticky_details_desktop": True, "background_media": "none",
            "border": "none", "border_width": 1, "border_opacity": 100,
            "border_radius": 0,
            "padding-block-start": 0, "padding-block-end": 0,
            "padding-inline-start": 0, "padding-inline-end": 0},
            "blocks": dettagli, "block_order": ordine_dettagli},
    },
    "block_order": ["media-gallery", "product-details"],
    "settings": {
        "content_width": "content-center-aligned", "desktop_media_position": "left",
        "equal_columns": False, "limit_details_width": True, "gap": 40,
        # barre d'achat collante native, sans code
        "enable_sticky_add_to_cart": True,
        "background_color": NERO,
        "padding-block-start": 24, "padding-block-end": 40},
}

# =========================================================================
# 2. Les quatre garanties
# =========================================================================
def garanzia(cle, nom_icona, titolo):
    return gruppo({f"{cle}_i": icona(nom_icona, BIANCO, 28),
                   f"{cle}_t": testo(f"<p>{titolo}</p>", couleur=GRIGIO,
                                     taille="0.875rem", align="center")},
                  ecart=8, align_h="center")

garanzie = sezione("garanzie", {
    "g1": garanzia("g1", "truck", "Spedizione gratuita e resi facili"),
    "g2": garanzia("g2", "stopwatch", "120 giorni di garanzia"),
    "g3": garanzia("g3", "lock", "Garanzia a vita"),
    "g4": garanzia("g4", "leaf", "100% priva di tossine"),
}, content_direction="row", gap=16, horizontal_alignment="space-between",
   vertical_alignment="flex-start", vertical_on_mobile=False,
   **{"padding-block-start": 36, "padding-block-end": 36,
      "border": "solid", "border_width": 1, "border_color": LINEA,
      "border_opacity": 100})

# =========================================================================
# 3. Phrase de rupture, révélée au défilement
# =========================================================================
rivelazione = sezione("rivelazione", {
    "frase": {"type": "jumbo-text", "settings": {
        "text": "È ora di ripensare le tue padelle.",
        "font": "heading", "alignment": "center", "line_height": "1",
        "letter_spacing": "-0.03em", "case": "none",
        "text_effect": "reveal", "animation_repeat": False,
        "text_color": BIANCO}, "blocks": {}},
}, **{"padding-block-start": 80, "padding-block-end": 80})

# =========================================================================
# 4. Les trois arguments longs
# =========================================================================
argomenti = sezione("argomenti", {
    "titolo": testo("<h2>Un nuovo standard di sicurezza, prestazioni e durata.</h2>",
                    preset="h3", couleur=BIANCO, align="center"),
    "pieghe": fisarmonica("pieghe", {
        "salute": riga_fisarmonica(
            "Titanio puro — il metallo più sicuro a contatto con il corpo",
            "<p>Usato da decenni negli impianti medici per la sua biocompatibilità. "
            "Non è tossico e non reagisce con gli alimenti.</p>", aperta=True),
        "purezza": riga_fisarmonica(
            "Antiaderente senza sostanze chimiche",
            "<p>La superficie è microincisa, non rivestita. Nessuna pellicola che si "
            "stacca col tempo, perché non c'è pellicola.</p>"),
        "confronto": riga_fisarmonica(
            "Nessun trasferimento di metalli nel cibo",
            "<p>Resiste agli utensili in metallo, al forno e alla lavastoviglie.</p>"),
    }),
}, gap=24)

# =========================================================================
# 5. Questions fréquentes
# =========================================================================
faq = sezione("faq", {
    "titolo": testo("<h2>Le domande che ci fate più spesso</h2>",
                    preset="h3", couleur=BIANCO, align="center"),
    "elenco": fisarmonica("elenco", {
        "q1": riga_fisarmonica("È adatta all'induzione?",
            "<p>Sì. La padella funziona su induzione, gas, piastra elettrica e "
            "vetroceramica.</p>"),
        "q2": riga_fisarmonica("Come si usa la prima volta?",
            "<p>Lavala con acqua tiepida e sapone, asciugala, poi scalda a fuoco medio "
            "con un filo d'olio. Il titanio dà il meglio a fuoco medio, non altissimo.</p>"),
        "q3": riga_fisarmonica("Si può lavare in lavastoviglie?",
            "<p>Sì. Non c'è alcun rivestimento che possa rovinarsi.</p>"),
        "q4": riga_fisarmonica("Quale misura scelgo?",
            "<p>La 26 cm è la più versatile per due persone. La 28 cm serve quando "
            "cucini spesso per tre o quattro.</p>"),
        "q5": riga_fisarmonica("E se non mi convince?",
            "<p>Hai 120 giorni per provarla. La rendi e ti rimborsiamo per intero.</p>"),
    }),
}, gap=24)

gabarit = {
    "sections": {
        "main": acquisto,
        "garanzie": garanzie,
        "rivelazione": rivelazione,
        "argomenti": argomenti,
        "faq": faq,
    },
    "order": ["main", "garanzie", "rivelazione", "argomenti", "faq"],
}

open("templates/product.json", "w", encoding="utf-8").write(
    json.dumps(gabarit, indent=2, ensure_ascii=False) + "\n")
print("templates/product.json :",
      len(open("templates/product.json", encoding="utf-8").read()), "octets")
