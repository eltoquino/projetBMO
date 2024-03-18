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

# Hypothèses

1. Le projet comprend la modélisation des états pour les différentes classes du système de paris en ligne.
2. Les diagrammes d'états sont utilisés pour représenter les états possibles et les transitions entre eux pour chaque classe.
3. Chaque classe, notamment Parieur, Bookmaker et Parier, possède ses propres états spécifiques et transitions associées.
4. Les états initiaux représentent les conditions de départ, tandis que les états finaux ou terminaux indiquent les résultats ou les conditions finales pour chaque processus.
5. Les transitions entre les états représentent les actions effectuées par les acteurs ou les changements de statut dans le système.

# Interprétation

1. Les diagrammes d'états offrent une vue claire et structurée des processus impliqués dans le système de paris en ligne, en mettant en évidence les différents états possibles pour chaque classe.
2. Chaque diagramme d'états présente des états initiaux, finaux et intermédiaires pertinents pour le processus spécifique de la classe, ce qui facilite la compréhension des interactions entre les différents composants du système.
3. Les transitions entre les états décrivent les actions ou les événements qui déclenchent les changements de statut, permettant ainsi de suivre le flux des processus à travers le système.
4. Les mécanismes de choix, tels que les transitions conditionnelles, sont utilisés pour représenter les décisions prises par le système en fonction des résultats des événements sportifs ou des paris.
5. Les états et les transitions sont définis de manière à refléter de manière précise les règles métier et les comportements attendus dans le système de paris en ligne.

# Commentaires

1. La modélisation des diagrammes d'états fournit une base solide pour la conception et le développement du système, en guidant les développeurs dans l'implémentation des logiques de traitement et des fonctionnalités spécifiques.
2. Les diagrammes d'états permettent une visualisation efficace des processus et des flux de données à travers le système, facilitant ainsi la communication entre les membres de l'équipe de développement.
3. Les mécanismes de choix ajoutent une flexibilité au modèle en permettant au système de prendre des décisions en fonction des conditions spécifiques, améliorant ainsi la robustesse et l'adaptabilité du système.
4. La clarté des états et des transitions facilite également la documentation des fonctionnalités du système, ce qui est essentiel pour la maintenance et l'évolution future de la plateforme de paris en ligne.
5. Les diagrammes d'états contribuent à garantir la cohérence et la fiabilité du système en décrivant de manière précise les comportements attendus et les règles de gestion à suivre dans différentes situations.