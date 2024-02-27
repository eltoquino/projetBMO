# projetBMO Louen Toquin & Joseph Tartivel

Ce document explique les diagrammes d'états créés pour les différentes classes du système de paris en ligne.

Parieur
Le diagramme d'états pour la classe Parieur présente les états possibles et les transitions entre eux :

Non connecté: Cet état représente le parieur qui n'est pas connecté au système.
Connecté: Cet état représente le parieur qui est connecté au système après s'être authentifié avec succès.
Les transitions possibles sont les suivantes :

Login: Transition de l'état "Non connecté" à l'état "Connecté" lorsque le parieur se connecte avec succès.
Logout: Transition de l'état "Connecté" à l'état "Non connecté" lorsque le parieur se déconnecte du système.

Bookmaker
Le diagramme d'états pour la classe Bookmaker est similaire à celui du Parieur :

Non connecté: Cet état représente le bookmaker qui n'est pas connecté au système.
Connecté: Cet état représente le bookmaker qui est connecté au système après s'être authentifié avec succès.

Les transitions possibles sont les mêmes que pour la classe Parieur : "Login" et "Logout".

Pari
Le diagramme d'états pour la classe Pari présente les états possibles pour un pari :

En cours: Cet état représente un pari en cours, avant que son résultat ne soit annoncé.
Terminé: Cet état représente un pari terminé, après que son résultat a été annoncé.
La transition possible est la suivante :

Résultat annoncé: Transition de l'état "En cours" à l'état "Terminé" lorsque le résultat du pari est annoncé.