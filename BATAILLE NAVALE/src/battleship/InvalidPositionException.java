package battleship;

/**
 * 
 */
public class InvalidPositionException extends Exception {
    /** Constructs a new exception with no detail message
     */
    public InvalidPositionException() {
      super();
    }
    
    /** Constructs a new exception with the specified detail message
     * @param message the specified detail message
     */
    public InvalidPositionException(String message) {
      super(message);
   }
}
