package battleship;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class BateauTest {

   @Test
   public void testOccupePositionHorizontal() {
      Bateau bateau = new Bateau(3, new Position(0, 0), Orientation.HORIZONTAL);
      
      assertTrue(bateau.occupePosition(new Position(0, 0)), "Devrait occuper (0,0)");
      assertTrue(bateau.occupePosition(new Position(0, 1)), "Devrait occuper (0,1)");
      assertTrue(bateau.occupePosition(new Position(0, 2)), "Devrait occuper (0,2)");
      assertFalse(bateau.occupePosition(new Position(0, 3)), "Ne devrait pas occuper (0,3)");
      assertFalse(bateau.occupePosition(new Position(1, 0)), "Ne devrait pas occuper (1,0)");
   }
   
   @Test
   public void testBateauNestPasCouleSansImpact() {
      Bateau bateau = new Bateau(2, new Position(1, 1), Orientation.VERTICAL);
      
      assertFalse(bateau.estCoule(), "Ne devrait pas être coulé sans impact");
   }
   
   @Test
   public void testBateauNestPasCouleSiPartielementTouche() {
      Bateau bateau = new Bateau(2, new Position(1, 1), Orientation.VERTICAL);
      
      bateau.toucher(new Position(1, 1));
      assertFalse(bateau.estCoule(), "Ne devrait pas encore être coulé après un seul impact");
   }
   
   @Test
   public void testBateauEstCouleQuandToutesTouchees() {
      Bateau bateau = new Bateau(2, new Position(1, 1), Orientation.VERTICAL);
      
      bateau.toucher(new Position(1, 1));
      bateau.toucher(new Position(2, 1));
      assertTrue(bateau.estCoule(), "Devrait être coulé après tous les impacts");
   }

}