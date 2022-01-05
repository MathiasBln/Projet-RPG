from random import randint
from copy import copy
from colors import *
from menu import *
from ascii import you_Die
from Inventaire import select_menu
from Combat import *

def LordPouic(dora_life, inventory):
    
    point = 0

    print("""
            ..-.--..
           ,','.-`.-.`.
          :.',;'     `.\.
          ||//----,-.--\|
        \`:|/-----`-'--||'/                       _______________________________
         \\|:    |:'   ||/    
          `||      \   |!                   Tu rentres chez moi pour voler mon precieux
          |!|          ;|             Tu devras répondre aux questions sinon tu finiras sur un pieu!
          !||:.   --  /|!               
         /||!||:.___.|!||\\
        /|!|||!|    |!||!\\:.
     ,'//!||!||!`._.||!||,:\\\\
    : :: |!|||!| SSt|!||! |!::
    | |! !||!|||`---!|!|| ||!|
    | || |!|||!|    |!||! |!||

    """)
 

    #instanciation des questions/réponses
    question = ["Quelle est la date de création d'Internet?", "Que veut dire W.W.W.?", "Lequel de ces outils n'est pas un navigateur?"]
    all_answer = [
        ["1996", "2000", "1960"],
        ["We Want Wine", "World Wild Web", "Wild Web World"],
        ["Google", "Firefox", "Safari"],
    ]
    good_answer = ["1960", "WORLD WILD WEB","GOOGLE"]

    #Série de question
    k = 1
    for i in range(3):
        print("Question", k)
        k += 1
        print(question[i])
        for j in range(len(all_answer[i])):
            print(all_answer[i][j])
        choice_answer = str(input())
        upper_choice = choice_answer.upper()
        if upper_choice == good_answer[i]:
            point += 1
        print()

    #Résultat obtenu
    if point >= 2:
        inventory.update({'Totem': 1})
        print("Tu as bien répondu, je te donne mon Précieux! Le Totem de Résurrection (à usage unique) ")
        return dora_life, inventory
    else:
        lord_life = 55
        lord_attack = [
            ['Ice Arrow',2,6, "Une énorme flèche de glace vous transperce et change l'état de la pièce!"],
            ['Fire Arrow',4,7, "Crache du feu de sa bouche et enflamme sa flèche avant de la tirer sur vous!"], 
            ['Rain of Arrow',6,9, "Impossible d'esquiver cette pluie de flèche!"], 
        ]

        #Combat contre Pouic
        #Dora
        dora_at = dora_attack()

        player_turn = True
    
        round = 0

        while dora_life > 0 or lord_life > 0:

            #Affichage vie
            print("VOTRE VIE")
            life_print(dora_life)
            print()
            print("VIE DE LORD POUIC")
            life_print(lord_life)
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
                # Transformation du type str en type int
                choice_attack = int(choice_attack)
                    
                if choice_attack == 3:
                    save = select_menu(dora_life, inventory)
                    dora_life = save[1]
                    inventory = save[0]
                else:
                    print(dora_at[choice_attack][3])
                    tx_Crit = randint(0,10)
                    for i in range(len(dora_at)):
                        if choice_attack == i:
                            print(dora_at[i][0])
                            lord_life -= dora_at[i][1]
                            if tx_Crit > dora_at[i][2]:
                                lord_life -= dora_at[i][1]
                player_turn = False
                round += 1
                
                #Tour du monstre
            else:
                choice_attack = randint(0,2)
                tx_Crit = randint(0,10)
                print()
                print(lord_attack[choice_attack][0])
                dora_life -= lord_attack[choice_attack][1]
                if tx_Crit > lord_attack[choice_attack][2]:
                    dora_life -= lord_attack[choice_attack][1]
                player_turn = True
                round += 1

            #Fin du combat
            #Mort de l'ennemi
            if lord_life <= 0:
                print("Bravo, tu m'as vaincu, je te donne mon Précieux! Le Totem de Résurrection (à usage unique)")
                inventory.update({'Totem': 1})
                return dora_life, inventory

            #Mort de Dora
            elif dora_life <= 0:
                print(bcolors.FAIL + you_Die + bcolors.RESET)
                print("Voulez-vous rejouer?")
                choice = str(input())
                if choice == "oui":
                    menu_game()
                else:
                    exit() 

        return dora_life, inventory




    