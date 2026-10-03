from vehicule import Vehicule
from plateau import Plateau
from solveur import SolveurRushHour
import sys

def debutant1():
    """
    Retourne le plateau avec la configuration du niveau debutant 1
    """
    plateau = Plateau()
    
    # Ajouter la voiture rouge (position-x, position-y, longueur de 2 unités, horizontale)
    voiture_rouge = Vehicule('R', 1, 2, 2, 'H', est_rouge=True)
    plateau.ajouter_vehicule(voiture_rouge)
    
    # Ajouter les autres véhicules
    plateau.ajouter_vehicule(Vehicule('A', 0, 0, 2, 'H'))  # Voiture verte horizontale en haut à gauche
    plateau.ajouter_vehicule(Vehicule('I', 5, 0, 3, 'V'))  # Camion jaune vertical en haut à droite
    plateau.ajouter_vehicule(Vehicule('P', 0, 1, 3, 'V'))  # Camion violet vertical à gauche
    plateau.ajouter_vehicule(Vehicule('E', 3, 1, 3, 'V'))  # Camion bleu vertical au centre
    plateau.ajouter_vehicule(Vehicule('B', 0, 4, 2, 'V'))  # Voiture orange verticale en bas à gauche
    plateau.ajouter_vehicule(Vehicule('C', 4, 4, 2, 'H'))  # Voiture bleu clair horizontale en bas à droite
    plateau.ajouter_vehicule(Vehicule('X', 2, 5, 3, 'H'))  # Camion vert horizontal en bas
    return plateau

def debutant2():
    """
    Retourne le plateau avec la configuration du niveau debutant 2
    """
    plateau = Plateau()
    # Ajouter la voiture rouge (position-x, position-y, longueur de 2 unités, horizontale)
    voiture_rouge = Vehicule('R', 0, 2, 2, 'H', est_rouge=True)
    plateau.ajouter_vehicule(voiture_rouge)
    
    # Ajouter les autres véhicules
    plateau.ajouter_vehicule(Vehicule('A', 0, 0, 2, 'V'))  # Voiture verte verticale en haut à gauche
    plateau.ajouter_vehicule(Vehicule('I', 3, 0, 3, 'H'))  # Camion jaune horizontal en haut à droite
    plateau.ajouter_vehicule(Vehicule('B', 3, 1, 2, 'V'))  # Voiture orange verticale au centre
    plateau.ajouter_vehicule(Vehicule('P', 5, 1, 3, 'V'))  # Camion rose verticale à droite
    plateau.ajouter_vehicule(Vehicule('Q', 0, 3, 3, 'H'))  # Camion bleu horizontal à gauche
    plateau.ajouter_vehicule(Vehicule('C', 4, 2, 2, 'V'))  # Voiture bleu clair verticale
    plateau.ajouter_vehicule(Vehicule('D', 2, 4, 2, 'V'))  # Voiture rose verticale en bas
    plateau.ajouter_vehicule(Vehicule('F', 0, 5, 2, 'H'))  # Voiture vert foncé horizontale en bas à gauche
    plateau.ajouter_vehicule(Vehicule('E', 4, 4, 2, 'H'))  # voiture violet foncé horizontal en bas à droite
    plateau.ajouter_vehicule(Vehicule('G', 3, 5, 2, 'H'))  # Voiture noire horizontale en bas
    return plateau

def expert1():
    """
    Retourne le plateau avec la configuration du niveau expert 1
    """
    plateau = Plateau()
    # Ajouter la voiture rouge (position-x, position-y, longueur de 2 unités, horizontale)
    voiture_rouge = Vehicule('R', 0, 2, 2, 'H', est_rouge=True)
    plateau.ajouter_vehicule(voiture_rouge)
    
    # Ajouter les autres véhicules
    plateau.ajouter_vehicule(Vehicule('A', 0, 0, 2, 'V'))  # Voiture verte verticale en haut à gauche
    plateau.ajouter_vehicule(Vehicule('O', 3, 0, 3, 'H'))  # Camion jaune horizontal en haut à droite
    plateau.ajouter_vehicule(Vehicule('B', 1, 1, 2, 'H'))  # Voiture orange horizontale en haut à gauche
    plateau.ajouter_vehicule(Vehicule('C', 3, 1, 2, 'V'))  # Voiture bleu clair verticale au centre
    plateau.ajouter_vehicule(Vehicule('E', 3, 3, 2, 'H'))  # Voiture violette horizontale au centre 
    plateau.ajouter_vehicule(Vehicule('Q', 3, 5, 3, 'H'))  # Camion bleu foncé horizontal en bas à gauche
    plateau.ajouter_vehicule(Vehicule('D', 2, 2, 2, 'V'))  # Voiture rose verticale au centre
    plateau.ajouter_vehicule(Vehicule('F', 2, 4, 2, 'V'))  # Voiture vert foncé verticale en bas au milieu
    plateau.ajouter_vehicule(Vehicule('G', 3, 4, 2, 'H'))  # Voiture noire horizontale
    plateau.ajouter_vehicule(Vehicule('X', 5, 2, 3, 'V'))  # Camion vert clair verticale à droite
    return plateau

def expert2():
    """
    Retourne le plateau avec la configuration du niveau expert 2
    """
    plateau = Plateau()
    # Ajouter la voiture rouge (position-x, position-y, longueur de 2 unités, horizontale)
    voiture_rouge = Vehicule('R', 0, 2, 2, 'H', est_rouge=True)
    plateau.ajouter_vehicule(voiture_rouge)
    
    # Ajouter les autres véhicules
    plateau.ajouter_vehicule(Vehicule('A', 2, 0, 2, 'V'))  # Voiture verte verticale en haut au milieu
    plateau.ajouter_vehicule(Vehicule('O', 3, 0, 3, 'H'))  # Camion jaune horizontal en haut à droite
    plateau.ajouter_vehicule(Vehicule('B', 3, 1, 2, 'V'))  # Voiture orange verticale au milieu
    plateau.ajouter_vehicule(Vehicule('C', 2, 2, 2, 'V'))  # Voiture bleu clair verticale au milieu
    plateau.ajouter_vehicule(Vehicule('E', 3, 3, 2, 'H'))  # Voiture violette horizontale au centre
    plateau.ajouter_vehicule(Vehicule('D', 0, 3, 2, 'H'))  # Voiture rose horizontale à gauche
    plateau.ajouter_vehicule(Vehicule('F', 0, 4, 2, 'V'))  # Voiture vert foncé verticale en bas à gauche
    plateau.ajouter_vehicule(Vehicule('G', 1, 4, 2, 'V'))  # Voiture noire verticale en bas à gauche
    plateau.ajouter_vehicule(Vehicule('X', 5, 2, 3, 'V'))  # Camion vert clair verticale à droite
    plateau.ajouter_vehicule(Vehicule('H', 2, 4, 2, 'H'))  # Voiture blanche horizontale en bas
    plateau.ajouter_vehicule(Vehicule('I', 2, 5, 2, 'H'))  # Voiture jaune horizontale en bas
    return plateau

def expert3():
    """
    Retourne le plateau avec la configuration du niveau expert 3
    """
    plateau = Plateau()
    # Ajouter la voiture rouge (position-x, position-y, longueur de 2 unités, horizontale)
    voiture_rouge = Vehicule('R', 3, 2, 2, 'H', est_rouge=True)
    plateau.ajouter_vehicule(voiture_rouge)
    
    # Ajouter les autres véhicules
    plateau.ajouter_vehicule(Vehicule('A', 1, 0, 2, 'H'))  # Voiture verte horizontal en haut
    plateau.ajouter_vehicule(Vehicule('O', 0, 0, 3, 'V'))  # Camion jaune vertical en haut à droite
    plateau.ajouter_vehicule(Vehicule('B', 4, 0, 2, 'V'))  # Voiture orange verticale en haut
    plateau.ajouter_vehicule(Vehicule('V', 1, 1, 2, 'V'))  # Voiture bleu clair verticale à gauche
    plateau.ajouter_vehicule(Vehicule('E', 3, 3, 2, 'V'))  # Voiture violette verticale au centre
    plateau.ajouter_vehicule(Vehicule('D', 2, 1, 2, 'V'))  # Voiture rose verticale au centre
    plateau.ajouter_vehicule(Vehicule('F', 2, 4, 2, 'V'))  # Voiture vert foncé verticale en bas
    plateau.ajouter_vehicule(Vehicule('G', 4, 4, 2, 'H'))  # Voiture noire horizontale en bas à droite
    plateau.ajouter_vehicule(Vehicule('H', 0, 5, 2, 'H'))  # Voiture blanche horizontale en bas à gauche
    plateau.ajouter_vehicule(Vehicule('I', 3, 5, 2, 'H'))  # Voiture jaune horizontale en bas
    plateau.ajouter_vehicule(Vehicule('Q', 0, 3, 3, 'H'))  # Camion bleu foncé horizontal sur le côté gauche
    plateau.ajouter_vehicule(Vehicule('P', 5, 1, 3, 'V'))  # Camion rose verticale à droite
    return plateau

def main():
    print("Rush Hour")
    print("----------------")
    print("1. Utiliser la configuration de la carte débutant n°1")
    print("2. Utiliser la configuration de la carte débutant n°2")
    print("3. Utiliser la configuration de la carte expert n°1")
    print("4. Utiliser la configuration de la carte expert n°2")
    print("5. Utiliser la configuration de la carte expert n°3")
    
    choix = input("Sélectionnez une option (1-5): ").strip()
    
    if choix == '1':
        plateau = debutant1()
    elif choix == '2':
        plateau = debutant2()
    elif choix == '3':
        plateau = expert1()
    elif choix == '4':
        plateau = expert2()
    elif choix == '5':
        plateau = expert3()
    else:
        print("\nVeuillez choisir un nombre entre 1 et 5.")
        sys.exit()

        
    print("\nModèle choisi :\n")
    print(plateau)
    print("\nRésolution du plateau en cours...\n")
    
    solveur = SolveurRushHour(plateau)
    solution = solveur.resoudre()
    
    print(solveur.obtenir_chemin_solution(solution))

if __name__ == "__main__":
    main()