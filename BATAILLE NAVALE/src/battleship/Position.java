package battleship;

public class Position {
   private int ligne;
   private int colonne;

   /**
     * Constructeur qui crée une position avec les coordonnées spécifiées
     * @param ligne le numéro de ligne (coordonnée verticale)
     * @param colonne le numéro de colonne (coordonnée horizontale)
     */
   public Position(int ligne, int colonne) {
      this.ligne = ligne;
      this.colonne = colonne;
   }

   /**
     * Renvoie le numéro de ligne de cette position
     * @return le numéro de ligne
     */
   public int getLigne() {
      return this.ligne;
   }

   /**
     * Renvoie le numéro de colonne de cette position
     * @return le numéro de colonne
     */
   public int getColonne() {
      return this.colonne;
   }

   /**
    * Vérifie si cette position est égale à une autre position.
    * Deux positions sont égales si elles ont les mêmes coordonnées de ligne et colonne.
    * @param obj l'autre position à comparer
    * @return true si les deux positions sont égales, false sinon
    */
   public boolean equals(Position obj) {
      if(!(obj instanceof Position)){
         return false;
      }
      return this.ligne== obj.ligne && this.colonne == obj.colonne;
   }
}
