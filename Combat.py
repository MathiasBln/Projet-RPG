#VERSION 23/12 15h06
from random import randint
from copy import copy
from colors import *
from Monstre import *
from Monster_ASCII import *
from menu import *
from ascii import you_Die
from Inventaire import select_menu

#afficher la vie lors des combats 
def life_print(For):
    life = []
    for i in range(For):
        life.append("█")
    str_word = "".join(life)
    print("Vie:", bcolors.FAIL + str_word + bcolors.RESET, (For * 2), "%")
    if For == 0:
        print(bcolors.FAIL + you_Die + bcolors.RESET)

def dora_attack():
    dora_spells = [
        ["GERMAN SOUPLEX : entrez 0", 6, 4, "Definition"],
        ["DORA SMASH : entrez 1", 8, 7, "Definition"],
        ["BABOUCHKA : entrez 2", 17, 9,"Definition", 2]
    ]
    return dora_spells

def error_program_combat(choice):
    list_str_numbers = ["0","1","2","3"]
    while choice not in list_str_numbers:    
            print('Mauvaise commande, veuillez entrer seulement 0, 1, 2, 3')
            choice = input()
    return choice

def combat(dora_life, inventory):

    #Monstre
    ascii_m = monster_ascii()
    beast = monster()
    beast_attack = monster_attack()

    #Dora
    dora_at = dora_attack()
    
    #Choix du monstre
    choice_monster = randint(0,4)
    print(ascii_m[beast[choice_monster][2]])
    print(beast[choice_monster][0], "VOUS ATTAQUE ATTENTION !!!!!\n ")
    monster_life = beast[choice_monster][1]

    player_turn = True
    
    round = 0

    while monster_life > 0 or dora_life > 0:

        #Affichage vie
        print("VOTRE VIE")
        life_print(dora_life)
        print()
        print("VIE DE", beast[choice_monster][0])
        life_print(monster_life)
        print()
        if round % 2 == 0:
            print("___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___")

        #Tour du joueur
        if player_turn == True:
            print("Quelle attaque voulez-vous faire?")
            for i in range(len(dora_at)):
                print(dora_at[i][0])
            
            choice_attack = input()
            choice_attack = error_program_combat(choice_attack)
            
            if type(choice_attack) == type("str"):
                choice_attack = int(choice_attack)

            # choix 3 : accéder à son sac à dos (inventaire)
            if choice_attack == 3:
                save = select_menu(dora_life, inventory)
                dora_life = save[1]
                inventory = save[0]
            else:
                print(dora_at[choice_attack][3])
                critical_rate = randint(0,10)
                for i in range(len(dora_at)):
                    if choice_attack == i:
                        print(dora_at[i][0])
                        monster_life -= dora_at[i][1]
                        if critical_rate > dora_at[i][2]:
                            monster_life -= dora_at[i][1]
            player_turn = False
            round += 1
            
            #Tour du monstre
        else:
            choice_attack = randint(beast[choice_monster][3],beast[choice_monster][5])
            critical_rate = randint(0,10)
            print()
            print(beast_attack[choice_attack][0])
            print(beast_attack[choice_attack][3])
            if beast_attack[choice_attack][0] == "DRAIN TITANO":
                dora_life -= beast_attack[choice_attack][1]
                monster_life += beast_attack[choice_attack][1]
                if critical_rate > beast_attack[choice_attack][2]:
                    dora_life -= beast_attack[choice_attack][1]
                    monster_life += beast_attack[choice_attack][1]
            elif beast_attack[choice_attack][0] == "ADAMENTIUM":
                monster_life += beast_attack[choice_attack][1]
            else:
                dora_life -= beast_attack[choice_attack][1]
                if critical_rate > beast_attack[choice_attack][2]:
                    dora_life -= beast_attack[choice_attack][1]
            player_turn = True
            round += 1

        
            
        #Fin du combat
        #Mort de l'ennemi
        if monster_life <= 0:
            print("Vous avez vaincu", beast[choice_monster][0])
            #Free loot
            random_loot = randint(0,100)
            
            if random_loot <= beast[choice_monster][6]:
                
                inventory_copy = copy(inventory)
                for key, value in inventory_copy.items():
                    if key == "Pomme" and value > 0:
                        inventory["Pomme"] += 1
                    else:
                        inventory.update({'Pomme': 1})
            round = 0
            return inventory, dora_life

        #Mort de Dora + verif Totem
        elif dora_life <= 0:
            totem = False
            for key in inventory:
                if key == "Totem":
                    if inventory[key] > 0 :
                        print("Votre Totem a été utilisé, vous pouvez continuer à combattre !")
                        inventory["Totem"] -= 1 
                        dora_life = 50
                        totem = True
            if totem == False:
                print(bcolors.FAIL + you_Die + bcolors.RESET)
                print("Voulez-vous rejouer?")
                choice = str(input())
                if choice == "oui":
                    menu_game()
                else:
                    exit() 
            totem = False 
                            
    return inventory, dora_life

