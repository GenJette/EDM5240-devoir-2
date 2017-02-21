#coding: utf-8 

import csv
    
fichier = "concordia1.csv"
f1 = open(fichier)
    
lignes = csv.reader(f1)
next(lignes)

# Premières lignes vues au cours 2 de Python

for ligne in lignes:
    # J'ai recours à la boucle (loop) parce que je devrai aller chercher une référence (ligne) dans un fichier complet (lignes)...
    # ...afin de l'appliquer à chaque définition de variable. (Cours 2 Python)
    
    titre = (ligne[2])
    # Va chercher ce qui se trouve à la ligne 2 (Cours 1 Python)
    
    longTitre = (len(ligne[2]))
    # "len" = compte le nombre de caractères - (Cours 1 Python)
    
    nomComplet = (ligne[1] +" "+ ligne[0])
    # J'ai mis le [1] avant [0] ainsi qu'un espace entre les deux pour donner "Prénom" (colonne 1) 
    #...[espace] "Nom de famille" (colonne 0) - (Cours 1 Python)
    
    nbPages = (ligne[5])
    if "M." in ligne[6]: 
        sorte = "Le mémoire"
    elif "Ph." in ligne[6]:
        sorte = "La thèse"
    # Étant donné que je ne pouvais trouver "mémoire" et "thèse" avec la boucle...
    #...j'ai eu recours au if, elif et in pour que la variable « soit encore plus variable », selon un nouveau critère.
    # (Cours 2 Python)
    
    print("{} de {} compte {} pages. Son titre est « {} », qui comprend {} de caratères.".format(sorte, nomComplet, nbPages, titre, longTitre))
    # Pour faire la phrases complète (même si elle n'est pas tout à fait complète)...
    # ...j'ai reproduit ce qu'on avait vu au premier cours de python avec la phrase des années olympiques. 
    # (Cours 1 Python)

# Bon. Le nombre de pages n'est pas complet lorsque je print ma phrase. J'ai pensé faire un dictionnaire pour définir...
#...chaque chiffre romain par un vrai chiffre, qui serait additionné au reste des pages. (Cours 2 Python)
d = {
    "i" : "1",
    "ii" : "2",
    "iii": "3",
    "iv" : "4",
    "v" : "5",
    "vi" : "6",
    "vii" : "7",
    "viii" : "8",
    "ix" : "9",
    "x" : "10",
    "xi" : "11",
    "xii" : "12",
    "xiii" : "13",
    "xiv" : "14",
    "xv" : "15",
    "xvi" : "16",
    "xvii" : "17",
    "xviii" : "18",
    "xix" : "19",
    "xx" : "20",
    "xxi" : "21",
    "xxii" : "22",
    "xxiii" : "23",
    "xxiv" : "24",
    "xxv" : "25",
    "xxvi" : "26",
    "xxvii" : "27",
    "xxviii" : "28",
    "xxix" : "29",
    "xxx" : "30",
    }

# Ne sachant pas si c'était le chemin le plus rapide, je n'ai pas été en mesure de trouver d'autres formules pour continuer.
