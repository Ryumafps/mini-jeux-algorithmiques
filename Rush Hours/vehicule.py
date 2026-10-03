class Vehicule:
    """
    Classe représentant un véhicule dans le Rush Hour.
    """
    def __init__(self, id:str, x:int, y:int, longueur:int, orientation:str, est_rouge=False): 
        """
        Initialise un véhicule avec sa position et son orientation.
        
        Exemple(s) :
        $$$ v = Vehicule('A', 1, 2, 2, 'H')
        $$$ v.id
        'A'
        $$$ v.x
        1
        $$$ v.y
        2
        $$$ v.longueur
        2
        $$$ v.orientation
        'H'
        $$$ v.est_rouge
        False
        $$$ r = Vehicule('R', 3, 2, 2, 'H', est_rouge=True)
        $$$ r.id
        'R'
        $$$ r.est_rouge
        True
        """
        self.id = id  #Identifiant du véhicule
        self.x = x    # Colonnes (0-5)
        self.y = y    # lignes (0-5)
        self.longueur = longueur        # Longueur du véhicule
        self.orientation = orientation  # 'H' pour Horizontal, 'V' pour Vertical 
        self.est_rouge = est_rouge      # True si c'est la voiture rouge
        
    def obtenir_coordonnees(self) -> list[tuple[int]]:
        """
        Retourne la liste des coordonnées occupées par le véhicule selon son orientation.
        
        Exemple(s) :
        $$$ vehicule = Vehicule('A', 1, 2, 2, 'H')
        $$$ vehicule.obtenir_coordonnees()
        [(1, 2), (2, 2)]
        """
        coordonnees = []
        if self.orientation == 'H':
            for i in range(self.longueur):
                coordonnees.append((self.x + i, self.y))
        else:  # Vertical
            for i in range(self.longueur):
                coordonnees.append((self.x, self.y + i))
        return coordonnees
    
    def peut_avancer(self, plateau) -> bool:
        """
        Vérifie si le véhicule peut se déplacer vers l'avant (droite pour horizontal, bas pour vertical).
        Précondition : plateau est un objet Plateau valide
        
        Exemple(s) :
        $$$ from plateau import Plateau
        $$$ plateau = Plateau(6)
        $$$ vehicule = Vehicule('A', 1, 2, 2, 'H')
        $$$ vehicule.peut_avancer(plateau)
        True
        """
        if self.orientation == 'H':
            cible_x = self.x + self.longueur
            if cible_x < plateau.taille and plateau.grille[self.y][cible_x] == 0:
                return True
        else:  # Vertical
            cible_y = self.y + self.longueur
            if cible_y < plateau.taille and plateau.grille[cible_y][self.x] == 0:
                return True
        return False
    
    def peut_reculer(self, plateau) -> bool:
        """
        Vérifie si le véhicule peut se déplacer en arrière (gauche pour horizontal, haut pour vertical).

        Exemple(s) :
        $$$ from plateau import Plateau
        $$$ plateau = Plateau(6)
        $$$ vehicule = Vehicule('A', 1, 2, 2, 'H')
        $$$ vehicule.peut_reculer(plateau)
        True
        """
        if self.orientation == 'H':
            if self.x > 0 and plateau.grille[self.y][self.x - 1] == 0:
                return True
        else:  # Vertical
            if self.y > 0 and plateau.grille[self.y - 1][self.x] == 0:
                return True
        return False
    
    def avancer(self):
        """
        Crée un nouveau véhicule avec position avancée d'une case (droite pour horizontal, bas pour vertical).
        Précondition : Le véhicule peut avancer (vérifier avec peut_avancer)
        
        Exemple(s) :
        $$$ vehicule = Vehicule('A', 1, 2, 2, 'H')
        $$$ vehicule_avance = vehicule.avancer()
        $$$ vehicule_avance.x
        2
        """
        if self.orientation == 'H':
            return Vehicule(self.id, self.x + 1, self.y, self.longueur, self.orientation, self.est_rouge)
        else:  # Vertical
            return Vehicule(self.id, self.x, self.y + 1, self.longueur, self.orientation, self.est_rouge)
    
    def reculer(self):
        """
        Crée un nouveau véhicule avec position reculée d'une case (gauche pour horizontal, haut pour vertical).
        Précondition : Le véhicule peut reculer (vérifier avec peut_reculer)
        
        Exemple(s) :
        $$$ vehicule = Vehicule('A', 1, 2, 2, 'H')
        $$$ vehicule_recule = vehicule.reculer()
        $$$ vehicule_recule.x
        0
        """
        if self.orientation == 'H':
            return Vehicule(self.id, self.x - 1, self.y, self.longueur, self.orientation, self.est_rouge)
        else:  # Vertical
            return Vehicule(self.id, self.x, self.y - 1, self.longueur, self.orientation, self.est_rouge)
    
    def __eq__(self, autre) -> bool:
        """
        Compare deux véhicules et retourne True s'ils sont identiques.
        Précondition : autre est un objet ou None
        
        Exemple(s) :
        $$$ v1 = Vehicule('A', 1, 2, 2, 'H')
        $$$ v2 = Vehicule('A', 1, 2, 2, 'H')
        $$$ v1 == v2
        True
        
        $$$ v1 = Vehicule('A', 1, 2, 2, 'H')
        $$$ v2 = Vehicule('B', 1, 2, 2, 'H')
        $$$ v1 == v2
        False
        """
        return (self.id == autre.id and self.x == autre.x and self.y == autre.y and self.longueur == autre.longueur and self.orientation == autre.orientation and self.est_rouge == autre.est_rouge)
    
    def __repr__(self) -> str:
        """
        Retourne une représentation textuelle du véhicule.

        Exemple(s) :
        $$$ v = Vehicule('A', 1, 2, 2, 'H')
        $$$ repr(v)
        "Vehicule(id=A, pos=(1,2), long=2, H)"
        """
        return f"Vehicule(id={self.id}, pos=({self.x},{self.y}), long={self.longueur}, {'H' if self.orientation == 'H' else 'V'}{', ROUGE' if self.est_rouge else ''})"