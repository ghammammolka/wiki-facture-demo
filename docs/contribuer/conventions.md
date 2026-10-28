# Conventions

## Fichiers et arborescence

- Une page par objet, dans `docs/objets/`.
- Nom de fichier en minuscules, sans accent, mots séparés par des tirets :
  `date-echeance.md`, pas `Date Échéance.md`.
- Toute nouvelle page est ajoutée à la navigation dans `mkdocs.yml`, dans la bonne
  zone de la facture.

## Rédaction

- Phrases courtes, vocabulaire du métier, pas de jargon technique inutile.
- Les noms de systèmes et d'outils sont en **gras** à leur première apparition.
- Les valeurs d'exemple sont entre accents graves : `42,99 €`.
- Les liens vers d'autres objets sont **relatifs** : `[Montant TTC](../objets/montant-ttc.md)`.

## Branches et commits

- Une branche par modification : `contenu/date-echeance` ou `outil/pipeline-liens`.
- Messages de commit au présent, qui disent ce qui change :
  `Ajoute la page Mode de paiement`.

## Contrôles automatiques

| Contrôle                | Outil                           | Ce qu'il vérifie                         |
| ----------------------- | ------------------------------- | ---------------------------------------- |
| Format Markdown         | markdownlint                    | Titres, listes, espaces, style homogène  |
| Respect du modèle       | `scripts/verifier_pages.py`     | Métadonnées et rubriques obligatoires    |
| Liens internes          | `scripts/verifier_pages.py`     | Chaque lien pointe vers une page existante |
| Construction du site    | `mkdocs build --strict`         | Aucune page orpheline ni avertissement   |
