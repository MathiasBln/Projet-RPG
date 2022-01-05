
from Combat import combat
from final_combat import *
from colors import *
from Inventaire import inventory
from chest import open_chest
from ascii import end
from enigme_goblin import enigma
from LordPouic import LordPouic
from final_combat import boss_combat

#Retourne une carte
def view_Map():
    view_map = [
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",".", ".", ".", ".", ".", ".", ".", ".", ".", ".","#", "#", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "█", "█", "█", "█", "█", "█", "█", "█","█", ".", ".", ".", ".", ".", "", ".", ".", "#","#", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "█", " ", "", " ", " ", " ", " ", " ","█", ".", ".", "§", ".", ".", ".", ".", "#", "#",".", ".", ".", "█", "█", "█", "█", ".", ".", "."],
        [".", ".", "█", " ", " ", " ", " ", " ", " ", " ","█", ".", "§", "§", ".", ".", ".", "#", "#", ".",".", ".", "░", "/", " ", "", "█", ".", ".", "."],
        [".", ".", "█", " ", " ", " ", "X", " ", " ", " ","█", ".", "§", "§", ".", ".", "#", "#", ".", ".",".", ".", "░", "█", "█", " ", "█", ".", ".", "."],
        [".", ".", "█", " ", " ", " ", " ", " ", " ", " ","█", ".", "§", ".", ".", "#", "#", ".", ".", ".",".", ".", "░", ".", "█", "█", "█", ".", ".", "."],
        ["#", ".", "█", " ", " ", " ", " ", " ", " ", " ","█", ".", ".", ".", "#", "#", "#", ".", ".", ".",".", ".", "░", ".", ".", ".", ".", ".", ".", "."],
        ["#", ".", "█", "█", "█", "█", "/", "█", "█", "█","█", ".", "#", "#", "#", ".", ".", ".", ".", ".",".", ".", "░", ".", ".", "§", ".", ".", ".", "."],
        ["#", "#", "§", "§", ".", " ", "░", ".", ".", "§","§", ".", "#", "#", ".", ".", ".", ".", ".", ".",".", "§", "░", "§", ".", "§", "§", ".", ".", "."],
        [".", "#", "#", ".", ".", ".", "░", "░", ".", ".",".", ".", ".", "#", "#", ".", ".", ".", ".", ".",".", "§", "░", "§", "§", "§", ".", "†", "†", "."],
        [".", "#", "#", ".", ".", ".", ".", "░", ".", ".",".", ".", ".", "#", "#", "#", ".", ".", ".", ".","§", "§", "░", "§", "§", ".", ".", "†", "†", "†"],
        ["§", ".", "#", "#", "§", ".", ".", "░", "░", "░","░", "░", ".", ".", "#", "#", "#", "§", "§", "§","§", "░", "░", "░", "§", "§", "†", "†", "†", "†"],
        ["§", ".", ".", "#", "#", "§", ".", ".", "░", "░","░", "░", "░", "░", "=", "=", "=", "░", "░", "░","░", "░", " ", "░", "░", "░", ".", "†", "†", "†"],
        ["§", ".", "§", ".", "#", "#", ".", ".", ".", ".",".", ".", "░", "░", "=", "=", "=", "░", "░", "░","░", "░", "", "░", "§", "§", "†", "†", "†", "†"],
        ["§", "§", "§", "§", ".", "#", "#", "§", ".", ".",".", ".", ".", ".", "#", "#", "#", "§", "§", "§","§", "░", "░", "░", "░", "§", "†", "†", "†", "†"],
        ["§", "", "█", "█", "█", " ", "#", "#", "#", "§","§", "§", ".", "#", "#", "#", ".", ".", ".", ".","§", "§", "░", "§", "░", "§", "†", "†", "†", "†"],
        ["§", "§", "█", "¶", "█", "§", ".", "#", "#", "#","#", "§", "#", "#", ".", ".", ".", ".", ".", ".",".", "§", "░", "§", "░", "░", "§", "§", "§", "§"],
        ["§", "§", "█", "/", "█", "§", "§", ".", ".", "#","#", "#", "#", ".", ".", ".", ".", ".", ".", ".",".", ".", "░", ".", "§", "░", "░", "§", "§", "§"],
        ["§", "§", "§", "§", "§", "§", "§", "§", ".", ".","#", "#", ".", ".", ".", ".", ".", ".", ".", ".",".", "░", "░", ".", "§", "§", "░", "░", "§", "§"],
        ["§", "§", "§", "§", "§", "§", "§", "§", "§", ".",".", ".", ".", ".", ".", ".", ".", ".", ".", ".",".", "░", "░", ".", "§", "§", "§", "░", "░", "§"],
        ["§", "§", "§", "§", "§", "§", "§", "§", "§", "§",".", ".", ".", ".", ".", ".", ".", ".", ".", ".",".", ".", ".", ".", "§", "§", "§", "§", "░", "◊"],
    ]
    return view_map

#retourne une liste de chaine de caractère
def text_Error():
    listing_sentance = [
        "Vous ne pouvez pas avancer, il y a un mur !",
        "Trouvez le pont pour traverser !",
        "Vous êtes en bordure de map, impossible de vous diriger vers cette direction !"
    ]
    return listing_sentance

#permet d'afficher la carte
def see_map(map):
    for i in range (len(map)):
        draw_map ="  ".join(map[i])
        print(draw_map)

#Bloque les bords de la carte
def error_map(Y, X):
    verif = False
    if Y > 20 or Y < 0:
        verif = True
    elif X > 29 or X < 0:
        verif = True
    return verif

#Permet de remplacer l'emplacement du joueur par un . afin de voir ses déplacements
def evolution_map(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == bcolors.FAIL + "X" + bcolors.RESET:
                map[i][j] = bcolors.FAIL + "." + bcolors.RESET


#Bouge et bloque X si il va vers un mur ou de l'eau
def move_X(choice, X, Y, tab):
    sentance = text_Error()
    if choice == "D":
        if X + 1 > 29:
            print(sentance[2])
            X = 29
        elif tab[Y][X + 1] == "█":
            print(sentance[0])
        elif tab[Y][X + 1] == "#":
            print(sentance[1])
        else:
            X += 1 
    elif choice == "Q":
        if X - 1 < 0:
            X = 0
            print(sentance[2])
        elif tab[Y][X - 1] == "█":
            print(sentance[0])
        elif tab[Y][X - 1] == "#":
            print(sentance[1])
        else:
            X -= 1 
    return X

#Bouge et bloque X si il va vers un mur ou de l'eau
def move_Y(choice, Y, X, tab):
    sentance = text_Error()
    if choice == "S":
        if Y + 1 > 20:
            Y = 20
            print(sentance[2])
        elif tab[Y + 1][X] == "█":
            print(sentance[0])
        elif tab[Y + 1][X] == "#":
            print(sentance[1])
        else:
            Y += 1
    elif choice == "Z":
        if Y -1 < 0:
            Y = 0
            print(sentance[2])
        elif tab[Y - 1][X] == "█":
            print(sentance[0])
        elif tab[Y - 1][X] == "#":
            print(sentance[1])
        else:
            Y -= 1
    return Y

#Retourne une liste de commande possible
def move_possible():
    set_move = ["z", "s", "q", "d", "m", "Z", "S", "Q", "D"]
    return set_move


def Map():
    #Position de départ
    X = 6
    Y = 4

    #Instanciation position monstre
    posX_fight = [2,10,13,5,7,18,25,15,4,27,8,1,7,13,18,8, -1]
    posY_fight = [0,0,4,6,6,7,7,9,10,12,13,17,17,17,18,20, -1]

    #Instanciation position coffre
    posX_chest = [4,25,1,16,22, -1]
    posY_chest = [2,3,15,1,13, -1]

    #Instanciation map et mouvement
    view_map = view_Map()
    view_map[Y][X] = bcolors.FAIL + "X" + bcolors.RESET
    move_poss = move_possible()

    end_game = False

    #Instanciation Vie du perso + inventaire
    dora_life = 50
    bag = inventory()

    #Début des déplacements
    while end_game == False:
        
        #Selectionner un mouvement + gestion erreur
        choice_mouvement = str(input())
        while choice_mouvement not in move_poss:
            print("Mouvement impossible, utilisez les bonnes touches !")
            choice_mouvement = str(input())

        upper_choice = choice_mouvement.upper()

        if upper_choice == "M":
            see_map(view_map)

        #Modifie X et Y
        X = move_X(upper_choice, X, Y, view_map)
        Y = move_Y(upper_choice, Y, X, view_map)

        #Verif des erreurs
        verif_map = error_map(Y, X)
        while verif_map == True:
            choice_mouvement = str(input())
            upper_choice = choice_mouvement.upper()
            if upper_choice == "M":
                see_map(view_map)
            X = move_X(upper_choice, X, Y, view_map)
            Y = move_Y(upper_choice, Y, X, view_map)
            verif_map = error_map(Y, X)

        #Gestion d'une case de combat
        for i in range(len(posX_fight) - 1):
            if X == posX_fight[i] and Y == posY_fight[i]:
                save = combat(dora_life, bag)
                dora_life = save[1]
                bag = save[0]
                posX_fight.remove(X)
                posY_fight.remove(Y)

        #Gestion d'une case de coffre
        for i in range(len(posX_chest) - 1):
            if X == posX_chest[i] and Y == posY_chest[i]:
                bag = open_chest(bag,X,Y)
                posX_chest.remove(X)
                posY_chest.remove(Y)

        #Gestion Event
        if X == 14 and Y == 12 or X == 14 and Y == 13:
            dora_life = enigma(dora_life)
            X = 17
        if view_map[Y][X] == "¶":
            save = LordPouic(dora_life, bag)
            dora_life = save[0]
            bag = save[1]
            Y = 18
        elif X == 29 and Y == 20:
            save = boss_combat(dora_life,bag)
            if save == True:
                print("Bravo, vous avez gagné la partie")
                exit()  


        #Modifie l'emplacement du joueur sur la map
        evolution_map(view_map)

        view_map[Y][X] = bcolors.FAIL + "X" + bcolors.RESET

        

