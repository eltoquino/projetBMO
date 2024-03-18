# projetBMO Louen Toquin & Joseph Tartivel

Pour des raisons de simplification nous avons modéliser les cas nomianaux et exceptionnels dans un seul diagramme. Ceux ci sont modélisés à l'aide d'un "alt". Sauf pour le rechargement, composé de deux diagrammes de séquences.


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

**Placer un Pari**

Acteurs
Parieur : Utilisateur du système qui placer un pari.
Système Paris en ligne : Plateforme numérique où les parieurs peuvent placer des paris sur des évennements sportifs.

Flux Principal
L'Utilisateur initie le processus en selectionnant un évennement sportif.
Le Système affiche les détails de l'évennement et les options de paris.
L'Utilisateur selectionne les infos du pari.
Le Système verifie la validité du pari.

Cas exceptionnel - Match commencé

Si le match est commencé et que le pari choisi nécessite d'être placé avant le début du match alors suite à la verification, le système envoie un message d'erreur indiquant que le pari est impossible, invitant alors l'utilisateur à quitter l'interface de pari.

Cas nominal - Match non commencé

Si le  pari est validé par le systeme alors il est enregistré et le systeme envoie un récapitulatif du pari ainsi qu'une confirmation à l'utilisateur.

Après cela l'utilisateur quitte l'interface de pari et retourne à la page d'acceuil.

Conclusion
Le diagramme de séquence s'assure que le processus de placement de pari est clair et gère les cas où les informations ne sont pas correctes, en assurant un retour d'information adéquat et en permettant au bookmaker de s'assurer qu'aucun pari frauduleux ne peux être placé.

**Rechargement - Cas nominal**

Acteurs
Utilisateur : Utilisateur du système qui souhaite recharger son compte
Système Paris en ligne : Plateforme numérique où les parieurs peuvent recharger leur compte de façon sécurisé.
Banque : Plateforme numérique de la banque du client, validant ou non les virements de l'utilisateur vers le systeme de paris en ligne.

Flux Principal
L'Utilisateur initie le processus en demandant un rechargement.
Le Système affiche le formulaire sécurisé de rechargement.
Le systeme envoie les informations à la banque, sans pouvoir les consulter.
Le banque verifie la validité des informations et la faisabilité du virement.
La banque valide le virement et l'indique au systeme.
Le systeme recharge le compte et indique le succes à l'utilisateur.
L'utilisateur quitte la page ou la recharge pour recommencer.

Conclusion
Le diagramme de séquence s'assure que le processus de rechargement est clair et sécurisé pour les 3 acteurs.

**Rechargement - Cas exeptionnel**

Acteurs
Utilisateur : Utilisateur du système qui souhaite recharger son compte
Système Paris en ligne : Plateforme numérique où les parieurs peuvent recharger leur compte de façon sécurisé.
Banque : Plateforme numérique de la banque du client, validant ou non les virements de l'utilisateur vers le systeme de paris en ligne.

Flux Principal
L'Utilisateur initie le processus en demandant un rechargement.
Le Système affiche le formulaire sécurisé de rechargement.
Le systeme envoie les informations à la banque, sans pouvoir les consulter.
Le banque verifie la validité des informations et la faisabilité du virement.
La banque indique au systeme que le virement est impossible.
Le systeme indique à l'utilisateur que le virement a été refusé par la banque.
L'utilisateur quitte la page ou la recharge pour recommencer.

Conclusion
Le diagramme de séquence s'assure que le processus de rechargement est clair et sécurisé pour les 3 acteurs, même en cas d'erreur.

# Hypothèses

1. Ces diagrammes concerne la modélisation des processus clés d'un système de paris en ligne.
2. Les différents cas d'utilisation sont modélisés à l'aide de diagrammes de séquence UML pour représenter les interactions entre les acteurs et le système.
3. Chaque cas d'utilisation est décrit en détail, couvrant à la fois les flux principaux et les cas nominaux, ainsi que les cas exceptionnels.
4. Les acteurs principaux du système sont identifiés, notamment les Parieurs, les Bookmakers et le Système Paris en ligne.
5. Les interactions entre les acteurs et le système sont clairement définies, y compris les actions initiales des acteurs, les réponses du système et les différentes branches pour les cas exceptionnels.

# Interprétation

1. Les diagrammes de séquence fournissent une vue dynamique des processus impliqués dans le système de paris en ligne, montrant comment les acteurs interagissent avec le système à travers différents scénarios.
2. Chaque cas d'utilisation est bien structuré, avec des flux principaux clairs ainsi que des branches pour les cas exceptionnels, ce qui garantit une gestion appropriée des situations imprévues.
3. Les acteurs sont correctement identifiés et leurs rôles dans le système sont définis de manière précise, ce qui facilite la compréhension des interactions.
4. Les diagrammes de séquence fournissent une base solide pour la conception et le développement du système, en guidant les développeurs dans l'implémentation des fonctionnalités et des logiques de traitement.
5. L'approche de regrouper les cas nominaux et exceptionnels dans un seul diagramme, sauf pour le rechargement, permet une représentation concise et compréhensible des différentes situations possibles.

# Commentaires

1. La structure claire et détaillée des diagrammes de séquence facilite la communication entre les membres de l'équipe de développement et assure une compréhension commune des processus du système.
2. La gestion appropriée des cas exceptionnels dans les diagrammes de séquence garantit une expérience utilisateur cohérente et évite les situations imprévues qui pourraient perturber le fonctionnement du système.
3. Les hypothèses clairement définies fournissent un cadre pour interpréter les diagrammes de séquence, en s'assurant que les interactions entre les acteurs et le système sont correctement modélisées.
4. L'approche de modélisation utilisée permet une documentation efficace des fonctionnalités du système, ce qui est essentiel pour le développement, la maintenance et l'évolution future de la plateforme de paris en ligne.
5. Les diagrammes de séquence fournissent non seulement une représentation visuelle des processus, mais également une base pour la validation des exigences fonctionnelles et la planification des tests, contribuant ainsi à la qualité globale du système.