from Map import view_Map, see_map
from random import randint
from Monstre import monster,monster_attack
from Monster_ASCII import monster_ascii
from menu import *
from Inventaire import inventory, select_menu
from Combat import life_print, dora_attack, error_program_combat

def error_program(word, phrase):
    print("Écrire", word, phrase )
    choice_back = str(input())
    while choice_back != word:
        print("Commande non reconnue, assurez vous d'avoir bien entré", word)
        choice_back = str(input())
        if choice_back == word:
            return choice_back



def tuto_game():
    print("Bienvenue sur \"Dora Soul\", avant tout nous allons vous expliquer les mécanismes à apprendre afin de partir sur de bonnes bases !")
    print("Pour commencer vous allez afficher la map, pour cela il suffit simplement d'écrire \"m\".")
    error_program("m", "pour afficher la map")
    print_map = view_Map()
    see_map(print_map)
    print("Voici la carte, elle vous servira pour ne pas vous perdre !")
    print("Maintenant place aux déplacements, vous avez le choix entre 4 directions, \"z\" \"q\" \"s\" \"d\".\nEssayez de descendre une fois.")
    error_program("s", "pour descendre")
    print("En descendant vous avez croisé votre premier monstre.. Voyons comment nous allons faire pour le battre.")
    combat(50, inventory())
    print("Toutes les bases du jeu vous ont été apprises, maintenant place à votre aventure, retrouvez l'artefact.\n ")
    print("A toi de jouer, Dora")


def combat(dora_Life, inventory):

    #Monstre
    ASCII_M = monster_ascii()
    beast = monster()
    beast_attack = monster_attack()

    #Dora
    player_attack = dora_attack()
    
    #Choix du monstre
    print(ASCII_M[beast[0][2]])
    print(beast[0][0], "vous attaque attention !\n ")

    monster_life = beast[0][1]
    player_turn = True

    for i in range(2):
        print("VOTRE VIE")
        life_print(dora_Life)
        print()
        print("VIE DE", beast[0][0])
        life_print(monster_life)
        print()
        if player_turn == True:
            for i in range(len(player_attack)):
                print(player_attack[i][0])
            print("Voici vos attaques, choisissez le bon combo pour mettre fin à sa vie ! \nSinon durant le jeu vous pourrez écrire 3 afin d'ouvrir votre inventaire pour utiliser certains objets qui peuvent vous être utiles !")    
            choice_attack = input()
            choice_attack = error_program_combat(choice_attack)
            if choice_attack == 3:
                save = select_menu(dora_Life, inventory)
                dora_Life = save[1]
                inventory = save[0]
                print(inventory)
                print(dora_Life)
            else:
                tx_Crit = randint(0,10)
                for i in range(len(player_attack)):
                    if choice_attack == i:
                        print(player_attack[i][0])
                        monster_life -= player_attack[i][1]
                        if tx_Crit > player_attack[i][2]:
                            monster_life -= player_attack[i][1]
            player_turn = False

            
        else:
            choice_attack = randint(beast[0][3],beast[0][5])
            tx_Crit = randint(0,10)
            print()
            print(beast_attack[choice_attack][0])
            print("Description")
            for i in range(len(beast_attack)):
                if choice_attack == i:
                    dora_Life -= beast_attack[i][1]
                    if tx_Crit > beast_attack[i][2]:
                        dora_Life -= beast_attack[i][1]
            player_turn = True

    
    print("Vous avez vaincu", beast[0][0], "dorénavant vous êtes prêts pour vos prochains combats.")     
    
    return 1





