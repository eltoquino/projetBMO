import re

# Texte dotUML simulé pour l'exemple
uml_input = """
class Parieur { 
    private email : string 
    private password : string 
    private portefeuille : int 
    private listParisEncours : list 
    private listParisPassés : list

    public parieur(userId : string, email : string, password : string) 
    public login(email : string, password : string) 
    public recharger(montant : int) 
    public parier(pari : pari, montant : double) }

class Bookmaker { 
    private email : string 
    private password : string

    public bookmaker(email : string, password : string) 
    public créerPari(Pari : pari) 
    public créerEvent(EvemmenementSportif : event) }

class Pari { 
    private montant : double 
    private gagné : bool 
    private cote : int

    public pari(montant : double, cote : int) 
    public majPari() 
    public getTerminé() : bool 
    public getEvenement() : EvenementSportif 
    public getTypePari() : TypePari 
    public getMontant() : double public getCote(): int }

abstract class TypePari { }

class TypePariSimple { 
    private resultatChoisi : int

    public typePariSimple(int : resultatChoisi) 
    public getResultatChoisi() : int 
    public setResultatChoisi(int : resultatChoisi) }

class TypePariAvance { 
    private details : String

    public typePariAvance(details : String) 
    public getDetails() : String 
    public setDetails(details : String) }

class EvenementSportif { 
    private nom : String 
    private dateDebut : Date 
    private terminé : bool

    public EvenementSportif(nom : String, dateDebut : Date) 
    public getNom() : String 
    public getSport() : Sport 
    public getDateDebut() : Date 
    public setTerminé() }

abstract class Sport { }

class Foot { 
    private equipe1 : string 
    private equipe2 : string 
    private miTemps : int 
    private scoreEquipe1 : int 
    private scoreEquipe2 : int 
    private tempsRestant : int

    public foot(equipe1 : string, equipe2 : string) 
    public majMatch()
    public afficheScore() 
    public getGagnant() : int 
    public getDifButs() : int 
    public getNbButsE1() : int 
    public getNbButsE2() : int 
    public getNbButsTotal() : int 
    public getScoreMiTemps() : int 
    public setScoreMiTemps(int : scoreMitemps) }

class Tennis { 
    private Joueur1 : string 
    private Joueur2 : string 
    private duréeEnMin : int

    public tennis(Joueur1 : string, Joueur2 : string) 
    public majMatch() 
    public getGagnant() : int 
    public getGagnantNemeSet(set : int) : int 
    public donneScore() }

class SetTennis { 
    private combientiemeSet : int 
    private nbJeuxJ1 : int 
    private nbJeuxJ2 : int 
    private nbPointsJeuActuelJ1 : int 
    private nbPointsJeuActuelJ2 : int 
    private setTerminé : bool

    public setTennis(combientiemeSet : int) 
    public majSet() 
    public getGagnantSet() : int }

class Basket { 
    private equipe1 : string 
    private equipe1 : string
    private quartTemps  int 
    private scoreEquipe1 : int      
    private scoreEquipe2 : int 
    private tempsRestant : int

    public basket(equipe1 : string, equipe1 : string) 
    public majMatch() 
    public getGagnant() : int 
    public getDifPoints() : int public donneScore() }

class Course { 
    private duréeEnMin : int 
    private listeCheveaux : list

    public course(listeCheveaux : list) 
    public majCourse() 
    public getGagnant() : int 
    public getPlace(numeroCheval : int) : int 
    public donneResultat() : list }

class Cheval { 
    private nom : String 
    private numero : int 
    private place : int

public cheval(nom : String, numero : int); 
public majPlace() }

align { EvenementSportif Sport Course }

Bookmaker "1" -- "" Pari; Bookmaker "1" -- "" EvenementSportif; Parieur "1" -- "" Pari; TypePari "1" -- "" Pari; TypePari <-- TypePariSimple; TypePari <-- TypePariAvance; EvenementSportif "1" -- "" Pari; Sport "1" -- "" EvenementSportif; Foot-->Sport; Tennis-->Sport; Basket-->Sport; Course-->Sport; SetTennis "5" -- "1" Tennis; Cheval ""--"" Course }
}
"""
def adjust_type(dotuml_type):
    """Ajuste les types de données DotUML aux types Java."""
    return {
        'string': 'String',
        'bool' : 'boolean',
        'list' : 'List'  
    }.get(dotuml_type, dotuml_type)

def parse_dotuml_to_java(uml_input):
    # Regex pour extraire les définitions de classe et les attributs
    class_pattern = re.compile(r'class\s+(\w+)\s*{\s*([^}]*)\s*}', re.DOTALL)
    attribute_pattern = re.compile(r'(private|public)\s+(\w+)\s+:\s+(\w+)')
    
    for class_match in class_pattern.finditer(uml_input):
        class_name = class_match.group(1)
        class_body = class_match.group(2)
        attributes = attribute_pattern.findall(class_body)
        
        yield generate_java_class(class_name, attributes)

def generate_java_class(class_name, attributes):
    java_code = f'import javax.persistence.*;\nimport org.openxava.annotations.*;\nimport java.util.*;\n\n@Entity\n@Getter\n@Setter\npublic class {class_name} {{\n\n'
    
    for visibility, attr_type, attr_name in attributes:
        adjusted_type = adjust_type(attr_type)
        java_code += f'    private {attr_name} {adjusted_type};\n\n'
        
    # Générer les getters et setters
    for visibility, attr_type, attr_name in attributes:
        adjusted_type = adjust_type(attr_name)
        cap_attr_name = attr_type[0].upper() + attr_type[1:]
        java_code += f'    public {attr_name} get{cap_attr_name}() {{\n        return {attr_type};\n    }}\n\n'
        java_code += f'    public void set{cap_attr_name}({attr_name} {attr_type}) {{\n        this.{attr_type} = {attr_type};\n    }}\n\n'
    
    java_code += '}\n'
    return java_code

# Générer et afficher le code Java pour chaque classe définie dans le texte DotUML
for java_class_code in parse_dotuml_to_java(uml_input):
    print(java_class_code)
