# Othello – Projet MA20

## Informations générales

* **Auteurs** : David Vilela & Aleksander Johnson  
* **Classe** : SI-Ca1a  
* **Projet** : MA20 – Reconstitution du jeu Othello  
* **Date de création** : 09.02.2026  

---

## Description du projet

Ce projet est une reconstitution du jeu **Othello (Reversi)**, réalisée en Python avec la bibliothèque **Pygame**.

Le jeu oppose deux joueurs qui placent des pions noirs et blancs sur un plateau 8x8 afin de capturer ceux de l’adversaire.

---

## Objectif du jeu

* Capturer le maximum de pions adverses  
* Contrôler le plateau  
* Avoir plus de pions que l’adversaire à la fin  

La partie se termine lorsque :

* aucun joueur ne peut jouer  

---

## Contrôles

Le jeu se joue à la souris :

* **Clic gauche** → placer un pion  
* **Bouton "Rejouer"** → relancer une partie  

---

## Fonctionnalités

* Interface graphique avec Pygame  
* Plateau 8x8 interactif  
* Affichage des coups valides  
* Retour automatique des pions capturés  
* Gestion des tours (Noir / Blanc)  
* Passage automatique si aucun coup possible  
* Score en temps réel  
* Détection de fin de partie  
* Bouton **Rejouer**  

---

## Logique du jeu

* Le plateau est représenté par une matrice 8x8  
* Chaque case peut être :
  * vide (0)
  * noire (1)
  * blanche (2)  
* Les coups sont validés uniquement s’ils capturent des pions  
* Les pions sont retournés selon les 8 directions possibles  
* Le jeu vérifie automatiquement si un joueur doit passer son tour  
* La partie se termine lorsque plus aucun coup n’est possible  

---

## Installation et exécution

### Prérequis

* Python 3.x installé  
* Pygame installé  -> pip install pygame

---

## © Copyright

© 2026 David Vilela & Aleksander Johnson. Tous droits réservés.

Ce projet a été réalisé dans le cadre du cours MA20.  
Toute reproduction, distribution ou utilisation sans autorisation préalable est interdite.
