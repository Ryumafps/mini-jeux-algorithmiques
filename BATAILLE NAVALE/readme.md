# POO java - TP 5

---

Ce TP consiste à implémenter un jeu de bataille navale en Java. L'objectif est de créer un jeu fonctionnel où un joueur peut attaquer des positions sur un plateau pour couler des navires prédéfinis. Le programme inclut la gestion des saisies utilisateur, l'affichage du plateau, le suivi des tirs et la détection de la fin de partie.

---

# Note : Toutes les commandes doivent être exécutées depuis le dossier racine du projet(Dans /TP5$).

#### Compilation des .java

```
javac -sourcepath src src/battleship/*.java src/io/*.java -d classes
```

#### Génération de la documentation

```
javadoc -sourcepath src src/battleship/*.java src/io/*.java -d docs
```

#### Compilation des tests

```
javac -cp classes:junit-console.jar -d classes test/*.java
```

#### Exécution des tests

```
java -jar junit-console.jar -class-path classes -scan-classpath
```

#### Exécution du programme

```
java -cp classes battleship.BattleShipMain
```

#### Création du fichier .jar à partir de MANIFEST.MF

```
jar cvfm battleship.jar MANIFEST.MF -C classes .
```

#### Exécution du programme avec un .jar

```
java -jar battleship.jar
```
