classDiagram
    class Personne {
        -_nom: str
        -_age: int
        -_bio: str
        +nom: property
        +age: property
        +bio: property
        +__init__(nom: str, age: int, bio: str)
        +__str__()
    }
    
    class Joueur {
        -liste_carte: list
        -meilleur_main: str
        -ajouter_carte_fait: bool
        +dict_joueur: dict
        +__init__(nom, age, bio)
        +meilleur_main_joueur()
        +piger_dans_lautre(target_nom)
        +voir_informations()
        +ajouter_carte_joueur()
        +afficher_carte_deck()
        +piger_carte_hasard()
        +melanger_carte_joueur()
        +sauvegarder_joueur()
        +load()
        +__str__()
    }
    
    class Carte_jeux {
        -tt_liste_carte: list
        -lst_carte_supprimer: list
        -_instance_carte: Carte_jeux
        +__init__()
        +get_instance()
        +creation_carte()
        +supprimer_carte(une_carte, list_supprimer_carte)
        +sauvegarder_carte()
        +load()
        +__str__()
    }
    
    class Carte {
        <<enumeration>>
        PIQUE
        COEUR
        CARREAU
        TREFLE
    }
    
    class Carte_chiffre {
        <<enumeration>>
        Un
        DEUX
        TROIS
        QAUTRE
        CINQ
        SIX
        Sept
        HUIT
        NEUF
        DIX
        KING
        VALET
        QUEEN
    }
    
    Personne <|-- Joueur : inherits
    Joueur --> Carte_jeux : uses
    Carte_jeux --> Carte : uses
    Carte_jeux --> Carte_chiffre : uses
