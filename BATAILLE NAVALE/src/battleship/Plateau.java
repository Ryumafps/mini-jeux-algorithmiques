package battleship;

public class Plateau {

   private int hauteur=8;
   private int largeur=12;
   private Bateau[] bateaux;
   private int nombreBateaux = 0;
   private int nombreTirs = 0;
   private EtatCase[][] grille;

   /**
     * Crée un plateau de jeu pour la bataille navale avec les dimensions et capacité spécifiées
     * @param hauteur la hauteur du plateau (nombre de lignes)
     * @param largeur la largeur du plateau (nombre de colonnes)
     * @param capaciteMax le nombre maximum de bateaux que le plateau peut contenir
     */
   public Plateau(int hauteur, int largeur, int capaciteMax) {
      this.hauteur = hauteur;
      this.largeur =largeur;
      this.bateaux = new Bateau[capaciteMax];
      this.nombreBateaux = 0;
      this.nombreTirs = 0;
      this.grille = new EtatCase[hauteur][largeur];

      for (int i=0; i<hauteur; i++){
         for (int j=0; j<largeur; j++){
            grille[i][j] = EtatCase.INCONNUE;
         }
      }
   }

   /**
     * Renvoie la hauteur du plateau
     * @return la hauteur du plateau en nombre de cases
     */
   public int getHauteur() {
      return this.hauteur;
   }

   /**
     * Renvoie la largeur du plateau
     * @return la largeur du plateau en nombre de cases
     */
   public int getLargeur() {
      return this.largeur;
   }

   /**
     * Renvoie le nombre total de tirs effectués sur le plateau
     * @return le nombre de tirs effectués
     */
   public int getNombreTirs() {
      return this.nombreTirs;
   }

   /**
     * Renvoie le nombre de bateaux actuellement placés sur le plateau
     * @return le nombre de bateaux présents
     */
   public int getNombreBateaux() {
      return this.nombreBateaux;
   }

   /**
     * Renvoie l'état d'une case à la position spécifiée
     * @param pos la position de la case à inspecter
     * @return l'état actuel de la case (INCONNUE, EAU ou BATEAU_TOUCHE)
     * @throws InvalidPositionException si la position est en dehors des limites du plateau
     */
   public EtatCase getEtatCase(Position pos) throws InvalidPositionException {
      if (pos.getLigne() < 0 || pos.getLigne() >= hauteur || 
          pos.getColonne() < 0 || pos.getColonne() >= largeur) {
         throw new InvalidPositionException("Position hors du plateau");
      }
      return grille[pos.getLigne()][pos.getColonne()];
   }

    /**
     * Vérifie si une position est valide (dans les limites du plateau)
     * @param pos la position à vérifier
     * @return true si la position est dans le plateau, false sinon
     */
   public boolean estPositionValide(Position pos) {
      return pos.getLigne() >= 0 && pos.getLigne()<hauteur && pos.getColonne() >=0 && pos.getColonne() < largeur;
   }

   /**
     * Vérifie si une position est occupée par un bateau
     * @param pos la position à vérifier
     * @return true si un bateau occupe la position, false sinon
     */
   public boolean estOccupeeParBateau(Position pos) {
      for (int i = 0; i < nombreBateaux; i++) {  // Parcourir jusqu'à nombreBateaux, pas tout le tableau
         if (bateaux[i] != null && bateaux[i].occupePosition(pos)){
            return true;
         }
      }
      return false;
   }

   /**
     * Vérifie si un bateau peut être ajouté au plateau sans chevaucher d'autres bateaux
     * et en restant dans les limites du plateau
     * @param bateau le bateau à vérifier
     * @return true si le bateau peut être placé, false sinon
     */
   public boolean peutAjouterBateau(Bateau bateau) {
      for (int i=0; i< bateau.getTaille(); i++){
         Position pos = bateau.getPositionCase(i);
         if (!estPositionValide(pos)){
            return false;
         }
         if (estOccupeeParBateau(pos)){
            return false;
         }
      }
      return true;
   }

   /**
     * Ajoute un bateau au plateau si la position est valide et sans chevauchement
     * @param bateau le bateau à ajouter
     */
   public void ajouterBateau(Bateau bateau){
      if (peutAjouterBateau(bateau)) {
         bateaux[nombreBateaux] = bateau;
         nombreBateaux++;
      }
   }

   /**
     * Effectue un tir à la position spécifiée et met à jour l'état du jeu
     * @param pos la position où tirer
     * @return le résultat du tir (DANS_EAU, TOUCHE ou COULE)
     * @throws InvalidPositionException si la position est invalide
     */
   public ResultatTir tirer(Position pos) throws InvalidPositionException {
      if (!estPositionValide(pos)){
         throw new InvalidPositionException("Position invalide: " + pos.getLigne() + "," + pos.getColonne());
      }
      nombreTirs++;
      
      // Si la case a déjà été visée, retourne DANS_EAU
      if (grille[pos.getLigne()][pos.getColonne()] != EtatCase.INCONNUE){
         return ResultatTir.DANS_EAU;
      }
      
      // Cherche si un bateau occupe cette position
      Bateau bateauTouche = null;
      for (int i = 0; i < nombreBateaux; i++) {
         if (bateaux[i] != null && bateaux[i].occupePosition(pos) && !bateaux[i].estTouche(pos)){
            bateauTouche = bateaux[i];
            break;
         }
      }
      
      if (bateauTouche == null){
         grille[pos.getLigne()][pos.getColonne()] = EtatCase.EAU;
         return ResultatTir.DANS_EAU;
      }
      
      // Touche le bateau
      bateauTouche.toucher(pos);
      grille[pos.getLigne()][pos.getColonne()] = EtatCase.BATEAU_TOUCHE;
      
      // Vérifie si le bateau est coulé
      if (bateauTouche.estCoule()){
         return ResultatTir.COULE;
      }
      
      return ResultatTir.TOUCHE;
   }

   /**
     * Affiche le plateau
     * @return une chaîne de caractères représentant le plateau
     */
   public String afficherPlateau() {
      StringBuilder sb = new StringBuilder();
      
      // Affiche les numéros de colonnes
      sb.append("   ");
      for (int j = 0; j < largeur; j++){
         if (j < 10) {
            sb.append(" " + j + " ");
         } else {
            sb.append(j + " ");
         }
      }
      sb.append("\n");
      
      // Affiche chaque ligne
      for (int i = 0; i < hauteur; i++){
         if (i < 10) {
            sb.append(" " + i + " ");
         } else {
            sb.append(i + " ");
         }
         for (int j = 0; j < largeur; j++){
            if (grille[i][j] == EtatCase.INCONNUE) {
               sb.append(" . ");
            } else if (grille[i][j] == EtatCase.EAU) {
               sb.append(" ~ ");
            } else if (grille[i][j] == EtatCase.BATEAU_TOUCHE) {
               sb.append(" * ");
            }
         }
         sb.append("\n");
      }
      return sb.toString();
   }

   /**
     * Vérifie si tous les bateaux du plateau ont été coulés
     * @return true si tous les bateaux sont coulés, false sinon
     */
   public boolean tousLesBateauxCoules(){
      for (int i = 0; i < nombreBateaux; i++){
         if (bateaux[i] != null && !bateaux[i].estCoule()){
            return false;
         }
      }
      return true;
   }
      
   
}
