#!/usr/bin/env python3
"""Contrôle qualité du Mini WikiFacture.

Vérifie que :
  1. chaque page d'objet (docs/objets/*.md, hors index) respecte le modèle :
     métadonnées obligatoires et rubriques dans l'ordre attendu ;
  2. chaque lien Markdown relatif de docs/ pointe vers un fichier existant.

Sort avec le code 1 si une erreur est trouvée, ce qui fait échouer le pipeline.
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
DOCS = RACINE / "docs"
OBJETS = DOCS / "objets"

METADONNEES = ["title", "tags", "responsable", "derniere_revue"]
RUBRIQUES = [
    "Définition",
    "Où est stockée la donnée",
    "Comment la consulter",
    "Qui peut la mettre à jour",
    "Quand est-elle obligatoire",
    "Exemple",
    "Voir aussi",
]
REVUE_MAX_JOURS = 365

LIEN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
BLOC_CODE = re.compile(r"```.*?```", re.S)


def lire_front_matter(texte: str) -> tuple[dict, str]:
    if not texte.startswith("---\n"):
        return {}, texte
    fin = texte.find("\n---\n", 4)
    if fin == -1:
        return {}, texte
    return yaml.safe_load(texte[4:fin]) or {}, texte[fin + 5:]


def verifier_modele(page: Path) -> list[str]:
    erreurs = []
    meta, corps = lire_front_matter(page.read_text(encoding="utf-8"))
    for champ in METADONNEES:
        if not meta.get(champ):
            erreurs.append(f"métadonnée manquante : {champ}")
    revue = meta.get("derniere_revue")
    if isinstance(revue, dt.date):
        age = (dt.date.today() - revue).days
        if age > REVUE_MAX_JOURS:
            erreurs.append(f"dernière revue il y a {age} jours (maximum {REVUE_MAX_JOURS})")
    elif revue:
        erreurs.append("derniere_revue doit être une date au format AAAA-MM-JJ")

    titres = re.findall(r"^## (.+?)\s*$", corps, flags=re.M)
    manquantes = [r for r in RUBRIQUES if r not in titres]
    for r in manquantes:
        erreurs.append(f"rubrique manquante : « {r} »")
    if not manquantes:
        ordre = [t for t in titres if t in RUBRIQUES]
        if ordre != RUBRIQUES:
            erreurs.append("les rubriques ne sont pas dans l'ordre du modèle")
    return erreurs


def verifier_liens(page: Path) -> list[str]:
    erreurs = []
    texte = BLOC_CODE.sub("", page.read_text(encoding="utf-8"))
    for cible in LIEN.findall(texte):
        if re.match(r"^[a-z]+:", cible) or cible.startswith("#"):
            continue  # lien externe ou ancre dans la même page
        chemin = cible.split("#", 1)[0]
        if not (page.parent / chemin).resolve().exists():
            erreurs.append(f"lien cassé : {cible}")
    return erreurs


def main() -> int:
    total = 0
    for page in sorted(DOCS.rglob("*.md")):
        erreurs = verifier_liens(page)
        if page.parent == OBJETS and page.name != "index.md":
            erreurs = verifier_modele(page) + erreurs
        for e in erreurs:
            print(f"ERREUR {page.relative_to(RACINE)} : {e}")
        total += len(erreurs)

    nb_pages = len(list(DOCS.rglob("*.md")))
    if total:
        print(f"\n{total} erreur(s) sur {nb_pages} pages.")
        return 1
    print(f"OK : {nb_pages} pages vérifiées, modèle et liens conformes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
