package battleship;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class PlateauTest {

   @Test
   public void testCreationPlateauAvecDimensionsCorrectes() {
      Plateau plateau = new Plateau(8, 12, 5);
      
      assertEquals(8, plateau.getHauteur(), "La hauteur devrait être 8");
      assertEquals(12, plateau.getLargeur(), "La largeur devrait être 12");
      assertEquals(0, plateau.getNombreBateaux(), "Devrait avoir 0 bateau au départ");
      assertEquals(0, plateau.getNombreTirs(), "Devrait avoir 0 tir au départ");
   }

   @Test
   public void testEstPositionValideRetourneTruePourPositionDansLimites() {
      Plateau plateau = new Plateau(5, 5, 5);
      
      assertTrue(plateau.estPositionValide(new Position(0, 0)), "Position (0,0) devrait être valide");
      assertTrue(plateau.estPositionValide(new Position(4, 4)), "Position (4,4) devrait être valide");
      assertTrue(plateau.estPositionValide(new Position(2, 3)), "Position (2,3) devrait être valide");
   }

   @Test
   public void testEstPositionValideRetourneFalsePourPositionHorsLimites() {
      Plateau plateau = new Plateau(5, 5, 5);
      
      assertFalse(plateau.estPositionValide(new Position(-1, 0)), "Position (-1,0) devrait être invalide");
      assertFalse(plateau.estPositionValide(new Position(0, -1)), "Position (0,-1) devrait être invalide");
      assertFalse(plateau.estPositionValide(new Position(5, 0)), "Position (5,0) devrait être invalide");
      assertFalse(plateau.estPositionValide(new Position(0, 5)), "Position (0,5) devrait être invalide");
   }

   @Test
   public void testGetEtatCaseLanceExceptionPourPositionInvalide() {
      Plateau plateau = new Plateau(5, 5, 5);
      
      assertThrows(InvalidPositionException.class, () -> {
         plateau.getEtatCase(new Position(-1, 0));
      }, "Devrait lancer InvalidPositionException pour position invalide");
   }

   @Test
   public void testAjouterBateauAugmenteNombreBateaux() {
      Plateau plateau = new Plateau(5, 5, 5);
      Bateau bateau = new Bateau(2, new Position(1, 1), Orientation.HORIZONTAL);
      
      plateau.ajouterBateau(bateau);
      assertEquals(1, plateau.getNombreBateaux(), "Devrait avoir 1 bateau après ajout");
   }

   @Test
   public void testEstOccupeeParBateauRetourneTruePourPositionOccupee() {
      Plateau plateau = new Plateau(5, 5, 5);
      Bateau bateau = new Bateau(3, new Position(1, 1), Orientation.HORIZONTAL);
      plateau.ajouterBateau(bateau);
      
      assertTrue(plateau.estOccupeeParBateau(new Position(1, 1)), "Position (1,1) devrait être occupée");
      assertTrue(plateau.estOccupeeParBateau(new Position(1, 2)), "Position (1,2) devrait être occupée");
      assertTrue(plateau.estOccupeeParBateau(new Position(1, 3)), "Position (1,3) devrait être occupée");
   }

   @Test
   public void testPeutAjouterBateauRetourneFalseSiBateauHorsPlateau() {
      Plateau plateau = new Plateau(5, 5, 5);
      Bateau bateau = new Bateau(3, new Position(0, 4), Orientation.HORIZONTAL);
      
      assertFalse(plateau.peutAjouterBateau(bateau), "Ne devrait pas pouvoir ajouter le bateau (sort du plateau)");
   }

   @Test
   public void testPeutAjouterBateauRetourneFalseSiChevauchement() {
      Plateau plateau = new Plateau(5, 5, 5);
      Bateau bateau1 = new Bateau(3, new Position(1, 1), Orientation.HORIZONTAL);
      Bateau bateau2 = new Bateau(2, new Position(1, 2), Orientation.VERTICAL);
      
      plateau.ajouterBateau(bateau1);
      assertFalse(plateau.peutAjouterBateau(bateau2), "Ne devrait pas pouvoir ajouter le bateau (chevauchement)");
   }

   @Test
   public void testTirerDansEau() throws InvalidPositionException {
      Plateau plateau = new Plateau(5, 5, 5);
      Bateau bateau = new Bateau(2, new Position(1, 1), Orientation.HORIZONTAL);
      plateau.ajouterBateau(bateau);
      
      ResultatTir resultat = plateau.tirer(new Position(0, 0));
      assertEquals(ResultatTir.DANS_EAU, resultat, "Devrait être DANS_EAU");
      assertEquals(EtatCase.EAU, plateau.getEtatCase(new Position(0, 0)), "La case devrait être marquée EAU");
   }

   @Test
   public void testTirerTouche() throws InvalidPositionException {
      Plateau plateau = new Plateau(5, 5, 5);
      Bateau bateau = new Bateau(2, new Position(1, 1), Orientation.HORIZONTAL);
      plateau.ajouterBateau(bateau);
      
      ResultatTir resultat = plateau.tirer(new Position(1, 1));
      assertEquals(ResultatTir.TOUCHE, resultat, "Devrait être TOUCHE");
      assertEquals(EtatCase.BATEAU_TOUCHE, plateau.getEtatCase(new Position(1, 1)), 
         "La case devrait être marquée BATEAU_TOUCHE");
   }

   @Test
   public void testTirerCoule() throws InvalidPositionException {
      Plateau plateau = new Plateau(5, 5, 5);
      Bateau bateau = new Bateau(2, new Position(1, 1), Orientation.HORIZONTAL);
      plateau.ajouterBateau(bateau);
      
      plateau.tirer(new Position(1, 1)); // Premier tir
      ResultatTir resultat = plateau.tirer(new Position(1, 2)); // Deuxième tir
      assertEquals(ResultatTir.COULE, resultat, "Devrait être COULE");
   }

   @Test
   public void testNombreTirsAugmenteApresChaqueTir() throws InvalidPositionException {
      Plateau plateau = new Plateau(5, 5, 5);
      Bateau bateau = new Bateau(2, new Position(1, 1), Orientation.HORIZONTAL);
      plateau.ajouterBateau(bateau);
      
      assertEquals(0, plateau.getNombreTirs(), "Devrait avoir 0 tir au départ");
      
      plateau.tirer(new Position(0, 0));
      assertEquals(1, plateau.getNombreTirs(), "Devrait avoir 1 tir");
      
      plateau.tirer(new Position(1, 1));
      assertEquals(2, plateau.getNombreTirs(), "Devrait avoir 2 tirs");
      
      plateau.tirer(new Position(1, 2));
      assertEquals(3, plateau.getNombreTirs(), "Devrait avoir 3 tirs");
      
      plateau.tirer(new Position(0, 0)); // Case déjà visée
      assertEquals(4, plateau.getNombreTirs(), "Devrait avoir 4 tirs");
   }

   @Test
   public void testTirerPositionNegativeLanceException() {
      Plateau plateau = new Plateau(5, 5, 5);
      
      assertThrows(InvalidPositionException.class, () -> {
         plateau.tirer(new Position(-1, 0));
      }, "Devrait lancer InvalidPositionException pour position négative");
   }

   @Test
   public void testTirerPositionHorsPlateauLanceException() {
      Plateau plateau = new Plateau(5, 5, 5);
      
      assertThrows(InvalidPositionException.class, () -> {
         plateau.tirer(new Position(0, 10));
      }, "Devrait lancer InvalidPositionException pour position hors plateau");
      
      assertThrows(InvalidPositionException.class, () -> {
         plateau.tirer(new Position(10, 0));
      }, "Devrait lancer InvalidPositionException pour position hors plateau");
   }

   @Test
   public void testTousLesBateauxCoulesRetourneTrueQuandTousCoules() throws InvalidPositionException {
      Plateau plateau = new Plateau(5, 5, 5);
      Bateau bateau = new Bateau(2, new Position(1, 1), Orientation.HORIZONTAL);
      plateau.ajouterBateau(bateau);
      
      plateau.tirer(new Position(1, 1));
      plateau.tirer(new Position(1, 2));
      
      assertTrue(plateau.tousLesBateauxCoules(), "Tous les bateaux devraient être coulés");
   }

   @Test
   public void testAfficherPlateauRetourneStringNonVide() {
      Plateau plateau = new Plateau(5, 5, 5);
      
      String affichage = plateau.afficherPlateau();
      assertNotNull(affichage, "L'affichage ne devrait pas être null");
      assertFalse(affichage.isEmpty(), "L'affichage ne devrait pas être vide");
   }

}