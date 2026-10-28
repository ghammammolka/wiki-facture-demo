# Mini WikiFacture

Ce référentiel explique **chaque objet présent sur une facture** : ce qu'il signifie,
où la donnée est stockée, comment la consulter, qui peut la mettre à jour et quand
elle est obligatoire.

!!! info "Projet de démonstration"
    Projet personnel réalisé par Molka Ghammam pour illustrer une démarche
    d'industrialisation d'un référentiel documentaire. Les contenus et les noms de
    systèmes sont **fictifs** et sans lien avec une entreprise réelle.

## Comment lire ce wiki

- Parcourez les objets par **zone de la facture** (en-tête, client, paiement) dans
  [Objets de la facture](objets/index.md).
- Ou utilisez la **recherche** en haut de la page : essayez « échéance » ou « e-mail ».
- Chaque page suit le même [modèle](contribuer/modele.md) : vous retrouvez toujours
  les mêmes rubriques au même endroit.

## Comment ce site est produit

Les pages sont écrites en Markdown dans un dépôt GitLab. À chaque merge request, un
pipeline GitLab CI vérifie automatiquement :

1. le format Markdown (linting) ;
2. que chaque page d'objet respecte le modèle ;
3. que tous les liens internes fonctionnent ;
4. que le site se construit sans avertissement.

Quand la merge request est fusionnée, le site est **publié automatiquement** sur
GitLab Pages. Pour proposer une modification, voir le
[guide de contribution](contribuer/index.md).
