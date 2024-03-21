# projetBMO Louen Toquin & Joseph Tartivel

Ce document vise à expliquer la modélisation du diagramme de classe "Paris en ligne".

**Introduction :**
Le diagramme UML fournit une représentation visuelle des classes et de leurs relations dans le système "Paris en ligne". Ce système permet aux parieurs de placer des paris sur différents événements sportifs et aux bookmakers de les créer. Il est composé de plusieurs entités clés telles que les parieurs, les bookmakers, les paris, les types de paris, les événements sportifs et les différents sports.

**Classes et leurs attributs :**
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

**Relations :**
- Les parieurs et les bookmakers sont liés aux paris, car les parieurs placent des paris et les bookmakers les proposent.
- Les bookmakers sont associés aux évennements car c'est eux qui les crées.
- Les différents types de paris sont associés aux paris.
- Les événements sportifs sont liés aux paris car les paris sont placés sur ces événements.
- Les différents sports sont spécialisés à partir de la classe abstraite Sport.
- Les sets de tennis sont liés aux matchs de tennis.
- Les chevaux sont associés aux courses, car ils participent à ces événements.

**Interprétations et hypothèses :**
1. Un parieur peut avoir plusieurs paris en cours ou passés, mais un pari est associé à un seul parieur.
2. De même, un bookmaker peut proposer plusieurs paris, mais un pari est proposé par un seul bookmaker.
3. De même, un bookmaker peut proposer plusieurs évennements sportifs, mais un évennement sportif est proposé par un seul bookmaker.
4. Les types de paris permettent une flexibilité dans la définition de différents types de paris, tels que les paris simples ou avancés.
5. Chaque pari est associé à un unique événement sportif sur lequel il est placé. Un évennement peut avoir une infinité de paris.
6. Chaque pari est associé à un unique type de pari. Un type peut avoir une infinité de paris.
7. Chaque événement sportif est lié à un unique type spécifique de sport, un sport peut avoir une infinité de paris.
8. Dans le tennis, un match est composé de plusieurs sets, chacun ayant son propre déroulement. Un match a maximum 5 sets, et un set appartient à un unique match.
9. Dans une course, plusieurs chevaux peuvent participer, et chaque cheval a un numéro et une place associée dans la course.

Ces interprétations et hypothèses fournissent une base solide pour la conception et le développement du système de paris en ligne.


**Code dotUML**

ClassDiagram [frame=true framecolor=steelblue label="Paris en ligne"]{

class Parieur { 
  private email : string 
  private password : string 
  private portefeuille: int 
  private listParisEncours : list 
  private listParisPassés : list

  public parieur(email: string, password: string) 
  public login(email: string, password:string) 
  public recharger(montant: int) 
  public parier(pari: pari, montant: double) 
}

class Bookmaker { 
  private email : string 
  private password : string

public bookmaker(email : string, password : string) public créerPari(Pari : pari) public créerEvent(EvemmenementSportif : event) }

class Pari { private montant: double private gagné : bool private cote : int

public pari(montant: double, cote : int) public majPari() public getTerminé(): bool public getEvenement(): EvenementSportif public getTypePari(): TypePari public getMontant(): double public getCote(): int }

abstract class TypePari { }

class TypePariSimple { private resultatChoisi: int

public typePariSimple(int : resultatChoisi) public getResultatChoisi(): int public setResultatChoisi(int : resultatChoisi) }

class TypePariAvance { private details: String

public typePariAvance(details: String) public getDetails(): String public setDetails(details: String) }

class EvenementSportif { private nom: String private dateDebut: Date private terminé: bool

public EvenementSportif(nom: String, dateDebut: Date) public getNom(): String public getSport(): Sport public getDateDebut(): Date public setTerminé() }

abstract class Sport { }

class Foot { private equipe1: string private equipe2: string private miTemps: int private scoreEquipe1: int private scoreEquipe2: int private tempsRestant: int

public foot(equipe1: string, equipe2: string) public majMatch()
public afficheScore() public getGagnant(): int public getDifButs(): int public getNbButsE1(): int public getNbButsE2(): int public getNbButsTotal(): int public getScoreMiTemps(): int public setScoreMiTemps(int : scoreMitemps) }

class Tennis { private Joueur1: string private Joueur2: string private duréeEnMin: int

public tennis(Joueur1: string, Joueur2: string) public majMatch() public getGagnant(): int public getGagnantNemeSet(set: int): int public donneScore() }

class SetTennis { private combientiemeSet : int private nbJeuxJ1 : int private nbJeuxJ2 : int private nbPointsJeuActuelJ1 : int private nbPointsJeuActuelJ2 : int private setTerminé : bool

public setTennis(combientiemeSet : int) public majSet() public getGagnantSet(): int }

class Basket { private equipe1: string private equipe1: string private quartTemps: int private scoreEquipe1: int private scoreEquipe2: int private tempsRestant: int

public basket(equipe1: string, equipe1: string) public majMatch() public getGagnant(): int public getDifPoints(): int public donneScore() }

class Course { private duréeEnMin: int private listeCheveaux : list

public course(listeCheveaux : list) public majCourse() public getGagnant(): int public getPlace(numeroCheval:int): int public donneResultat(): list }

class Cheval { private nom: String private numero: int private place: int

public cheval(nom: String, numero: int); public majPlace() }

align { EvenementSportif Sport Course }

Bookmaker "1" -- "" Pari; Bookmaker "1" -- "" EvenementSportif; Parieur "1" -- "" Pari; TypePari "1" -- "" Pari; TypePari <-- TypePariSimple; TypePari <-- TypePariAvance; EvenementSportif "1" -- "" Pari; Sport "1" -- "" EvenementSportif; Foot-->Sport; Tennis-->Sport; Basket-->Sport; Course-->Sport; SetTennis "5" -- "1" Tennis; Cheval ""--"" Course }
