package battleship;
import io.Input;
public class Game {
   private Plateau plateau;
   
   public Game(Plateau plateau){
      this.plateau = plateau;
   }
   
   public void play(){
      System.out.println("=== BATAILLE NAVALE ===\n");
      System.out.println("Nombre de bateaux à couler: " + plateau.getNombreBateaux() + "\n");
      
      while(!plateau.tousLesBateauxCoules()){
         System.out.println(plateau.afficherPlateau());
         
         int ligne = -1;
         int colonne = -1;
         
         // Demande la ligne
         boolean ligneOk = false;
         while (!ligneOk) {
            try {
               System.out.print("Entrez la ligne à viser: ");
               ligne = Input.readInt();
               ligneOk = true;
            } catch (java.io.IOException e) {
               System.out.println("Erreur: veuillez entrer un entier valide.");
            }
         }
         
         // Demande la colonne
         boolean colonneOk = false;
         while (!colonneOk) {
            try {
               System.out.print("Entrez la colonne à viser: ");
               colonne = Input.readInt();
               colonneOk = true;
            } catch (java.io.IOException e) {
               System.out.println("Erreur: veuillez entrer un entier valide.");
            }
         }
         
         Position pos = new Position(ligne, colonne);
         
         try {
            ResultatTir resultat = plateau.tirer(pos);
         
            if (resultat == ResultatTir.DANS_EAU) {
               System.out.println("DANS L'EAU!\n");
            } else if (resultat == ResultatTir.TOUCHE) {
               System.out.println("TOUCHÉ!\n");
            } else if (resultat == ResultatTir.COULE) {
               System.out.println("COULÉ!\n");
            }
         } catch (InvalidPositionException e){
            System.out.println("Erreur: " + e.getMessage() + "\n");
         }
      }
      
      System.out.println("\n=== VICTOIRE ===");
      System.out.println("Tous les bateaux ont été coulés!");
      System.out.println("Nombre de tirs: " + plateau.getNombreTirs());
   }
}