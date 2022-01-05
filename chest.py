def open_chest(inventory,X,Y):
    print("Bravo, vous avez trouvé un coffre !!")
    if X == 4 and Y == 2:
        inventory.update({'Baguette magique': 2})
    elif X == 25 and Y == 3:
        inventory.update({'Butter chicken': 1})
    elif X == 1 and Y == 15:
        inventory.update({'Poulet au caramel': 1})
    elif X == 22 and Y == 13:
        inventory.update({'Redbull': 1})
    elif X == 16 and Y == 1:
        inventory.update({'Bon souvenir': 1})

    print("Whaou ! Dora, regarde ton cartable, regarde bien tu as quelque_chose en plus : ")
    
    for key,value in inventory.items():
        print("-",key,":",value)

    return inventory
        

    