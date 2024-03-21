
**README pour le script de génération de code Java à partir de DotUML**

**Description :**

Ce script Python permet de transformer une description de classes en notation DotUML en code Java. Il analyse le texte DotUML, extrait les informations des classes, de leurs attributs, et génère le code Java correspondant, incluant les annotations pour la persistance (JPA) et l'accès aux données (getters et setters).

**Fonctionnalités :**

Extraction des définitions de classe et de leurs attributs à partir d'un texte DotUML.
Conversion des types de données DotUML en types de données Java.
Génération de code Java avec annotations JPA pour chaque classe extraite.
Génération de méthodes getters et setters pour chaque attribut de classe.

**Comment ça marche ?**

Le script lit un texte DotUML, recherche les déclarations de classes et d'attributs à l'aide d'expressions régulières, et génère ensuite du code Java pour chaque classe trouvée. Les types de données DotUML sont ajustés pour correspondre aux types Java standard. Le code Java généré inclut des annotations pour la persistance des données (JPA) et des méthodes d'accès aux attributs de chaque classe (getters et setters).

**Limitations :** 

Le script ne gère pas toutes les nuances et caractéristiques de la notation DotUML.
Les relations entre les classes (par exemple, les associations, les héritages) ne sont pas prises en compte dans la génération du code.
Nous avons pas réussi à générer les classes abstraite elle sont mise comme "public"
