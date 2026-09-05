#!/usr/bin/env python3
"""Description produit : les deux arguments et les quatre caractéristiques.

Shrine n'expose pas de bloc « texte à pictogramme » dans son bloc d'achat, et
sa section produit fait 312 ko — impossible d'en lire le schéma pour en
énumérer les blocs. Ce contenu passe donc par la description du produit,
placée juste sous le prix, avec des classes que je définis moi-même et que
j'habille par le CSS de la section. Aucun réglage deviné.
"""
import json

def ico(d):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round">'
            f'{d}</svg>')

DIAMANTE = ico('<path d="M6 3h12l3 6-9 12L3 9z"/><path d="M3 9h18"/><path d="M9 3l3 18 3-18"/>')
INDUZIONE = ico('<rect x="3" y="4" width="18" height="16" rx="2"/>'
                '<circle cx="8.5" cy="9.5" r="2.5"/><circle cx="15.5" cy="9.5" r="2.5"/>'
                '<path d="M6 16h12"/>')
FORNO = ico('<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 8h18"/>'
            '<circle cx="7" cy="5.5" r=".6"/><circle cx="10" cy="5.5" r=".6"/>'
            '<rect x="6" y="11" width="12" height="7" rx="1"/>')
LAVASTOVIGLIE = ico('<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 8h18"/>'
                    '<circle cx="7" cy="5.5" r=".6"/><path d="M9 12c1.5 1.5 4.5 1.5 6 0"/>'
                    '<path d="M9 15.5c1.5 1.5 4.5 1.5 6 0"/>')
SENZA = ico('<circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/>')
SUPERFICIE = ico('<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/>'
                 '<circle cx="12" cy="12" r="1.6"/>')

CARATTERISTICHE = [
    (DIAMANTE, "Indistruttibile", "Per sempre"),
    (INDUZIONE, "Induzione", "Pronta all'uso"),
    (FORNO, "Forno", "Sicura"),
    (LAVASTOVIGLIE, "Lavastoviglie", "Sicura"),
]

righe = "".join(
    f'<li>{i}<b>{t}</b><span>{s}</span></li>' for i, t, s in CARATTERISTICHE)

DESCRIZIONE = (
    '<div class="tv-argomenti">'
    f'<p>{SENZA}<span><strong>Senza PFAS, PTFE e PFOA.</strong> '
    'Nessun interferente ormonale.</span></p>'
    f'<p>{SUPERFICIE}<span><strong>Superficie microincisa</strong>, '
    'naturalmente antiaderente.</span></p>'
    '</div>'
    f'<ul class="tv-caratteristiche">{righe}</ul>'
    '<p class="tv-nota">Cucina senza pensieri, lava senza sfregare. '
    'Costruzione a 5 strati, con garanzia a vita e 120 giorni di prova.</p>'
)
open("descrizione.html", "w", encoding="utf-8").write(DESCRIZIONE)
print(len(DESCRIZIONE), "caractères")
