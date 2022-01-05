from random import choice
from Map import Map
from ascii import *
from tuto import *

def menu_game():

    print(asci_top_sword + bcolors.FAIL + asci_top + bcolors.RESET + asci_top_sword_reverse)
    error_program("entrer", "pour continuer.")
    print(asci_menu + asci_new_game + asci_choose_language + asci_infos_credits + asci_quit + asci_what_to_do)
    choice_menu = str(input())

    while choice_menu != "1" and choice_menu != "2" and choice_menu != "3" and choice_menu != "4":
        print("Commande non reconnue, assurez vous d'avoir bien entré 1, 2, 3 ou 4.") 
        choice_menu = str(input())

    #nouvelle partie
    if choice_menu == "1":
        new_game()

    #choisir langue
    elif choice_menu == "2":
        choose_language()
        error_program("menu", "pour revenir au menu principal")
        menu_game()

    #infos et credits
    elif choice_menu == "3":
        info_credit()
        error_program("menu", "pour revenir au menu principal.")
        menu_game()

    #quitter le jeu
    elif choice_menu == "4":
        quit_game()


    #appeler fonctions en dessous
def quit_game():
        print("Le jeu est fermé.")
        exit()

def quit_to_menu(choice):
    if choice == "Quit":
        menu_game()

def new_game():
    print(synopsis())
    error_program("continuer", "pour commencer.")
    print("Voulez-vous accéder à un tuto ? Répondez oui pour y accéder ou tapez non pour jouer")
    choice_tuto = str(input().lower())
    if choice_tuto == 'oui':
        tuto_game()
        Map()
    elif choice_tuto == 'non':
        Map()
    else:
        # Ici comment faire mieux, je n'ai pas pu utiliser la fonction error_program car c'est un choix entre oui ou non (pas un seul word)
        while choice_tuto != 'oui' or choice_tuto != 'non':
            print('Vous avez voulu accéder au jeu ? tapez non pour accéder au jeu')
            choice_tuto = str(input().lower())
            if choice_tuto == 'non':
                Map()
            elif choice_tuto == 'oui':
                tuto_game()
                Map()
    
def error_program(word, sentance):
    print("Écrire", word, sentance )
    choice_back = str(input())
    while choice_back != word:
        print("Commande non reconnue, assurez vous d'avoir bien entré", word)
        choice_back = str(input())
        if choice_back == word:
            break

def choose_language():
    print("DLC payant, 19,99€")

def info_credit():
    print("Dora Soul est un jeu vidéo de type RPG exclusivement codé et développé en Python.\nCe jeu vous plonge dans un monde fantastique prenant pour référence le dessin animé\"Dora l'Exploratrice\".\nSon but est une fois de plus vivre une aventure incroyable dans un monde sombre à la Dark Souls.\n \n")
    print("\nUgo DUMOUCHEL\nJulien VERITE\nYassine HABIBI\nAmaury FRANSSEN\nMathias BOUILLON\n")

def synopsis():
    context ="Dora est une exploratrice qui parcourt terres et mers à la recherche d’objets et pour accomplir des missions. \nElle est accompagnée de Babouche et d’une carte." 
    event ="\nAprès une mission périlleuse elle récupèra un objet étrange, mais il s'avérait être un artefact maudit." 
    new_world ="\nA la tombée de la nuit, l'artefact envoûta son inconscient et la plongea dans un profond cauchemard."
    goal ="\nPour se reveiller, elle devra combattre plusieurs adversaires qui lui sont familiers et de combattre l'artefact."

    all_strings = str(context)+str(event)+str(new_world)+str(goal)
    return all_strings