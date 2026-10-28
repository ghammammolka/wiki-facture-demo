# Modèle de page

Chaque objet de la facture a **sa propre page**, construite sur ce modèle. Les
rubriques sont obligatoires et dans cet ordre : le pipeline refuse une page à
laquelle il en manque une.

Copiez le fichier `modeles/objet-facture.md` du dépôt, renommez-le, puis remplissez-le.

```markdown
---
title: Nom de l'objet
tags:
  - Zone de la facture
responsable: Équipe propriétaire du contenu
derniere_revue: AAAA-MM-JJ
---

# Nom de l'objet

## Définition

## Où est stockée la donnée

## Comment la consulter

## Qui peut la mettre à jour

## Quand est-elle obligatoire

## Exemple

## Voir aussi
```

## Les métadonnées en tête de page

| Champ            | Rôle                                                      |
| ---------------- | --------------------------------------------------------- |
| `title`          | Nom affiché de l'objet                                    |
| `tags`           | Zone et thèmes, utilisés pour l'index par étiquette       |
| `responsable`    | Équipe à contacter en cas de question sur le contenu      |
| `derniere_revue` | Date de la dernière relecture, pour repérer les pages anciennes |
