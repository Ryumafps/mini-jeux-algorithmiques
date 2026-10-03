# Projet Rush Hour
---

## Description

Rush Hour est un jeu de puzzle dans lequel des véhicules de différentes tailles sont placés sur une grille 6x6. L'objectif est de faire sortir la voiture rouge par la droite en déplaçant les autres véhicules qui bloquent son passage. Ce projet implémente une version textuelle du jeu ainsi qu'un solveur automatique utilisant l'algorithme de recherche en largeur.

## Fonctionnalités

* Représentation textuelle du plateau de jeu
* Déplacement des véhicules selon les règles du jeu
* Solveur automatique qui trouve le chemin optimal pour résoudre le puzzle
* Plusieurs configurations prédéfinies (niveaux débutant et expert)
* Visualisation des mouvements de la solution

## Structure du projet

Le projet est divisé en quatre fichiers Python principaux :

* `vehicule.py` : Définit la classe `Vehicule` qui représente les véhicules du jeu
* `plateau.py` : Définit la classe `Plateau` qui représente la grille de jeu
* `solveur.py` : Implémente l'algorithme de recherche en largeur pour résoudre les puzzles
* `main.py` : Point d'entrée du programme qui permet de sélectionner une configuration et de la résoudre

## Journal de développement

### Semaine 1 : Saisie d'une configuration, liste des mouvements possibles

Durant cette première semaine, j'ai implémenté les classes de base du projet :

* Classe `Vehicule` pour représenter les voitures et camions de différentes tailles
* Classe `Plateau` pour gérer la grille de jeu et les positions des véhicules
* Méthodes pour ajouter/supprimer des véhicules et vérifier les mouvements possibles

À la fin de cette semaine, le programme pouvait :

* Représenter des véhicules avec leurs propriétés (identifiant, position, longueur, orientation)
* Placer ces véhicules sur un plateau de jeu
* Vérifier si un véhicule peut avancer ou reculer selon les règles du jeu
* Obtenir la liste des déplacements possibles pour tous les véhicules

### Semaines 2 et 3 : Résolution du casse-tête

Durant ces deux semaines, j'ai développé l'algorithme de résolution :

* Implémentation de la classe `SolveurRushHour` qui utilise la recherche en largeur
* Méthodes pour gérer les états visités et éviter les boucles
* Fonctions pour représenter la solution sous forme de séquence de mouvements

À la fin de cette période, le programme pouvait :

* Trouver le chemin optimal (le moins de mouvements) pour résoudre n'importe quelle configuration soluble
* Détecter les configurations impossibles à résoudre
* Afficher la séquence complète des mouvements nécessaires pour résoudre le puzzle

### Semaine 4 : Recherche de solution particulière

Durant cette dernière semaine, j'ai finalisé le projet :

* Création de plusieurs configurations prédéfinies (débutant et expert)
* Interface utilisateur simple pour sélectionner une configuration
* Optimisation de l'algorithme de résolution
* Création de tests complets pour valider le bon fonctionnement du code
* Rédaction de la documentation

## Exemples d'exécution

### Exemple 1 : Résolution d'un niveau débutant

```
Rush Hour
----------------
1. Utiliser la configuration de la carte débutant n°1
2. Utiliser la configuration de la carte débutant n°2
3. Utiliser la configuration de la carte expert n°1
4. Utiliser la configuration de la carte expert n°2
5. Utiliser la configuration de la carte expert n°3

Sélectionnez une option (1-5): 1

Modèle choisi :

AA...I
P..E.I
PRRE.I
P..E..
B...CC
B.XXX.


Résolution du plateau en cours...

Solution trouvée en 13 déplacements:
AA...I
P..E.I
PRRE.I
P..E..
B...CC
B.XXX.

Déplacement 1: Véhicule A se déplace en avant
.AA..I
P..E.I
PRRE.I
P..E..
B...CC
B.XXX.

...
```

### Exemple 2 : Résolution d'un niveau expert

```
Rush Hour
----------------
1. Utiliser la configuration de la carte débutant n°1
2. Utiliser la configuration de la carte débutant n°2
3. Utiliser la configuration de la carte expert n°1
4. Utiliser la configuration de la carte expert n°2
5. Utiliser la configuration de la carte expert n°3

Sélectionnez une option (1-5): 3

Modèle choisi :

A..OOO
ABBC..
RRDC.X
..DEEX
..FGGX
..FQQQ

Résolution du plateau en cours...

Solution trouvée en 73 déplacements:

...
```

## Utilisation

* Exécutez le programme principal :
  ```
  python main.py
  ```
* Sélectionnez une configuration en entrant un nombre entre 1 et 5
* Le programme affichera la solution avec tous les mouvements nécessaires
