# Compléter ici (noms, groupe, contenu fichier, date)
# TP Prog: Jeu du Binairo 
#
# Ne pas supprimer cette ligne. <trace>binairo.py</trace>


####################
# Jeu du Binairo
####################
from config_binairo import grille1


ZERO = '0'
UN = '1'
VIDE = ' '

def init_grille(config):
    """ initialise la grille avec des cases vides et place les valeurs dedans

    Précondition :
    Exemple(s) :
    $$$
    """
    taille, valeurs = config
    grille = [[VIDE for _ in range(taille)] for _ in range(taille)] # cree uen grillle 4x4 vide tab en comprehension
    for x, y, val in valeurs:  # pour chaque tuple dans valeurs
        grille[x][y] = val  # Place `val` à la position (x, y) dans la grille
    return grille

def afficher_grille(grille):
    """ affiche la grille 

    Précondition :
    Exemple(s) :
    $$$
    """
    taille = len(grille)
    ligne_sep = "+---" * taille + "+"
    for ligne in grille:
        print(ligne_sep)
        print("| " + " | ".join(ligne) + " |")
    print(ligne_sep)
    

def grille_remplie(grille):
    """ renvoie True si grille remplie sinon False, si c'est gagnant ou pas

    Précondition :
    Exemple(s) :
    $$$ grille_remplie([['1','1','0','0'],['0','0','1','1'],['1','0','0','1'],['0','1','1','0']])
    True
    """
    for ligne in grille:
        for case in ligne:
            if case != '0' and case != '1':
                return False 
    return True 


def est_valide(grille):
    """ verfiei si les conditions sont respecter 

    Précondition :
    Exemple(s) :
    $$$
    """
    return (regle_symboles(grille) and identique_dans_grille(grille) and nb_symbole(grille))


#-------------------------
# REGLES DE POSITIONNEMENT
#-------------------------

def regle_symboles(grille):
    """ Predicat qui verifie si il ya a + de 2 symbole identique cote a cote

    Précondition :
    Exemple(s) :
    $$$
    """
    i = 0
    colonnes = [[grille[j][i] for j in range(len(grille))] for i in range(len(grille))]
    while i < len(grille) and pas_plus_de_2_symboles_ligne(grille[i]) and pas_plus_de_2_symboles_ligne(colonnes[i]):
        i = i+1
    return i == len(grille)
                
def pas_plus_de_2_symboles_ligne(ligne: list[int]):
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ pas_plus_de_2_symboles_ligne([0,1,1,0,1,0,0,1])
    True
    $$$ pas_plus_de_2_symboles_ligne([0,0,1,1,1,0,0])
    False
    """
    i = 0
    while i < len(ligne) - 2 and (not (ligne[i] == ligne[i+1] == ligne[i+2]) or ligne[i] == VIDE):
        i = i+1
    return i == len(ligne) - 2
   
   
def identique_dans_grille(grille):
    """ Predicat qui verifie si il ya des lignes ou colonne identique dans la grille

    Précondition :
    Exemple(s) :
    $$$ identique_dans_grille([[1, 2, 3], [4, 2, 3], [1, 2, 3]])
    True
    """
    if identique_lignes(grille):
        return True
    colonnes = [[grille[j][i] for j in range(len(grille))] for i in range(len(grille))]
    if identique_lignes(colonnes):
        return True
    return False

def identique_lignes(grille):
    """ Preicat qui verifie si il ya des lignes identiques dans la grille

    Précondition :
    Exemple(s) :
    $$$ identique_lignes([[UN, UN, ZERO],[UN, UN, ZERO]])
    True
    $$$ identique_lignes([[1, 2, 3],[4, 5, 6],[1, 2, 3]])
    True
    """
    for i in range(len(grille)):
        for j in range(i + 1, len(grille)):
            if grille[i] == grille[j]:
                return True
    return False

def bon_symbole():
    """ n'autorise que des symboles 0 ou 1

    Précondition :
    Exemple(s) :
    $$$
    """
    return s == "0" or s == "1"

def nb_symbole(grille):
    """ verifie si il y a autant de 0 que de 1 dans chaques lignes/colonnes

    Précondition :
    Exemple(s) :
    $$$ nb_symbole([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]])
    True
    """
    for ligne in grille:
        if ligne.count(0) != ligne.count(1):
            return False
        
    for i in range(len(grille[0])):  
        c0 = c1 = 0
        for j in range(len(grille)):  
            if grille[j][i] == 0:
                c0 += 1
            elif grille[j][i] == 1:
                c1 += 1
        if c1 != c0:
            return False
    return True
    
    
def jouer():
    grille = init_grille(grille1) # Initialiser la grille avec la configuration donnée de grille 1
    print("Grille initiale :")
    afficher_grille(grille)
    
    while not grille_remplie(grille):
        a = input("Choisie entre 0 et 1: ") # val
        b = int(input("En quel position abcisse voulez vous choisir: ")) # x -
        c = int(input("En quel position ordonner voulez vous choisir: ")) # y |
        grille[c][b] = a
        print("Grille en cours")
        afficher_grille(grille)
        
    # conditions de victoire 
    print("VOUS AVEZ GAGNER !!!!!!")
    
if __name__ == "__main__":
    jouer()
