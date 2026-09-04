# Titanio Vero — thème Shopify

Dawn 16 modifié. 25 sections sur mesure, toutes réglables dans le
personnalisateur.

## Installation

1. Shopify → **Boutique en ligne → Thèmes**
2. **Ajouter un thème → Importer un thème**
3. Dépose le fichier `.zip`
4. **Aperçu** pour vérifier, puis **Publier** quand tu es prêt

Le thème s'installe à côté de celui en place. Rien n'est écrasé, et tu peux
revenir en arrière à tout moment.

## Avant de publier, prépare ça dans Shopify

Sans ces éléments, la page s'affiche mais certaines zones restent vides.

| À créer | Ce qui s'affiche alors |
|---|---|
| **Le produit** avec prix, prix comparé, option `Misura` et photos | Prix, prix barré, sélecteur de taille, galerie |
| **Une collection** contenant le produit | La grille de la page d'accueil |
| **Les pages** Chi siamo, Contatti, Guida alle misure | Les liens du pied de page |
| **Les politiques** (Paramètres → Politiques) | Mentions légales italiennes |
| **Un menu** nommé Footer | Les colonnes du pied de page |
| **Le logo** dans le personnalisateur | En-tête et pied de page |

Le **prix comparé** est ce qui déclenche l'affichage du prix barré. Sans lui,
pas de « 389 € » rayé, pas de badge de remise.

## Ce qui se règle sans code

- Tous les textes, section par section
- Toutes les images et vidéos
- L'ordre des sections, par glisser-déposer
- Masquer une section sans la supprimer
- Ajouter ou retirer des éléments : une garantie, une question, un témoignage,
  une carte comparative, un onglet

## Les sections

**Ossature** — `tv-annuncio`, `tv-testa`, `tv-piede`

**Fiche produit** — `tv-prodotto` (galerie, prix, variantes, offres, achat),
`tv-garanzie`, `tv-schede`, `tv-fisarmonica`, `tv-impegno`, `tv-carte`,
`tv-rivelazione`, `tv-mosaico`, `tv-video`, `tv-recensioni-profili`,
`tv-strati`, `tv-faq`, `tv-recensioni`, `tv-barra-fissa`

**Accueil** — `tv-eroe`, `tv-promo`, `tv-prodotti`, `tv-striscia`,
`tv-merita`, `tv-marca`, `tv-testo`, `tv-lettera`

`tv-carte`, `tv-rivelazione` et `tv-testo` servent plusieurs fois avec des
contenus différents : ajoutes-en autant que tu veux.

## Un point sur la grille de produits

`tv-prodotti` affiche une carte aujourd'hui et une grille dès que la collection
en contiendra plusieurs. Aucun code à retoucher quand tu ajouteras la spatule
ou le couvercle.

## Ce qui reste à faire

- **Relecture de l'italien par un natif.** Voir `TRADUZIONI.md`.
- **Les photos.** Chaque emplacement porte la description de l'image attendue.
- **Les applications** — avis clients et offres groupées. Les emplacements sont
  prêts ; il reste à y brancher les applications choisies.
- **Le tiroir panier.** La maquette en contient un ; il utilise pour l'instant
  celui de Dawn, à réhabiller quand tu auras validé le reste.
