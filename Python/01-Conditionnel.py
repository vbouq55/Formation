#Demande de l'annee a tester
myImputAnnee = input("\nSaisissez une année : ")
myAnnee = int(myImputAnnee)

#Test de l'année
isBissextile = (myAnnee % 4 == 0 and (myAnnee % 100 != 0 or myAnnee % 400 == 0))

#Affichage du resultat
if isBissextile:
    print("\nL'année", myAnnee, "est bissextile.")
else:
    print("\nL'année", myAnnee, "n'est pas bissextile.") 
print("\n")
