# Guide de contribution

Tout le monde peut proposer une modification, même sans être développeur. Les
contrôles automatiques protègent le site : une erreur est détectée **avant** d'être
publiée.

## Proposer une modification en 5 étapes

1. **Créez une branche** depuis la branche principale, par exemple
   `contenu/adresse-email`.
2. **Modifiez ou créez la page** en Markdown. Pour un nouvel objet, partez du
   [modèle de page](modele.md).
3. **Ouvrez une merge request.** Le modèle de description s'affiche
   automatiquement : complétez-le.
4. **Attendez le pipeline.** S'il est rouge, cliquez sur le job en échec : le message
   indique la page et la ligne à corriger.
5. **Faites relire** par l'équipe responsable du contenu. Après validation et fusion,
   le site est mis à jour automatiquement en quelques minutes.

## Vérifier en local (facultatif)

```bash
pip install -r requirements.txt
python scripts/verifier_pages.py
mkdocs serve
```

Le site est alors visible sur `http://127.0.0.1:8000` et se recharge à chaque
modification.

## Règles

Voir les [conventions](conventions.md) : nommage des fichiers, rédaction, branches
et contrôles.
