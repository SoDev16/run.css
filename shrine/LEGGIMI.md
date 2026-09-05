# Titanio Vero sur Shrine Pro

Fichiers destinés au thème **`shrinepro`**
(`gid://shopify/OnlineStoreTheme/203990499676`) sur `t3dz1k-jv.myshopify.com`.

L'arborescence reproduit celle du thème Shopify.

## Sauvegarde

Avant toute modification, la configuration d'origine a été copiée sur le thème
lui-même : `assets/originale-settings_data.json.txt`. Elle contient les jetons
de licence Shrine (`animations_type`, `fav_collection`). En cas de problème,
la restaurer par `themeFilesCopy` en sens inverse.

## Ce qui est repris de Shrine

Toute la mise en page s'appuie sur des sections et des blocs natifs de Shrine,
pour qu'ils restent déplaçables et réglables depuis le personnalisateur.

## Ce qui est volontairement absent

Aucune remise chiffrée (« -55 % », « SAVE [percentage] ») : en Italie, une
annonce de réduction exige un prix de référence des trente derniers jours
(directive Omnibus, D.Lgs. 26/2023), qu'une boutique qui ouvre ne peut pas
établir.

## Règle apprise, à respecter pour tous les fichiers de Shrine

**Modifier le fichier d'origine, ne jamais le reconstruire.**

Trois envois ont été refusés par `themeFilesUpsert` sans le moindre message
d'erreur — liste vide, aucune `userError`, fichier inchangé. À chaque fois
la cause était la même : le fichier avait été réécrit à partir de zéro au
lieu d'être chargé puis modifié.

Le fichier de réglages d'origine est conservé ici sous
`originale-settings_data.json`. Toute modification part de lui.

Corollaire : les écritures sont **asynchrones**. Relire un fichier moins de
trente secondes après l'envoi donne encore l'ancienne version, ce qui fait
prendre des écritures en cours pour des refus.

## Affirmations de la référence volontairement reformulées

Trois arguments du site de référence ne sont pas repris tels quels dans
l'accordéon des bénéfices.

| Référence | Pourquoi | Écrit à la place |
|---|---|---|
| « Conserve jusqu'à 45 % de nutriments en plus » | allégation nutritionnelle chiffrée ; le règlement CE 1924/2006 exige une substantiation scientifique | « Cuoci a fuoco medio, non altissimo » — la conduction du titane, sans chiffre |
| « Naturellement antibactérien » | une allégation antibactérienne sur un article relève du règlement biocides UE 528/2012 | « Facile da tenere pulita » — surface lisse et non poreuse |
| « Impossible à corroder », « impossible à détruire » | absolus indéfendables | « Resiste agli alimenti acidi », « Fatta per durare » |

« SlipScale™ » est une marque de la référence et n'est pas employée.

## Règle absolue : relire avant d'écrire

Un envoi de `templates/product.json` a effacé un bloc que le client avait
construit lui-même dans le personnalisateur — une comparaison de poêles en
images. Le fichier local ne contenait pas son travail, et l'écriture a
remplacé le fichier entier.

**Avant toute écriture d'un gabarit, relire la version en ligne et y
fusionner les modifications, jamais envoyer la copie locale telle quelle.**
Le champ `updatedAt` du fichier indique si le client a touché au thème
depuis le dernier envoi.
