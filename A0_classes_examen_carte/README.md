# S9 Évaluation sur l'introduction à l'orienté-objet
L'évaluation vaut pour 15% de la session et est notée sur 30 pts.
Elle a une durée prévue d'environ 2h.

## Éléments évalués
- Capacité à décomposer un problème avec une approche orientée objet
- Capacité à modéliser une solution orientée objet
- Capacité à programmer des classes et implémenter la logique applicative en manipulant des objets
- Capacité à manipuler des fichiers contenant des objets sérialisés

## Modalités de l'évaluation
- Il s’agit d’un travail individuel.
- Remettre le code source et le diagrammme de votre application dans l’espace prévu à cet effet sur GitHub Classroom avant la fin du cours. 
- Aucun retard ne sera accepté – le dernier archivage (_commit_) avant l’heure de remise sera la version corrigée. 

### Matériel autorisé à l'examen

- Tous vos fichiers personnels, exercices, corrigés, etc.
- Sites internet suivants (télécharger vos notes de cours personnelles au besoin - ex. en PDF)
  - https://projets420.gitbook.io/notes-de-cours/
  - https://projets420.gitbook.io/notes-de-cours/420-2g4-programmation-orientee-objet
  - https://github.com/420-2G4-Prog-orientee-objet
  - https://docs.python.org/
  - https://mermaid.js.org/
  - https://app.diagrams.net/
  - https://cegepoutaouais-lea.omnivox.ca/

## Instructions
- L'examen est constitué d'une mise en situation, le jeu de carte
- Vous avez 3 tâches à compléter à l'aide de cette mise en situation
- Pour chaque tâche, une durée approximative est fournie. Il est suggéré de passer à une autre tâche après ce temps et d'y revenir par la suite au besoin.

## Exigences
- Vous devez représenter un jeu de carte
- Une carte à jouer doit avoir une valeur et une couleur.
  - Valeurs : DEUX, TROIS, QUATRE, CINQ, SIX, SEPT, HUIT, NEUF, DIX, VALET, DAME, ROI, AS
  - Couleurs : CARREAU, TREFLE, COEUR, PIQUE
- Il doit être possible d'obtenir la valeur numérique d'une carte. (2-10, valet (11), dame (12), roi(13), as(14))
- Un paquet de carte doit contenir toutes les 52 cartes possibles. Sans JOKER.
- Les cartes du paquet peuvent être mélangées.
- Une carte du paquet peut être pigé au hasard. Lorsqu'elle est pigée, elle n'est plus dans le paquet.
- Les cartes du paquet peuvent être affichées.
- Les cartes dans la main d'un joueur peuvent aussi être mélangées et on peut piger dans celle-ci.
- Il doit être possible d'ajouter une carte dans la main d'un joueur.
- La main d'un joueur est composée d'au maximum 5 cartes.
- Il doit être possible de voir la valeur totale (numérique) des cartes dans la main d'un joueur.
- La main obtenue ayant la plus haute valeur totale est placée dans une propriété `meilleure_main` disponible dans toutes les mains
  (il ne s'agit pas de la meilleure main théorique, mais plutôt de la meilleure main obtenue pendant l'utilisation de l'application)

Vous devez utiliser, au besoin, là où c'est approprié :
- Enum
- Héritage 
- Propriétés et méthodes de classe
- Accesseurs et mutateurs

## Tâches
### Partie 1 - Diagramme (environ 30 minutes)
Vous devez en produire le diagramme de classe et le mettre dans le même dossier.
Vous pouvez le faire en `mermaid` dans un fichier **diagramme.md** 
ou avec [draw.io](https://app.diagrams.net) et l'exporter en image nommée **diagramme.png**.

Note : vous n'avez pas besoin d'utiliser les relations d'aggrégation et de composition

### Partie 2 - Implémentation (environ 60 minutes)
- Créez les fichiers et classes nécessaires pour répondre aux exigences.
- Vous n'avez pas besoin de créer une application avec un menu : vous pouvez vous créer un script (main.py) 
  pour vous aider à dépanner, mais ce n'est pas exigé.

> **⚠️ Avertissement**  
> Si votre code Python diffère du plan, mettez à jour votre diagramme.


### Partie 3 - Tests unitaires (environ 30 minutes)
Ajoutez des tests unitaires qui permettent de vérifier : 
- Que la valeur numérique de la dame de pique est bien 12
- Que lors de la création d'un paquet, celui-ci contient 52 cartes
- Que lors de la pige d'une carte du paquet, celle-ci est retirée du paquet
- Que lors de la création de la main d'un joueur, celle-ci est vide
- La valeur numérique totale des cartes dans la main d'un joueur

Vous pouvez évidemment créer plus de tests que demandé.

## Grille d'évaluation
| **Critères   d’évaluation     et indicateurs**               | **Excellent (100%)**                                         | **Bien à très bien <br />(60 – 80%)**                        | **Insuffisant <br />(40% ou moins)**                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Production d’un diagramme de classes  conforme à l’énoncé**  <br />5 pts | Production d’un diagramme clair et complet où toutes  les classes, les attributs et les méthodes sont présents, ainsi que **leur  type et leur visibilité**. L’héritage et les associations simples sont  correctement représentées. Identification claire des propriétés et des  méthodes de classe. | Globalement, le travail effectué démontre la capacité  à représenter une situation en orienté-objet. Quelques détails sont à  corriger, mais toutes les classes sont présentes de même que les méthodes et  les attributs les plus importants. | Le diagramme ne correspond pas à l’énoncé dans son  ensemble. Globalement, le travail effectué ne démontre pas la capacité à  représenter une situation en orienté-objet |
| **Programmation adéquate des classes et  méthodes selon les principes de l’orienté-objet**   <br />10 pts | Le travail effectué démontre la capacité à créer et  manipuler des objets et des classes. Dans toutes les situations, les objets  sont créés et les méthodes sont appelées adéquatement à l’aide des paramètres  appropriés. Les paramètres et retours des méthodes sont correctement typés. | Le travail soumis répond aux exigences de façon  globale. Capacité à créer et manipuler les objets dans la plupart des  situations. | Le travail soumis ne démontre pas la capacité à créer  et manipuler des classes et des objets (moins de 3 démonstrations) |
| **Programmation rigoureuse de la logique  applicative et gestion appropriée des erreurs**  <br />10 pts | Le programme est fonctionnel et conforme à toutes les  exigences. Toutes les données sont adéquatement validées selon les exigences  fournies. | Quelques détails sont à corriger, mais le code est  globalement conforme à la majorité des exigences fournies au niveau de la  logique applicative. | Le programme ne répond pas à la majorité des  exigences. Il peut, par exemple, demander des corrections majeures pour être  fonctionnel. |
| **Production de tests adéquats**  <br />5 pts                | Les tests demandés (5/5) ont été correctement  implémentés et s’exécutent sans erreur. Ils sont pertinents. | La plupart des tests demandés (3/5) ont été  correctement implémentés et s’exécutent sans erreur. | Peu de méthodes de tests unitaires implémentées OU  les tests ne sont pas pertinents dans l’ensemble |
