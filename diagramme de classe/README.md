# projetBMO Louen Toquin & Joseph Tartivel

Ce document vise à expliquer la modélisation du diagramme UML "Paris en ligne".

Introduction :
Le diagramme UML fournit une représentation visuelle des classes et de leurs relations dans le système "Paris en ligne". Ce système permet aux parieurs de placer des paris sur différents événements sportifs et aux bookmakers de les créer. Il est composé de plusieurs entités clés telles que les parieurs, les bookmakers, les paris, les types de paris, les événements sportifs et les différents sports.

Classes et leurs attributs :
1. Parieur : Représente les utilisateurs qui placent des paris. Ils ont un identifiant utilisateur, un email, un mot de passe, un portefeuille pour stocker leurs jetons, une liste de paris en cours et une liste de paris passés (modélisé par "listParisPassés : list" dans le diagramme).
   
2. Bookmaker : Représente les admins du systeme de paris. Ils ont un identifiant, un email et un mot de passe.

3. Pari : Représente un pari placé par un parieur et créé par un bookmaker. Il a un identifiant, un montant, une indication si le pari est gagné et une cote. Il est lié à un type de pari et à un événement sportif.

4. TypePari : Classe abstraite représentant le type de pari. Elle est spécialisée en deux sous-classes : TypePariSimple et TypePariAvance.
    4.1. TypePariSimple : Represente un pari sur le gagant du match ou de la course, l'int associé correspond soit au numéro de l'équipe (1 ou 2 et 0 pour un match nul) soit le numéro du cheval parié gagnant.
    4.2. TypeParisAvance : Représente  un pari dit "avancé", par exemple "+ de 1.5 buts dans le match" ou "joueur 1 ne concède pas plus de 3 jeux sur le match". le string détail correspond à la description textuelle du Pari.

5. EvenementSportif : Représente un événement sportif sur lequel les paris sont placés. Il a un nom, une date de début et une indication si l'événement est terminé. Il est associé à un sport.

6. Sport : Classe abstraite représentant différents sports. Elle est spécialisée en plusieurs sous-classes telles que Foot, Tennis, Basket, et Course.

7. SetTennis : Représente un ensemble de jeux dans un match de tennis. Il a un numéro de set, un nombre de jeux pour chaque joueur, un nombre de points pour le jeu actuel, et une indication si le set est terminé. Nous faisons le choix de créer une classe set afin de représenter le résultat exact du match au jeu près.

8. Cheval : Représente un cheval dans une course hippique. Il a un nom, un numéro et une place dans la course.

Relations :
- Les parieurs et les bookmakers sont liés aux paris, car les parieurs placent des paris et les bookmakers les proposent.
- Les différents types de paris sont associés aux paris.
- Les événements sportifs sont liés aux paris car les paris sont placés sur ces événements.
- Les différents sports sont spécialisés à partir de la classe abstraite Sport.
- Les sets de tennis sont liés aux matchs de tennis.
- Les chevaux sont associés aux courses, car ils participent à ces événements.

Interprétations et hypothèses :
1. Un parieur peut avoir plusieurs paris en cours ou passés, mais un pari est associé à un seul parieur.
2. De même, un bookmaker peut proposer plusieurs paris, mais un pari est proposé par un seul bookmaker.
3. Les types de paris permettent une flexibilité dans la définition de différents types de paris, tels que les paris simples ou avancés.
4. Chaque pari est associé à un événement sportif sur lequel il est placé.
5. Chaque événement sportif est lié à un type spécifique de sport.
6. Dans le tennis, un match est composé de plusieurs sets, chacun ayant son propre déroulement. Un match a maximum 5 sets.
7. Dans une course, plusieurs chevaux peuvent participer, et chaque cheval a un numéro et une place associée dans la course.

Ces interprétations et hypothèses fournissent une base solide pour la conception et le développement du système de paris en ligne.