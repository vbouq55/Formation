import pickle # Module pour sauvegarder et charger des objets Python (comme notre dictionnaire de scores)
import os     # Module pour interagir avec le système d'exploitation, notamment vérifier l'existence d'un fichier
import random # Module pour choisir un mot aléatoirement

# On importe les variables de données depuis notre fichier donnees.py
from donnees import LISTE_MOTS, NBR_CHANCES, CHEMIN_SCORES

def charger_scores(chemin_fichier):
    """
    Charge les scores depuis le fichier spécifié.
    Retourne un dictionnaire des scores ou un dictionnaire vide si le fichier n'existe pas
    ou ne peut pas être lu.
    """
    if os.path.exists(chemin_fichier):
        # Le fichier existe, on essaie de le lire
        with open(chemin_fichier, 'rb') as f: # 'rb' pour read binary, car pickle travaille en binaire
            try:
                scores = pickle.load(f)
                print("Scores chargés avec succès.")
            except (pickle.UnpicklingError, EOFError):
                # Si le fichier est vide ou corrompu, on recommence avec un dictionnaire vide
                scores = {}
                print("Attention : Fichier de scores corrompu ou vide. Création d'un nouveau fichier.")
            except Exception as e:
                # Gérer d'autres erreurs potentielles lors de la lecture
                scores = {}
                print(f"Erreur lors du chargement des scores : {e}. Création d'un nouveau fichier.")
    else:
        # Le fichier n'existe pas encore
        scores = {}
        print(f"Fichier de scores '{chemin_fichier}' non trouvé. Création d'un nouveau.")
    return scores

def enregistrer_scores(scores_dict, chemin_fichier):
    """
    Enregistre le dictionnaire de scores dans le fichier spécifié.
    """
    try:
        with open(chemin_fichier, 'wb') as f: # 'wb' pour write binary
            pickle.dump(scores_dict, f)
        print("Scores enregistrés avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement des scores : {e}")


def choisir_mot(liste_mots):
    """
    Choisit un mot aléatoire dans la liste fournie.
    """
    return random.choice(liste_mots)

def afficher_mot_cache(mot_secret, lettres_trouvees):
    """
    Construit et retourne la chaîne à afficher avec les lettres trouvées
    et des étoiles (*) pour les lettres non trouvées.
    """
    affichage = ""
    for lettre in mot_secret:
        if lettre in lettres_trouvees:
            affichage += lettre
        else:
            affichage += "*"
    return affichage

def saisir_lettre(lettres_deja_saisies):
    """
    Demande au joueur de saisir une lettre et valide l'entrée.
    L'entrée doit être une seule lettre de l'alphabet, non déjà saisie.
    """
    while True: # Boucle tant que l'entrée n'est pas valide
        lettre = input("Saisissez une lettre : ").lower().strip() # Lire l'entrée, la mettre en minuscule et enlever les espaces

        if len(lettre) != 1:
            print("❌ Veuillez saisir *une seule* lettre.")
        elif not lettre.isalpha():
            print("❌ Veuillez saisir une lettre de l'alphabet.")
        elif lettre in lettres_deja_saisies:
            print(f"✋ Vous avez déjà saisi la lettre '{lettre}'. Essayez une autre.")
        else:
            # L'entrée est valide et n'a pas été saisie auparavant
            return lettre # On sort de la boucle en retournant la lettre valide


def gerer_partie(mot_secret, nbr_chances_initiales, nom_joueur, scores):
    """
    Gère le déroulement complet d'une partie de jeu du pendu pour un joueur donné.
    Met à jour le dictionnaire de scores en cas de victoire.
    Retourne le dictionnaire de scores potentiellement mis à jour.
    """
    lettres_trouvees = set() # Ensemble des lettres du mot secret qui ont été trouvées
    lettres_saisies_total = set() # Ensemble de *toutes* les lettres que le joueur a saisies (pour éviter de les redemander)
    chances_restantes = nbr_chances_initiales

    print(f"\n--- Nouvelle partie pour {nom_joueur} ---")
    print(f"Mot à trouver : {afficher_mot_cache(mot_secret, lettres_trouvees)}")

    # Boucle principale du jeu pour une partie
    while chances_restantes > 0:
        print(f"\nChances restantes : {chances_restantes}")
        print(f"Lettres déjà essayées : {' '.join(sorted(list(lettres_saisies_total)))}") # Afficher les lettres déjà essayées

        # Demander une lettre valide au joueur
        lettre_saisie = saisir_lettre(lettres_saisies_total)
        lettres_saisies_total.add(lettre_saisie) # Ajouter la lettre à l'ensemble des lettres déjà saisies

        if lettre_saisie in mot_secret:
            print(f"✅ Bravo ! La lettre '{lettre_saisie}' est dans le mot.")
            lettres_trouvees.add(lettre_saisie) # Ajouter la lettre à l'ensemble des lettres trouvées

            mot_actuel_affiche = afficher_mot_cache(mot_secret, lettres_trouvees)
            print(f"Mot actuel : {mot_actuel_affiche}")

            # Vérifier si toutes les lettres du mot ont été trouvées
            mot_trouve_completement = all(lettre in lettres_trouvees for lettre in mot_secret)

            if mot_trouve_completement:
                print("\n🎉 Félicitations ! Vous avez trouvé le mot :", mot_secret)
                score_gagne = chances_restantes # Le score est le nombre de chances restantes
                print(f"Vous gagnez {score_gagne} points.")
                # Mettre à jour le score du joueur
                # On s'assure que le joueur existe, même si pendu.py le fait déjà, c'est plus sûr ici
                if nom_joueur not in scores:
                     scores[nom_joueur] = 0
                scores[nom_joueur] += score_gagne
                return scores # La partie est gagnée, on retourne les scores mis à jour

        else:
            print(f"❌ Dommage ! La lettre '{lettre_saisie}' n'est pas dans le mot.")
            chances_restantes -= 1 # Une chance perdue
            print(f"Mot actuel : {afficher_mot_cache(mot_secret, lettres_trouvees)}")

    # Si on sort de la boucle while, c'est que chances_restantes est arrivé à 0
    print("\n😥 Oh non ! Vous n'avez plus de chances.")
    print("Vous avez perdu. Le mot était :", mot_secret)
    # Pas de points gagnés, on retourne les scores sans modification pour cette partie
    return scores
