from vehicule import Vehicule

class Plateau:
    """
    Classe représentant le plateau de jeu Rush Hour.
    """

    def __init__(self, taille=6):
        """
        Initialise un plateau vide.
            
        $$$ p = Plateau()
        $$$ p.taille
        6
        $$$ p.vehicules
        {}
        $$$ p.position_sortie
        (5, 2)

        $$$ p2 = Plateau(4)
        $$$ p2.taille
        4
        $$$ p2.position_sortie
        (3, 2)
        """
        self.taille = taille
        self.grille = [[0 for _ in range(taille)] for _ in range(taille)]
        self.vehicules = {}
        self.position_sortie = (taille - 1, 2)  # La position de sortie du plateau
    
    def ajouter_vehicule(self, vehicule) -> bool:
        """
        Ajoute un véhicule au plateau si ses coordonnées sont valides et non occupées.
        
        Exemple(s) :
        $$$ plateau = Plateau()
        $$$ vehicule = Vehicule('A', 1, 2, 2, 'H')
        $$$ plateau.ajouter_vehicule(vehicule)
        True
        $$$ plateau.grille[2][1] == 'A'
        True
        $$$ plateau.grille[2][2] == 'A'
        True
        """
        # Vérifie si le véhicule est dans les limites du plateau
        for x, y in vehicule.obtenir_coordonnees():
            if not (0 <= x < self.taille and 0 <= y < self.taille):
                return False
            
            # Vérifie si la position est déjà occupée
            if self.grille[y][x] != 0:
                return False
        
        # Si le véhicule est la voiture rouge, on vérifie qu'elle se trouve sur la ligne 2
        if vehicule.est_rouge and vehicule.y != 2:
            return False
        
        # Ajoute le véhicule au plateau
        self.vehicules[vehicule.id] = vehicule
        for x, y in vehicule.obtenir_coordonnees():
            self.grille[y][x] = vehicule.id
        
        return True
    
    def supprimer_vehicule(self, id_vehicule:str):
        """
        Supprime un véhicule du plateau en libérant ses coordonnées.
        Précondition : id_vehicule est une chaîne correspondant à un véhicule existant
        
        Exemple(s) :
        $$$ plateau = Plateau()
        $$$ vehicule = Vehicule('A', 1, 2, 2, 'H')
        $$$ plateau.ajouter_vehicule(vehicule)
        $$$ plateau.supprimer_vehicule('A')
        $$$ 'A' in plateau.vehicules
        False
        $$$ plateau.grille[2][1] == 0
        True
        $$$ plateau.grille[2][2]
        0
        """
        if id_vehicule in self.vehicules:
            vehicule = self.vehicules[id_vehicule]
            for x, y in vehicule.obtenir_coordonnees():
                self.grille[y][x] = 0
            del self.vehicules[id_vehicule]
    
    def deplacer_vehicule(self, id_vehicule:str, direction:str):
        """
        Déplace un véhicule dans la direction spécifiée.
        Renvoie un nouveau plateau avec le véhicule déplacé, ou None si le déplacement est invalide
            
        Exemple(s) :
        $$$ plateau = Plateau()
        $$$ plateau.ajouter_vehicule(Vehicule('A', 1, 2, 2, 'H'))
        $$$ nouveau_plateau = plateau.deplacer_vehicule('A', 'avant')
        $$$ nouveau_plateau.vehicules['A'].x
        2
        """
        if id_vehicule not in self.vehicules:
            return None
        
        vehicule = self.vehicules[id_vehicule]
        
        # Vérifie si le déplacement est valide
        if (direction == 'avant' and not vehicule.peut_avancer(self)) or (direction == 'arriere' and not vehicule.peut_reculer(self)):
            return None
        
        # Crée un nouveau plateau pour le nouvel état
        nouveau_plateau = self.copier()
        
        # Supprime l'ancien véhicule
        nouveau_plateau.supprimer_vehicule(id_vehicule)
        
        # Ajoute le véhicule déplacé
        if direction == 'avant':
            nouveau_vehicule = vehicule.avancer()
        else:  # arrière
            nouveau_vehicule = vehicule.reculer()
            
        nouveau_plateau.ajouter_vehicule(nouveau_vehicule)
        
        return nouveau_plateau
    
    def obtenir_deplacements_possibles(self) -> list[tuple["id_vehicule", "direction"]]:
        """
        Obtient tous les déplacements possibles à partir de l'état actuel du plateau.
            
        Exemple(s) :
        $$$ plateau = Plateau()
        $$$ plateau.ajouter_vehicule(Vehicule('A', 1, 2, 2, 'H'))
        $$$ plateau.ajouter_vehicule(Vehicule('B', 0, 0, 2, 'V'))
        $$$ deplacements = plateau.obtenir_deplacements_possibles()
        $$$ ('A', 'avant') in deplacements and ('A', 'arriere') in deplacements
        True
        $$$ ('B', 'haut') in deplacements and ('A', 'bas') in deplacements
        False
        """
        deplacements = []
        for id_vehicule, vehicule in self.vehicules.items():
            if vehicule.peut_avancer(self):
                deplacements.append((id_vehicule, 'avant'))
            if vehicule.peut_reculer(self):
                deplacements.append((id_vehicule, 'arriere'))
        return deplacements
    
    def est_resolu(self) -> bool:
        """
        Vérifie si le puzzle est résolu (la voiture rouge peut sortir).

        Exemple(s) :
        $$$ plateau = Plateau()
        $$$ voiture_rouge = Vehicule('R', 4, 2, 2, 'H', est_rouge=True)
        $$$ plateau.ajouter_vehicule(voiture_rouge)
        $$$ plateau.est_resolu()
        True
        """
        for id_vehicule, vehicule in self.vehicules.items():
            if vehicule.est_rouge:
                # La voiture est à la sortie si la case à droite est libre jusqu'au bord
                if vehicule.orientation == 'H':
                    # Vérifier si le chemin est libre jusqu'à la sortie
                    chemin_sortie_libre = True
                    for x in range(vehicule.x + vehicule.longueur, self.taille):
                        if self.grille[vehicule.y][x] != 0:
                            chemin_sortie_libre = False
                    return chemin_sortie_libre
        return False
    
    def copier(self):
        """
        Crée une copie du plateau.
        
        Renvoie un nouveau plateau avec la même configuration
            
        Exemple(s) :
        $$$ plateau = Plateau()
        $$$ plateau.ajouter_vehicule(Vehicule('A', 1, 2, 2, 'H'))
        
        $$$ plateau.ajouter_vehicule(Vehicule('R', 4, 2, 2, 'H', est_rouge=True))
        
        $$$ copie = plateau.copier()
        $$$ copie.vehicules['A'].x == plateau.vehicules['A'].x
        True
        $$$ copie.vehicules['R'].x == plateau.vehicules['R'].x
        True
        $$$ copie is not plateau
        True
        """
        nouveau_plateau = Plateau(self.taille)
        for id_vehicule, vehicule in self.vehicules.items():
            nouveau_vehicule = Vehicule(vehicule.id, vehicule.x, vehicule.y, vehicule.longueur, vehicule.orientation, vehicule.est_rouge)
            nouveau_plateau.ajouter_vehicule(nouveau_vehicule)
        return nouveau_plateau
    
    def obtenir_hash_etat(self) -> tuple[str]:
        """
        Renvoie un tuple représentant l'état actuel du plateau avec la postition de toutes les voitures
        Pour vérifier si un état a déjà été visité.

            
        Exemple(s) :
        $$$ plateau1 = Plateau()
        $$$ plateau1.ajouter_vehicule(Vehicule('A', 1, 2, 2, 'H'))
        $$$ hash1 = plateau1.obtenir_hash_etat()
        $$$ plateau2 = plateau1.copier()
        $$$ hash2 = plateau2.obtenir_hash_etat()
        $$$ hash1 == hash2
        True
        """
        etat = []
        for id_vehicule, vehicule in sorted(self.vehicules.items()):
            etat.append((id_vehicule, vehicule.x, vehicule.y))
        return tuple(etat)
    
    def __str__(self):
        """
        Représentation sous forme de chaîne du plateau.
        
        Exemple(s) :
        $$$ plateau = Plateau(3)
        $$$ plateau.ajouter_vehicule(Vehicule('A', 0, 0, 2, 'H'))
        $$$ str(plateau)
        'AA.\\n...\\n...\\n'
        """
        resultat = ""
        for y in range(self.taille):
            for x in range(self.taille):
                cellule = self.grille[y][x]
                if cellule == 0:
                    resultat += "."
                else:
                    for id_vehicule, vehicule in self.vehicules.items():
                        if id_vehicule == cellule:
                            resultat += cellule
            resultat += "\n"
        return resultat