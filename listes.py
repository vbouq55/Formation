inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
    ]

# Trier l'inventaire par la valeur numérique en ordre décroissant
inventaire_trie = sorted(inventaire, key=lambda x: x[1], reverse=False)

print(inventaire_trie)