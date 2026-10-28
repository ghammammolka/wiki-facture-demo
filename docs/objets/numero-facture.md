---
title: Numéro de facture
tags:
  - En-tête
  - Identifiant
responsable: Équipe Projets Facture
derniere_revue: 2026-10-28
---

# Numéro de facture

## Définition

Identifiant unique attribué à chaque facture. Il permet de retrouver une facture sans ambiguïté, par exemple lors d'un échange avec le service client ou d'une réclamation.

## Où est stockée la donnée

Généré par le **système de facturation** (fictif : *SI Facturation*) au moment de l'émission, puis copié dans l'**archive des factures**.

## Comment la consulter

- Outil de consultation des factures : recherche par numéro.
- Espace client en ligne : rubrique « Mes factures ».

## Qui peut la mettre à jour

Personne : le numéro est **non modifiable**. Une erreur se corrige par une facture d'avoir, qui porte son propre numéro.

## Quand est-elle obligatoire

Toujours. Une facture sans numéro n'est pas valide.

## Exemple

`FAC-2026-10-004512` : préfixe, année, mois, puis numéro séquentiel.

## Voir aussi

- [Date d'émission](date-emission.md)
- [Montant TTC](montant-ttc.md)
