# pendu.py

# On importe tout ce dont on a besoin depuis nos autres fichiers
from fonctions import charger_scores, enregistrer_scores, choisir_mot, gerer_partie, saisir_lettre
from donnees import LISTE_MOTS, NBR_CHANCES, CHEMIN_SCORES

def main():
    """
    Fonction principale du jeu du Pendu.
    Gère le chargement/sauvegarde des scores et la boucle des parties.
    """
    print("================================")
    print("=== Bienvenue dans le Pendu ! ===")
    print("================================")

    # 1. Charger les scores existants
    scores = charger_scores(CHEMIN_SCORES)

    # 2. Demander le nom du joueur
    nom_joueur = input("\nEntrez votre nom : ").strip() #strip() enlève les espaces avant et après le nom
    # S'assurer que le nom n'est pas vide
    while not nom_joueur:
         nom_joueur = input("Votre nom ne peut pas être vide. Entrez votre nom : ").strip()


    # 3. Initialiser le score du joueur s'il est nouveau ou afficher son score actuel
    if nom_joueur not in scores:
        scores[nom_joueur] = 0 # Le nouveau joueur commence avec 0 points
        print(f"👋 Bienvenue, {nom_joueur} ! C'est votre première partie. Votre score est de 0 points.")
    else:
        print(f"✨ Re-bonjour, {nom_joueur} ! Votre score actuel est de {scores[nom_joueur]} points.")

    # 4. Boucle principale pour jouer plusieurs parties
    jouer_encore = True
    while jouer_encore:
        # Choisir un mot pour la nouvelle partie
        mot_a_deviner = choisir_mot(LISTE_MOTS)
        # print(f"[Debug] Mot secret : {mot_a_deviner}") # Ligne de debug, à commenter/supprimer

        # Lancer une partie. La fonction gerer_partie gère le jeu et met à jour le score si victoire
        # Elle retourne le dictionnaire de scores potentiellement modifié
        scores = gerer_partie(mot_a_deviner, NBR_CHANCES, nom_joueur, scores)

        # Afficher le score total du joueur après la fin de la partie (victoire ou défaite)
        print(f"\nScore total de {nom_joueur} : {scores[nom_joueur]} points.")

        # 5. Sauvegarder les scores après chaque partie terminée
        enregistrer_scores(scores, CHEMIN_SCORES)

        # 6. Demander si le joueur veut rejouer
        reponse = input("Voulez-vous jouer une autre partie ? (oui/non) : ").lower().strip()
        # La boucle continue si la réponse est exactement 'oui'
        jouer_encore = (reponse == 'oui')

    print("\n================================")
    print("=== Merci d'avoir joué ! À bientôt ! ===")
    print("================================")


# Point d'entrée du script
if __name__ == "__main__":
    main() # Lance la fonction principale lorsque le script est exécuté directement

