from collections import deque
from plateau import Plateau

class SolveurRushHour:
    """
    Classe pour résoudre les puzzles Rush Hour en utilisant la recherche en largeur.
    """
    def __init__(self, plateau):
        """
        Initialise le solveur avec un plateau.
            
        Exemple :
        $$$ from plateau import Plateau
        $$$ from vehicule import Vehicule
        $$$ plateau = Plateau(6) 
        $$$ vehicule_rouge = Vehicule('R', 1, 2, 2, 'H', est_rouge=True)
        $$$ plateau.ajouter_vehicule(vehicule_rouge)
        $$$ solveur = SolveurRushHour(plateau)
        $$$ solveur.plateau_initial == plateau
        True
        $$$ solveur.plateau_initial.vehicules['R'] == vehicule_rouge
        True
        """
        self.plateau_initial = plateau
        
    def resoudre(self) -> list:
        """
        Résout le puzzle Rush Hour en utilisant la recherche en largeur.
        
        Renvoie une liste des déplacements pour résoudre le puzzle, ou None si aucune solution n'existe
            
        Exemple :
        $$$ from collections import deque
        $$$ from vehicule import Vehicule
        $$$ plateau = Plateau(6)
        $$$ # Test avec un véhicule rouge qui nécessite un déplacement
        $$$ vehicule_rouge = Vehicule('R', 2, 2, 2, 'H', est_rouge=True)  # À une case de la sortie
        $$$ plateau.ajouter_vehicule(vehicule_rouge)
        $$$ solveur = SolveurRushHour(plateau)
        $$$ solution = solveur.resoudre()
        $$$ solution is None  # Une solution devrait exister
        False
        
        $$$ from vehicule import Vehicule
        $$$ plateau = Plateau(6)
        $$$ vehicule_rouge = Vehicule('R', 2, 2, 2, 'H', est_rouge=True)
        $$$ vehicule_bloquant = Vehicule('A', 4, 0, 6, 'V')  # Bloque complètement
        $$$ plateau.ajouter_vehicule(vehicule_rouge)
        $$$ plateau.ajouter_vehicule(vehicule_bloquant)
        $$$ solveur = SolveurRushHour(plateau)
        $$$ solveur.resoudre() is None
        True
        
        $$$ from vehicule import Vehicule
        $$$ plateau = Plateau(6)
        $$$ vehicule_rouge = Vehicule('R', 2, 2, 2, 'H', est_rouge=True)
        $$$ vehicule_bloquant = Vehicule('A', 4, 0, 3, 'V')
        $$$ plateau.ajouter_vehicule(vehicule_rouge)
        $$$ plateau.ajouter_vehicule(vehicule_bloquant)
        $$$ solveur = SolveurRushHour(plateau)
        $$$ solveur.resoudre() is None
        False
        """
        # Utilise une file pour stocker les états du plateau et les séquences de déplacements
        file = deque([])
        file.append((self.plateau_initial, []))  # (plateau, deplacements)
        
        # Garde une trace des états visités pour éviter les cycles
        visites = set()
        visites.add(self.plateau_initial.obtenir_hash_etat())
        
        while file:
            plateau_courant, deplacements = file.popleft()
            if plateau_courant.est_resolu():
                return deplacements
            deplacements_possibles = plateau_courant.obtenir_deplacements_possibles()
            
            for id_vehicule, direction in deplacements_possibles:
                nouveau_plateau = plateau_courant.deplacer_vehicule(id_vehicule, direction)
                hash_etat = nouveau_plateau.obtenir_hash_etat()
                # Si l'état a déjà été visité on passe a l'itération suivante
                if hash_etat not in visites:
                    # Marque le nouvel état comme visité
                    visites.add(hash_etat)
                    # Ajoute le nouvel état à la file avec sa séquence de déplacements
                    nouveaux_deplacements = deplacements + [(id_vehicule, direction)]
                    file.append((nouveau_plateau, nouveaux_deplacements))
        # Si la file est vide et qu'aucune solution n'a été trouvée
        return None
    
    def obtenir_chemin_solution(self, deplacements:list) -> str:
        """
        Renvoie une représentation sous forme de chaîne de la solution
            
        Exemple :
        $$$ from vehicule import Vehicule
        $$$ plateau = Plateau(6)
        $$$ vehicule = Vehicule('X', 2, 2, 2, 'H')
        $$$ plateau.ajouter_vehicule(vehicule)
        $$$ solveur = SolveurRushHour(plateau)
        $$$ deplacements = [('X', 'avant')]
        $$$ solution_str = solveur.obtenir_chemin_solution(deplacements)
        $$$ "Solution trouvée en 1 déplacements" in solution_str
        True
        
        $$$ from vehicule import Vehicule
        $$$ plateau = Plateau(6)
        $$$ vehicule = Vehicule('X', 2, 2, 2, 'H')
        $$$ plateau.ajouter_vehicule(vehicule)
        $$$ solveur = SolveurRushHour(plateau)
        $$$ solveur.obtenir_chemin_solution(None)
        "Aucune solution n'existe pour cette configuration."
        """
        if deplacements is None:
            return "Aucune solution n'existe pour cette configuration."
        
        solution = f"Solution trouvée en {len(deplacements)} déplacements:\n"
        
        plateau = self.plateau_initial.copier()
        solution += str(plateau) + "\n"
        
        for i, (id_vehicule, direction) in enumerate(deplacements):
            if direction == 'avant':
                direction_str = "en avant" if plateau.vehicules[id_vehicule].orientation == 'H' else "en bas"
            else:
                direction_str = "en arrière" if plateau.vehicules[id_vehicule].orientation == 'H' else "en haut"
                
            solution += f"Déplacement {i+1}: Véhicule {id_vehicule} se déplace {direction_str}\n"
            plateau = plateau.deplacer_vehicule(id_vehicule, direction)
            solution += str(plateau) + "\n"
        
        return solution