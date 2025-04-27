# Liste des mots possibles pour le jeu du pendu
# Assurons-nous que les mots font bien 8 lettres ou moins
LISTE_MOTS = [
    "python", "ordinateur", "programmation", "developpeur",
    "fonction", "variable", "module", "algorithme", "boucle",
    "condition", "structure", "donnees", "fichier", "console",
    "clavier", "souris", "ecran", "reseau", "internet", "web",
    "script", "langage", "syntaxe", "erreur", "bug", "classe",
    "objet", "methode", "attribut", "heritage", "polymorphisme",
    "module", "paquet", "import", "export", "bibliotheque",
    "cadre", "test", "debug", "commit", "push", "pull",
    "branche", "fusion", "depot", "distant", "local", "version"
]

# On va filtrer la liste pour garder uniquement les mots de 8 lettres maximum
LISTE_MOTS = [mot.lower() for mot in LISTE_MOTS if len(mot) <= 8]

# Nombre de chances autorisées au joueur
NBR_CHANCES = 8

# Nom du fichier où seront enregistrés les scores
CHEMIN_SCORES = "C:/Users/Vincent/Downloads/scores"
