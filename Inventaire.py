from random import randint

#------------- OBJETS DE L'INVENTAIRE ISSUS DES COFFRES ---------------------

  #FONCTION POUR Baguette magique
def magic_wand_loot(dora_life):
  random_num = randint(0,4)
  wand = 5
  dora_life += wand*random_num
  print("La baguette magique ne marche pas toujours mais peut vous donner peu ou beaucoup de vie en plus")
  return dora_life

def caramel_chicken(dora_life):
  dora_life += 20
  print("Attention! une bouchée de trop est votre santé mentale tombe à zéro")
  return dora_life

def butter_chicken(dora_life):
  random_num = randint(1,2)
  if random_num == 1:
    dora_life += 12
    print("direction Gare du Nord pour ton meilleur Butter Chicken !!")
  else:
    dora_life -= 5
    print("dommage tu as pris un Butter Chicken du street wok, tellement immonde que tu perds des PV")
  return dora_life

def redbull_loot(dora_life):
  dora_life = 50
  print("La Redbull régénère toute votre santé")
  return dora_life

def good_remember(dora_life):
  print("Une photo de votre famille pop devant vous, votre santé est reboostée!")
  dora_life += 15
  return dora_life
#----------------------------------------------------- ---------------------


#Objet de base 
def apple_loot(dora_life):
  apple = 10
  dora_life += apple 
  print("La pomme régénére votre santé")
  return dora_life 



#Affichage inventaire avec items > 0
def listing(dico):
  new_dico = {}
  for k, v in dico.items():
    if v > 0:
      new_dico.update({k : v})
  return new_dico

#Creation de l'inventaire
def inventory():
  inventory = {}
  object_map_potion = {"Pomme" :  2 }
  object_map_special = {"Redbull" : 0  , "Totem" :  0 }
  potion_list = listing(object_map_potion)
  special_list = listing(object_map_special)
  inventory.update(potion_list)
  inventory.update(special_list)
  return inventory

#Fonction utilisation de l'inventaire
def select_menu(dora_life, inventory):
    inventory = listing(inventory)
    print(inventory)
    choice = str(input("Veuillez entrer le nom de l'objet que vous voulez utiliser:"))
    print("Si vous voulez sortir, dites 'Sortir'")
    if choice == "Sortir":
        return inventory, dora_life
    else:
      while choice not in inventory :
          print("L'object utilisé n'est pas dans l'inventaire ou vous avez mal écris le nom de l'objet.")
          print("ATTENTION aux espaces, qu'il n'y ait pas de majuscule et que votre réponse ne soit pas un chiffre")
          choice =str(input("Veuillez choisir un objet présent dans l'inventaire: "))

    object_listing  =["Pomme", "Redbull", "Totem","Baguette magique","Butter chicken","Poulet au caramel"]

    if choice in object_listing:
      #gestion problème choix du totem
        print("Voulez vous vraiment utiliser la potion de", choice,  "?")
        if choice == "Totem":
                print("Vous ne pouvez pas utiliser cet objet, il s'active automatiquement le moment venu!")
                inventory["Totem"] = 1
                select_menu(dora_life, inventory)
      #selection d'un objet
        else:
          second_choice = input("oui ou non ?")
          if second_choice == "oui":
              inventory[choice] -= 1
              if choice == "Pomme":
                  dora_life = apple_loot(dora_life)
              elif choice == "Redbull":
                  dora_life = redbull_loot(dora_life)
              elif choice == "Baguette magique":
                  dora_life = magic_wand_loot(dora_life)
              elif choice == "Butter chicken":
                  dora_life = butter_chicken(dora_life)
              elif choice == "Poulet au caramel":
                  dora_life = caramel_chicken(dora_life)
              elif choice == "Bon souvenir":
                  dora_life = good_remember(dora_life)
          else:
              select_menu(dora_life, inventory)


    inventory = listing(inventory)

    return inventory, dora_life


