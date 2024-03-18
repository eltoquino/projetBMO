# projetBMO Louen Toquin & Joseph Tartivel

Ce document explique les diagrammes d'états créés pour les différentes classes du système de paris en ligne.

**Parieur**
Le diagramme d'états pour la classe Parieur présente les états possibles et les transitions entre eux :

Non connecté: Cet état représente le parieur qui n'est pas connecté au système.
Connecté: Cet état représente le parieur qui est connecté au système après s'être authentifié avec succès.
L'initialState peut ici représenter l'état avant la création du compte

Les transitions possibles sont les suivantes :

Login: Transition de l'état "Non connecté" à l'état "Connecté" lorsque le parieur se connecte avec succès.
Logout: Transition de l'état "Connecté" à l'état "Non connecté" lorsque le parieur se déconnecte du système.

**Bookmaker**
Le diagramme d'états pour la classe Bookmaker est similaire à celui du Parieur :

Non connecté: Cet état représente le bookmaker qui n'est pas connecté au système.
Connecté: Cet état représente le bookmaker qui est connecté au système après s'être authentifié avec succès.
L'initialState peut ici représenter l'état avant la création du compte

Les transitions possibles sont les mêmes que pour la classe Parieur : "Login" et "Logout".

**Parier**
Ce diagramme d'état modélise le processus de pari dans le système de paris en ligne, depuis la création de l'événement jusqu'à la détermination du résultat du pari.

EventPasCommencé : L'état initial avant le début de l'événement sportif. Les paris peuvent être placés à ce stade.
EventCommencé : L'état durant lequel l'événement sportif est en cours. Les paris peuvent être placés à ce stade.
EventTerminé : L'état indiquant que l'événement sportif est terminé. Aucun nouveau pari ne peut être placé, et le processus de vérification des paris commence.
PariPlacé : L'état représentant un pari qui a été placé. Ce peut être avant ou pendant l'événement sportif.
PariGagnant : L'état final pour un pari qui s'est avéré gagnant après la vérification du résultat de l'événement.
PariPerdant : L'état final pour un pari qui s'est avéré perdant après la vérification du résultat de l'événement.

Les transitions possibles sont les suivantes :

Création de l'événement : Transition de l'état initial à EventPasCommencé.
Création du pari avant l'événement : Transition de EventPasCommencé à PariPlacé.
Création du pari en cours d'événement : Transition de EventCommencé à PariPlacé.
Début de l'événement : Transition de EventPasCommencé à EventCommencé.
Fin de l'événement : Transition de EventCommencé à EventTerminé.

Mécanisme de Choix :

Après la fin de l'événement, le système atteint un point de décision (représenté par le pseudo-état de choix c) où il détermine si un pari est gagnant, perdant ou annulé, basé sur le résultat de l'événement et de possibles invalidation.
Si le pari est vérifié comme gagnant, la transition mène à l'état PariGagnant.
Si le pari est vérifié comme perdant, la transition mène à l'état PariPerdant.
Si l'évennement ou le pari est annulé, la transition mène à l'état PariAnnulé. Exemple "Match annulé".