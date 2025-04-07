import os
import pickle

def set_tmp_dir():
    os.chdir("C:/ProjPerso/TmpDir/")

def write_file():
    set_tmp_dir()
    # Ecrire dans un fichier
    myFile = open("test.txt", "w")
    myFile.write("Hello World")
    myFile.close()

def read_file():
    set_tmp_dir()
    # Lire un fichier
    myFile = open("test.txt", "r")
    content = myFile.read()
    myFile.close()
    print(content)

def read_file_with():
    set_tmp_dir()
    # Lire un fichier avec le mot clé with
    with open("test.txt", "r") as myFile:
        content = myFile.read()
        print(content)
        print("Dans le with, myFile.closed = ", myFile.closed)  
    # Le fichier est automatiquement fermé à la fin du bloc with
    print("Hors du with, myFile.closed = ", myFile.closed)  

def write_with_Pickle():
    set_tmp_dir()
    # Préparation Objet à écrire
    score = {"joueur 1": 5, "joueur 2": 35, "joueur 3": 20, "joueur 4": 2 }
    with open('donnees', 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(score)
    # Fin
    print("Ecriture terminée")

def read_with_Pickle():
    set_tmp_dir()
    # Lecture d'un fichier avec pickle
    with open('donnees', 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        score = mon_depickler.load()
    print(score)    

write_with_Pickle()
read_with_Pickle()
