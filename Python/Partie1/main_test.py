"""Permet de tester les fonctions de base de Python"""

import os
from  Python.Partie1.multiplcation import *

# # test de la fonction table
# table(3, 20)
# os.system("pause")

prenom = "Paul"
nom = "Dupont"
age = 21
print( "Je m'appelle {0} {1} ({3} {0} pour l'administration) et j'ai {2} ans.".format(prenom, nom, age, nom.upper()))

# formatage d'une adresse
adresse = """ 
{no_rue}, {nom_rue}
{code_postal} {nom_ville} ({pays})
""".format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")
print(adresse)
 
os.system("pause")
