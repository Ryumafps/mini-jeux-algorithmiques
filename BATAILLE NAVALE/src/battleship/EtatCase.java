package battleship;

/** Enumeration des états d'une case
*/
public enum EtatCase{
    INCONNUE, //'.' - jamais visée
    EAU, //'~' - visée et vide
    BATEAU_TOUCHE //'*'  - visée et bateau tocuhée
}