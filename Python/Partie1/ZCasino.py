"""TP ZCasino"""

import random
import math
import os

# Initialisation
print("Bienvenue au ZCasino !")
myMoney = 1000
print("Vous avez", myMoney, "€.")

#Prepare le tour de jeu
isEndGame = False
while myMoney > 0 and not isEndGame:

    # Demande le numéro sur lequel le joueur veut miser
    isMyNumber = False
    while not isMyNumber:
        try:
            myNumber = int(input("Sur quel numéro voulez-vous miser ? (0-49) : "))
            assert myNumber >= 0 and myNumber <= 49
            isMyNumber = True
        except ValueError:
            print("Veuillez entrer un nombre valide !")
        except AssertionError:
            print("Veuillez entrer un nombre entre 0 et 49 !")

    # Demande la mise du joueur
    isMyMise = False    
    while not isMyMise:
        try:
            myMise = int(input("Combien voulez-vous miser ? : "))
            assert myMise > 0 and myMise <= myMoney
            isMyMise = True
        except ValueError:
            print("Veuillez entrer un nombre valide !")
        except AssertionError:
            print("Veuillez entrer un nombre entre 1 et", myMoney, "!")

    # Lancement de la roulette
    myLancer = random.randrange(50)
    print("La roulette tourne... et s'arrête sur le numéro", myLancer)

    # Calcul des gains
    if myNumber == myLancer:
        myMoney += myMise * 3
        print("Félicitations ! Vous avez gagné", myMise * 3, "€ !")
    elif myNumber % 2 == myLancer % 2:
        myMoney += math.ceil(myMise / 2)    
        print("Bravo ! Vous avez gagné", math.ceil(myMise / 2), "€ !")
    else:
        myMoney -= myMise
        print("Dommage ! Vous avez perdu", myMise, "€ !")

    # Affichage du solde
    print("Vous avez maintenant", myMoney, "€.")

    # Fin du tour de jeu
    if myMoney == 0:
        print("Vous avez tout perdu ! Au revoir !") 
        isEndGame = True
    else:
        # Demande si le joueur veut continuer
        isMyContinuer = False
        while not isMyContinuer:
            try:
                myContinuer = input("Voulez-vous continuer ? (o/n) : ")
                assert myContinuer == "o" or myContinuer == "n"
                isMyContinuer = True
            except AssertionError:
                print("Veuillez entrer 'o' ou 'n' !")
        if myContinuer == "n":
            isEndGame = True

if myMoney != 0:
    print("Vous repartez avec", myMoney, "€.")
print("\n")
os.system("pause")
