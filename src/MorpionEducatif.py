#python 3.7.1
#Auteur : Jean-Baptiste Sanchez

# Définition d'une constante représentant la taille de la grille de jeu
TAILLE_GRILLE = 3

# Définition de la liste des joueurs (classe joueur ?)
joueur = [" ", "x", "o"]

# Définition de la grille 2D de jeu pour sauvegarder les infos de jeu
grille = [[0] * TAILLE_GRILLE for _ in range(TAILLE_GRILLE)]

# Initialisation de cette grille 2D en mettant dans chaque case de celle ci un caractere blanc correspondant au non joueur
for i in range(TAILLE_GRILLE) :
  for j in range(TAILLE_GRILLE):
    grille[i][j] = joueur[0];

# Affichage de la grille vide (a mettre dans fonction ou classe ou objet)
# for i in range(0,TAILLE_GRILLE) :
  # print(joueur[0] + "\t|\t" + joueur[0] + "\t|\t" + joueur[0])

# Définition du joueur actuelle 1 ou 2 en fonction du tour et des variables booleennes permettant le test de victoire et de fin de partie
joueurActuelle = 1
partieIsOver = False

# Tant que la partie n'est pas fini on execute :
while partieIsOver is False:

  # Au début de chaque tour nous affichons l'état de la grille de jeu
  print("\nGrille de jeu\n")
  for i in range(TAILLE_GRILLE) :
    for j in range(TAILLE_GRILLE):
      print("| " + grille[i][j], end = " ")
    print("|")

  # On indique quel joueur doit jouer et nous demandons à l'utilisateur le numéro de la ligne et de la colonne dans laquelle il veut jouer
  print("\nTour :\t" + joueur[joueurActuelle])

  while True:
    try:
      ligne = int(input("Ligne: "))

      if 0 < ligne < TAILLE_GRILLE + 1:
        ligne -= 1

        try:
          colonne = int(input("Colonne: "))

          if 0 < colonne < TAILLE_GRILLE + 1:
            colonne -= 1

            # On ajoute le symbole du joueur qui joue dans la case qu'il veut marquer seulement si la case est vide
            if grille[ligne][colonne] == joueur[0] :
              grille[ligne][colonne] = joueur[joueurActuelle]
              break
            else :
              print("\nErreur : Cette case est déjà marqué par un joueur\n")

          else:
            print("\nErreur : Saisie incorrect\nVeuillez saisir un entier entre 1 et", TAILLE_GRILLE, "\n")

        except ValueError:
          print("\nErreur : Saisie incorrect\nVeuillez saisir un entier entre 1 et", TAILLE_GRILLE, "\n")
          continue

      else:
        print("\nErreur : Saisie incorrect\nVeuillez saisir un entier entre 1 et", TAILLE_GRILLE, "\n")

    except ValueError:
      print("\nErreur : Saisie incorrect\nVeuillez saisir un entier entre 1 et", TAILLE_GRILLE, "\n")
      continue


  # On parcours la grille pour vérifier si il y a des alignements ou si la grille est complete
  # 00 01 02 enchaînement gagnant
  # 10 11 12
  # 20 21 22
  # 00 11 22 diag gagnante
  # 02 11 20
  # si aucun joueur[0] fin de partie égalité
  # si joueur[0] une ligne ne peut pas être gagnante

  # Vérification des lignes horizontal et de  la diagonale en partant du coin gauche
  i = 0
  j = 0
  jInverse = TAILLE_GRILLE
  iFlag = 0
  jFlag = 0
  diagFlag = 0
  alignement = False
  empty = False

  for i in range(TAILLE_GRILLE) :
    case = grille[i][j]
    jFlag = 0
    jInverse = 0
    if alignement is True :
      break

    for j in range(TAILLE_GRILLE) :
      case = grille[i][j]

      if case == joueur[joueurActuelle] :
        jFlag += 1

        if jFlag > TAILLE_GRILLE-1 :
          alignement = True
          break

      # On vérifie si il y a un alignement en diagonale de la gauche vers la droite en partant du coin
      if j == i :
        if case == joueur[joueurActuelle] :
          diagFlag += 1

          if diagFlag > TAILLE_GRILLE-1 :
            alignement = True
            break

  # Vérification de l'autre diagonale
  if (grille[0][2] == joueur[joueurActuelle]) & (grille[1][1] == joueur[joueurActuelle]) & (grille[2][0] == joueur[joueurActuelle]):
    alignement = True

  # Vérification des colonnes
  if ((grille[0][0] == joueur[joueurActuelle]) & (grille[1][0] == joueur[joueurActuelle]) & (grille[2][0] == joueur[joueurActuelle])) | ((grille[0][1] == joueur[joueurActuelle]) & (grille[1][1] == joueur[joueurActuelle]) & (grille[2][1] == joueur[joueurActuelle])) | ((grille[0][2] == joueur[joueurActuelle]) & (grille[1][2] == joueur[joueurActuelle]) & (grille[2][2] == joueur[joueurActuelle])):
    alignement = True

  # Vérification que le terrain ne soit pas complet
  empty = True # On part du postulat que le terrain est complet

  # On parcourt le terrain, si jamais nous rencontrons une case vide alors nous aurons prouver par son contraire que le terrain n'est pas complet
  for i in range(TAILLE_GRILLE) :
    for j in range(TAILLE_GRILLE) :
      case = grille[i][j]
      if (case == joueur[0]) & (empty is False) :
        empty = False

  # Si une des vérification d'alignement à fonctionné alors on termine le jeu
  if alignement is True | empty is True:
    print("\nGrille de jeu\n")
    for i in range(TAILLE_GRILLE) :
      for j in range(TAILLE_GRILLE):
        print("| " + grille[i][j], end = " ")
      print("|")
    gagnant = joueurActuelle
    print("Le joueur ", joueur[joueurActuelle], " a gagné la partie")
    partieIsOver = True

  # Sinon on continue le jeu donc on switch de joueur
  else:
    if joueurActuelle==1:
      joueurActuelle=2
    else:
      joueurActuelle=1


input("Appuyer sur ENTER pour terminer le programme.")
