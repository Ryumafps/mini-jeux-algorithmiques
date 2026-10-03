package battleship;

public class BattleShipMain {
   
   public static void main(String[] args){
      Plateau plateau = new Plateau(8, 12, 10);
      Bateau bateau1 = new Bateau(3, new Position(2, 3), Orientation.HORIZONTAL);
      Bateau bateau2 = new Bateau(4, new Position(4, 1), Orientation.VERTICAL);
      Bateau bateau3 = new Bateau(2, new Position(0, 15), Orientation.HORIZONTAL); //(hors plateau)
      
      plateau.ajouterBateau(bateau1);
      plateau.ajouterBateau(bateau2);
      plateau.ajouterBateau(bateau3);
      
      // position des bateaux pour tester
      System.out.println("=== POSITIONS DES BATEAUX (pour test) ===");
      System.out.println("Bateau 1 (taille 3, horizontal): ligne 2, colonnes 3-5");
      System.out.println("Bateau 2 (taille 4, vertical): lignes 4-8, colonne 1");
      System.out.println("Bateau 3 (taille 2, horizontal): ligne 0, colonne 15-16 (hors plateau)");
      System.out.println("==========================================\n");
      Game game = new Game(plateau);
      game.play();
   }
}