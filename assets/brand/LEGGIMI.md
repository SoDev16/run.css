# Titanio Vero — identité de marque

## Le concept

Un logotype pur : le nom en capitales grasses très espacées, un filet, puis
« VERO » en dessous, léger et étiré à la même largeur.

Les terminaisons des lettres sont **coupées en biseau** — le geste du métal
taillé. Le A est un chevron sans barre, comme un pan coupé. C'est ce qui donne
au mot son caractère : rien n'est arrondi, tout est facetté.

## Les fichiers

| Fichier | Où l'utiliser |
|---|---|
| `logo-principale.svg` | Usage courant : en-tête du site, e-mails, factures |
| `logo-principale-bianco.svg` | Le même sur fond foncé ou sur photo |
| `logo-principale-verde.svg` | Le même en vert profond, sur fond clair |
| `logo-su-verde.svg` | Bloc complet, blanc sur vert — bandeaux, publicités |
| `logo-tm.svg` | Avec le ™ — voir la note ci-dessous |
| `monogramma.svg` | Le monogramme TV seul |
| `favicon.svg` | Onglet du navigateur, à partir de 16 px |
| `apple-touch-icon.png` | Icône iPhone / Android (180 px) |

### ™ ou ® ?

Le fichier par défaut n'en porte aucun. Utilise `logo-tm.svg` (**™**) dès
maintenant : il ne demande aucune formalité et signale que tu revendiques la
marque. Le **®** est réservé aux marques effectivement enregistrées — s'en
servir avant l'enregistrement est une infraction en Italie comme en France.
Une fois ton dépôt EUIPO accordé, je te sors la version ®.

Les `.svg` sont vectoriels : ils restent nets à n'importe quelle taille, du favicon
au panneau d'exposition. Ce sont eux qu'il faut charger dans Shopify.
Les `.png` sont là pour les outils qui refusent le SVG (certains réseaux sociaux,
quelques imprimeurs).

## Les couleurs

| Rôle | Code |
|---|---|
| Bronze — logo, boutons, accents | `#B57C46` |
| Sable — fonds doux, bordures | `#BCA588` |
| Vert profond — sections sombres, favicon | `#002418` |
| Crème — fonds clairs | `#F5F0E8` |
| Rouge — prix barrés, urgence | `#D43140` |
| Vert — « en stock », validations | `#42C216` |

## Trois règles

1. **De l'air autour.** Laisse au minimum la hauteur du poinçon comme marge libre.
2. **Une seule couleur à la fois.** Le logo est monochrome : bronze, blanc ou vert.
   Jamais de dégradé, jamais d'ombre portée.
3. **Ne déforme pas.** Redimensionne toujours en conservant les proportions.

## Le lettrage

Dessiné en vectoriel, lettre par lettre — ce n'est pas une police du commerce.
Personne d'autre ne l'a, et il n'y a **aucune licence à payer**, y compris sur
du packaging imprimé.

`genera-logo.py` conserve l'alphabet : lance-le pour régénérer tous les
fichiers, ou appelle `logotipo("MOT", "SOUS-TITRE", couleur)` pour composer
un autre mot dans le même dessin.
