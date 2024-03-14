# projetBMO Louen Toquin & Joseph Tartivel

Pour des raisons de simplification nous avons modéliser les cas nomianaux et exceptionnels dans un seul diagramme. Ceux ci sont modélisés à l'aide d'un "alt".


**Consultation des Paris:**

Acteurs
ParieurBookmaker : Représente l'utilisateur du système qui peut être soit un parieur soit un bookmaker. Cet acteur initie le processus de consultation des paris.
Système Paris en ligne : Plateforme sur laquelle les paris sont placés, gérés et consultés.

Flux Principal
L'utilisateur (ParieurBookmaker) initie la consultation en demandant à voir les paris disponibles.
Le système vérifie la présence de paris dans la base de données.

Cas Nominal - Présence de paris
Si un ou plusieurs paris existent, le système affiche la liste des paris à l'utilisateur.
Cas Exceptionnel - Aucun pari
Si aucun pari n'est disponible, le système affiche un message d'erreur informant l'utilisateur qu'il n'y a pas de paris à consulter.

Après l'affichage des paris ou le message d'erreur, l'utilisateur quitte l'affichage des paris.

Conclusion
Ce diagramme montre le processus de consultation des paris par l'utilisateur, traitant à la fois le cas où des paris sont disponibles et le cas où aucun pari n'est présent. Le système répond de manière appropriée pour garantir que l'utilisateur est informé de la situation des paris.

**Consulter les résultats:**

Acteurs
Parieur : Utilisateur du système qui souhaite consulter les résultats des événements sportifs sur lesquels il a parié ou qu'il suit.
Système Paris en ligne : Plateforme numérique où les parieurs peuvent consulter les résultats des événements sportifs.

Flux Principal
Le Parieur initie le processus en demandant à consulter les résultats.
Le Système Paris en ligne procède à la vérification de la disponibilité des résultats.

Cas Nominal - Présence de résultats
Si des résultats sont disponibles, le système les affiche pour le parieur.
Cas Exceptionnel - Aucun résultat
Si aucun résultat n'est disponible, le système affiche un message d'erreur informant le parieur de l'absence de résultats.

Après la consultation, le parieur quitte l'affichage des résultats.

Conclusion
Le diagramme de séquence décrit comment le système de paris en ligne doit réagir lorsque le parieur demande à voir les résultats des événements. Cela inclut la gestion appropriée des situations où les résultats ne sont pas encore disponibles, assurant ainsi une expérience utilisateur cohérente et informative.

**Inscription Utilisateur:**

Acteurs
Utilisateur : La personne qui souhaite s'inscrire et créer un nouveau compte sur la plateforme.
Système : La plateforme en ligne qui traite les inscriptions des nouveaux utilisateurs.

Flux Principal
L'Utilisateur initie le processus en faisant une demande d'inscription au système.
Le Système affiche le formulaire d'inscription.
L'Utilisateur remplit le formulaire avec ses informations personnelles et le soumet pour validation.
Le Système valide les informations soumises.

Cas de Nominal - Informations Validées
Si les informations sont validées, le Système confirme l'inscription et affiche un message de confirmation.
Cas Exceptionnel - Informations Invalide
Si les informations sont invalides, le Système indique les erreurs à l'Utilisateur et demande la correction.
L'Utilisateur corrige les informations et resoumet le formulaire.
Si les informations sont désormais valides, le Système confirme l'inscription et affiche un message de confirmation. Si elles sont encore invalides, le processus de correction est répété.

Après l'inscription (réussite ou non) l'utilisateur quitte l'inscription

Conclusion
Le diagramme de séquence s'assure que le processus d'inscription est clair et gère les cas où les informations ne sont pas correctes, en assurant un retour d'information adéquat et en permettant à l'Utilisateur de corriger les erreurs pour compléter l'inscription.

**MAJ Paris**

Acteurs
Bookmaker : La personne qui souhaite mettre à jours la liste des paris
Système : La plateforme de paris en ligne.

Flux Principal
L'Utilisateur initie le processus en faisant une demande de mise à jours des paris.
Le Système affiche les paris.
L'Utilisateur selectionne le pari à mettre à jour.
Le Système envoie le formulaire necessaire pour mettre à jour.
L'utilisateur renvoie le formulaire complété

Cas de Nominal - Informations Valides
Si les informations sont validées, le Système confirme la mise à jour des paris.
Cas Exceptionnel - Informations Invalides
Si les informations sont invalides, le Système indique les erreurs à l'Utilisateur et demande la correction en renvoyant le formulaire. Dans ce cas là le système boucle au renvoie du formulaire.

Après la mise à jour (réussite ou non) l'utilisateur quitte l'inscription.

Conclusion
Le diagramme de séquence s'assure que le processus de mise à jour est clair et gère les cas où les informations ne sont pas correctes, en assurant un retour d'information adéquat et en permettant au bookmaker de corriger les erreurs pour compléter la maj.