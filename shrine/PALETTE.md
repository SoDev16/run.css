# Palette Titanio Vero — relevée sur le site de référence

Valeurs mesurées sur les captures d'écran fournies, recoupées avec le code
source de la page. Ce ne sont pas des couleurs inventées.

| Rôle | Code | Où elle sert sur le site de référence |
|---|---|---|
| Noir | `#121212` | fond général de tout le site |
| Noir 2 | `#1C1C1C` | cartes, surfaces d'interface, champs |
| Blanc | `#FFFFFF` | texte principal |
| Gris | `#A8A8A8` | texte secondaire, légendes |
| Filet | `#2A2A2A` | séparateurs, contours |
| Rouge | `#BF092F` | bandeau d'annonce, bouton d'achat, pastilles |
| Rouge sombre | `#7B1F2A` | survols, second plan du rouge |
| Vert | `#002418` | grandes sections de marque (vue éclatée, « il tuo corpo merita ») |
| Vert vif | `#1E9E5A` | coches de validation, indicateurs positifs |
| Or | `#A3825F` | filets décoratifs, traits de séparation dans les sections vertes |
| Beige | `#BDA589` | titres des sections vertes |
| Beige clair | `#D4C7B4` | texte courant dans les sections vertes |
| Crème | `#F5F0E8` | fonds clairs ponctuels |

## Comment elles se répartissent dans Shrine

Shrine n'expose que sept couleurs globales. Le reste se pose **section par
section**, par les réglages `custom_colors_background` et
`custom_colors_text` que chaque section possède.

| Réglage global de Shrine | Couleur |
|---|---|
| `colors_background_1` | `#121212` |
| `colors_background_2` | `#1C1C1C` |
| `colors_text` | `#FFFFFF` |
| `colors_accent_1` | `#BF092F` |
| `colors_accent_2` | `#002418` |
| `colors_outline_button_labels` | `#FFFFFF` |
| `colors_solid_button_labels` | `#FFFFFF` |

Le vert placé en `accent_2` permet de basculer une section entière en vert
depuis le personnalisateur, sans code : il suffit de choisir le schéma
« accent-2 ». C'est ainsi que seront traitées la vue éclatée et la section
« Il tuo corpo merita ».

Or, beige et crème se posent au cas par cas sur les sections concernées.
