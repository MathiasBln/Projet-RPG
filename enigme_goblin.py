from random import randint
from goblin_ascii import *
from Combat import life_print


def enigma(dora_life):
    # énigme Père Pougniasse
    print(goblin_dialogs_alt)

    choice_enigma = str(input())
    upper_choice = choice_enigma.upper()

    while upper_choice != "PYTHON":

        choice_random = randint(0, 1)
        if choice_random == 0:          # Perds 10 PV
            print(goblin_enigma_bad_1)
            dora_life -= 10
            print("VOTRE VIE")
            life_print(dora_life)
        elif choice_random == 1:        # Perds 5 PV
            print(goblin_enigma_bad_2)
            dora_life -= 5
            print("VOTRE VIE")
            life_print(dora_life)
        choice_enigma = str(input())
        upper_choice = choice_enigma.upper()


    if upper_choice == "PYTHON":
        print(goblin_enigma_good)

    return dora_life

