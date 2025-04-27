class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self.lieu_residence = "Paris"

class Compteur:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    
    objets_crees = 0 # Le compteur vaut 0 au départ
    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur.objets_crees += 1

def main():
    """Procédure principale pour démontrer l'utilisation des classes."""
    # Création d'une personne
    personne = Personne("Doe", "John")
    print(f"Personne créée : {personne.prenom} {personne.nom}, {personne.age} ans, résidant à {personne.lieu_residence}")
    
    # Création de plusieurs compteurs
    compteur1 = Compteur()
    compteur2 = Compteur()
    print(f"Nombre d'objets Compteur créés : {Compteur.objets_crees}")

if __name__ == "__main__":
    main()

