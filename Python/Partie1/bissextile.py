#Demande de l'annee a tester
isSaisieMyAnnee = False
while not isSaisieMyAnnee:
    myImputAnnee = input("\nSaisissez une année : ")
    try:
        myAnnee = int(myImputAnnee)
        assert myAnnee > 0
        isSaisieMyAnnee = True
    except ValueError:
        print("\nVous n'avez pas saisi une année correcte.")
    except AssertionError:
        print("\nL'année saisie est inférieure ou égale à 0")

#Test de l'année
isBissextile = (myAnnee % 4 == 0 and (myAnnee % 100 != 0 or myAnnee % 400 == 0))

#Affichage du resultat
if isBissextile:
    print("\nL'année", myAnnee, "est bissextile.")
else:
    print("\nL'année", myAnnee, "n'est pas bissextile.") 
print("\n")
