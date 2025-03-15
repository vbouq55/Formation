import math

def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb de 1*nb à max*nb"""

    i = 0
    while i < max: # Tant que i est strictement inférieure à 10,
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1 # On incrémente i de 1 à chaque tour de boucle.

table(5)