
#liste bidimensionnelle incluant le nom d'attaques de monstres 
def monster_attack():
    monster_spells = [
        # [Nom Attaque, DGT, Tx CRIT, Description]
        ["SHRED", 5 , 5, "Meca Shipper charge son poing pour vous projetter dans les airs."],
        ["BIGBANG", 7, 7, "Envoie un rayon de bug concentré qui explose à votre contact."],
        ["PING OF DEATH", 15, 8, "Meca Shipper vous emporte dans les airs avant de vous écraser au sol."],
        ["UPPERCUT", 5, 5, "Eren Shipper lache son meilleur uppercut à la Conor McGregor"],
        ["DRAIN TITANO", 6, 7, "Eren Shipper draine votre essence vitale."],
        ["ADAMENTIUM", 25, 11, "Eren Shipper pose un bouclier autour de lui."],
        ["COUP DE BRANCHE", 6, 6, "Pumpkins Shipper lance une branche"],
        ["LANCER DE GRAINES", 8, 7, "Pumpkins Shipper tournoie et projette rapidement des graines."],
        ["ATTAQUE DE CORBEAUX", 18, 8, "Plusieurs corbeaux sortent de la tête de Pumpkins Shipper et fonce droit sur vous"],
        ["PAY ME A RING", 5, 7, "Shipper Lone Bride effectue une courte ruée avant de vous attaquer"],
        ["MEET MOTHER-IN-LAW", 6, 7, "Shipper Lone Bride envoye un clone dans votre direction qui explose à votre contact"],
        ["MARRY ME", 15, 8, "Shipper Lone Bride ordonne à sa bague d'émettre une onde de choc, vous projetant directement proches de celle-ci"],
        ["CLE DE BRAS", 4, 6, "Drip shipper vous plaques au sol et vous maitrise rapidement"],
        ["SWAGGY", 6, 7, "Drip Shipper se cache dans votre corps, infligeant des dégâts quand il ressort."],
        ["DOIG DRIP", 13, 9, "Drip Shipper ravage la zone devant lui avant de se téléporter derrière vous"]
    ]
    return monster_spells
#liste bidimensionnelle incluant le nom des monstres + infos asci + position des indices d'attaques + chance de drop un objet après l'avoir tué
def monster():
    monster_stats = [
        #[NOM, PV, Indice ASCII, Indice ATT1, Indice Att2, Indice ULTI, Tx de drop]
        ["MECA SHIPPER", 26, 0, 0, 1, 2, 25],
        ["EREN SHIPPER", 17, 1, 3, 4, 5, 10],
        ["PUMPKINS SHIPPER", 23, 2, 6, 7, 8, 15],
        ["SHIPPER LONE BRIDE", 31, 3, 9, 10, 11, 50],
        ["DRIP SHIPPER", 41, 4, 12, 13, 14, 5]
    ]
    return monster_stats



# Section spéciale pour le boss (attaques et liste du boss)
#Stat BOSS FINAL
def boss_monster():
    # [NOM, PV, indices des attaques (,,,) 0 à 4]
    boss = ["Living Dead Mammoth",70,0,1,2,3]
    return boss

def boss_monster_attacks():
    # [Nom Attaque, DEGATS, Tx CRIT, Description]
    boss_attacks = [
        ['FIRE CLEANER',5,8, "Living Dead Mammoth tournoye en flamme et vous aspire vers le feu."], #boss_attacks[0][0] => name of the attack 
        ['EAU DE GLACE',6,9, "Living Dead Mammoth vous asperge d'eau et vous immobilise dans de la glace"],  #boss_attacks[1][0] => idem for this attack
        ['GORGOGNE POWER',8,11,"Living Dead Mammoth a le pouvoir de la Gorgogne: si vous croisez son regard, vous êtes changé en pierre"],
        ['HELL RIFT',10,15,"Une faille vers l'Enfer s'ouvre sous vos pieds, vous êtes attaqués par des démons, fuyez !"],
    ]
    return boss_attacks
