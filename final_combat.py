from random import randint
from copy import copy
from Combat import dora_attack, life_print, error_program_combat
from colors import *
from Monstre import *
from Monster_ASCII import *
from menu import *
from ascii import you_Die
from Inventaire import select_menu


def boss_combat(dora_life, inventory):
    
    # Paramètrage du boss : son ascii, sa liste, ses attaques.
    asci_boss = boss_ascii()
    great_monster = boss_monster()
    beast_attack = boss_monster_attacks()

    #Dora
    dora_at = dora_attack()
    
    #Affichage du boss
    print(asci_boss[0])
    print("Living Dead Mammoth vous attaque, soyez prêt pour le combat final. Il détermine votre destinée. \n ")
    monster_life = great_monster[1] # Accés aux PV du boss

    player_turn = True
    
    round = 0
    boss_result = False

    while monster_life > 0 or dora_life > 0:

        #Affichage vie
        print("VOTRE VIE")
        life_print(dora_life)
        print()
        print("VIE DE", great_monster[0])
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
            
            choice_attack = int(choice_attack)
                
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
            choice_attack = randint(great_monster[2],great_monster[5])
            critical_rate = randint(0,10)
            print()
            print(beast_attack[choice_attack][0])
            print(beast_attack[choice_attack][3])
            if beast_attack[choice_attack][0] == "EAU DE GLACE":
                dora_life -= beast_attack[choice_attack][1]
                monster_life += beast_attack[choice_attack][1]
                if critical_rate > beast_attack[choice_attack][2]:
                    dora_life -= beast_attack[choice_attack][1]
                    monster_life += beast_attack[choice_attack][1]
            elif beast_attack[choice_attack][0] == "HELL RIFT":
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
            print(asci_boss[1]) 
            boss_result = True
            return boss_result
        #Mort de Dora
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

       
    return boss_result