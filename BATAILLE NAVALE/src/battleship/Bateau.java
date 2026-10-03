package battleship;
/**
 * Représente un bateau dans un jeu de bataille navale.
 * Un bateau est caractérisé par sa taille, sa position d'origine, son orientation
 * et l'état de ses cases (touchées ou non).
 */
public class Bateau{
   private int taille;
   private Position positionOrigine;
   private Orientation orientation;
   private boolean[] casesTouchees; //true si une case est touche

   /**
     * Construit un nouveau bateau avec les caractéristiques spécifiées.
     * @param taille           La taille du bateau (nombre de cases)
     * @param positionOrigine  La position de la première case du bateau
     * @param orientation      L'orientation du bateau (HORIZONTAL ou VERTICAL)
     */
   public Bateau(int taille, Position positionOrigine, Orientation orientation) {
      this.taille = taille;
      this.positionOrigine = positionOrigine;
      this.orientation = orientation;
      this.casesTouchees = new boolean[taille];
   }

   /**
     * Retourne la taille du bateau.
     * @return Le nombre de cases que occupe le bateau
     */
   public int getTaille() {
      return this.taille;
   }

     /**
     * Retourne la position d'origine du bateau.
     * @return La position de la première case du bateau
     */
   public Position getPositionOrigine() {
      return this.positionOrigine;
   }

   /**
     * Retourne l'orientation du bateau.
     * @return L'orientation actuelle du bateau (HORIZONTAL ou VERTICAL)
     */
   public Orientation getOrientation(){
      return this.orientation;
   }

   /**
     * Calcule la position d'une case spécifique du bateau.
     * @param indice L'indice de la case dans le bateau (0 pour la première case)
     * @return La position de la case correspondante sur la grille
     */
   public Position getPositionCase(int indice) {
      if (orientation == Orientation.HORIZONTAL) {
         return new Position(positionOrigine.getLigne(), positionOrigine.getColonne() + indice);
      } else {
         return new Position(positionOrigine.getLigne() + indice, positionOrigine.getColonne());
      }
   }

    /**
     * Vérifie si le bateau occupe une position donnée sur la grille.
     * @param pos La position à vérifier
     * @return true si le bateau occupe la position, false sinon
     */
   public boolean occupePosition(Position pos) {
      for (int i=0; i<taille; i++){
         if (getPositionCase(i).equals(pos)){
            return true;
         }
      }
      return false;
   }
   

   /**
     * Marque une case du bateau comme touchée lorsqu'elle est atteinte.
     * @param pos La position touchée
     * @return L'indice de la case touchée dans le bateau, ou -1 si la position ne correspond à aucune case du bateau
     */
   public int toucher(Position pos) {
      for(int i=0; i<taille; i++){
         if (getPositionCase(i).equals(pos)){
            casesTouchees[i] = true;
            return i;
         }
      }
      return -1;
   }
   

   /**
     * Vérifie si le bateau est complètement coulé (toutes ses cases sont touchées).
     * @return true si toutes les cases sont touchées, false sinon
     */
   public boolean estCoule(){
      for (int i = 0; i < casesTouchees.length; i++) {
         boolean touche = casesTouchees[i];
         if(!touche){
               return false;
            }
      }
      return true;
   }

   /**
     * Vérifie si une position spécifique du bateau a déjà été touchée.
     * @param pos La position à vérifier
     * @return true si la case à cette position est déjà touchée, false sinon
     */
   public boolean estTouche(Position pos){
      for (int i = 0; i < taille; i++) {
         if (getPositionCase(i).equals(pos)){
               return casesTouchees[i];
            }
      }
      return false;
   }
}
