# Mini WikiFacture

Référentiel documentaire en Markdown qui explique chaque objet d'une facture, publié
automatiquement en site web par un pipeline GitLab CI.

Projet personnel de démonstration réalisé par **Molka Ghammam**. Les contenus et les
noms de systèmes sont fictifs.

## Ce que montre ce projet

| Besoin                               | Solution dans ce dépôt                                       |
| ------------------------------------ | ------------------------------------------------------------ |
| Générer le site automatiquement      | MkDocs + thème Material, publié sur GitLab Pages             |
| Pipelines GitLab CI                  | `.gitlab-ci.yml` : qualité, construction, publication        |
| Linting Markdown                     | markdownlint, configuré dans `.markdownlint-cli2.yaml`       |
| Vérification des liens               | `scripts/verifier_pages.py` + `mkdocs build --strict`        |
| Tests de build                       | Construction stricte du site à chaque merge request          |
| Normalisation du contenu             | Modèle de page, métadonnées et rubriques vérifiés en CI      |
| Navigation et recherche              | Onglets par zone de facture, recherche en français, étiquettes |
| Bonnes pratiques de contribution     | Guide, conventions, modèle de merge request                  |

## Le pipeline

```text
Merge request  ──►  lint-markdown ─┐
                    verifier-modele-et-liens ─┴─►  construire-site   (pas de publication)

Branche main   ──►  lint-markdown ─┐
                    verifier-modele-et-liens ─┴─►  pages   ──►  site publié sur GitLab Pages
```

Si un contrôle échoue, la suite du pipeline ne s'exécute pas : une erreur n'arrive
jamais sur le site publié.

## Lancer en local

```bash
pip install -r requirements.txt
python scripts/verifier_pages.py
mkdocs serve
```

Puis ouvrir `http://127.0.0.1:8000`.

## Démonstration d'un contrôle qualité

1. Créer une branche `demo/lien-casse`.
2. Dans `docs/objets/montant-ttc.md`, remplacer `date-echeance.md` par
   `date-echeanse.md`.
3. Ouvrir une merge request : le job `verifier-modele-et-liens` échoue et indique la
   page et le lien en cause.
4. Corriger, pousser : le pipeline repasse au vert.

## Structure

```text
.
├── .gitlab-ci.yml                   pipeline
├── .gitlab/merge_request_templates/ modèle de merge request
├── .markdownlint-cli2.yaml          règles de format Markdown
├── mkdocs.yml                       configuration et navigation du site
├── requirements.txt
├── docs/
│   ├── index.md
│   ├── objets/                      une page par objet de la facture
│   └── contribuer/                  guide, modèle, conventions
├── modeles/objet-facture.md         modèle à copier pour un nouvel objet
└── scripts/verifier_pages.py        contrôle du modèle et des liens
```
