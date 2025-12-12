#Name:
#Class: 5th Hour
#Assignment: Semester Project 1

import random
import time

#Due to weird time travelling circumstances beyond explanation, you find yourself in 2018 or so
#working for Larian Studios. Currently, they are working on the early prototypes of the hype
#upcoming game "Baldur's Gate 3". BG3 is a game that uses the Dungeons & Dragons 5th edition rules
#as its framework for gameplay. You have been given a basic dictionary of some of the main hero
#characters and some of the enemies they may face, and are tasked with making an early prototype
#of one of the party members fighting against an enemy until one of them hits zero HP (dies).

partyDict = {
    "LaeZel" : {
        "HO" : 48,
        "Init" : 1,
        "AC" : 17,
        "AtkMod": 6,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 3
    },
    "Shadowheart" : {
        "HP" : 40,
        "Init" : 1,
        "AC" : 18,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 3,
    },
    "Gale" : {
        "HP" : 32,
        "Init" : 1,
        "AC" : 14,
        "AtkMod": 6,
        "Damage" : random.randint(1,10) + random.randint(1,10),
    },
    "Astarion" : {
        "HP" : 40,
        "Init" : 3,
        "AC" : 14,
        "AtkMod": 5,
        "Damage" : random.randint(1,8) + random.randint(1,6) + 4,
    }
}

enemyDict = {
    "Goblin" : {
        "HP" : 7,
        "Init" : 0,
        "AC" : 12,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 2
    },
    "Orc": {
        "HP" : 15,
        "Init": 1,
        "AC" : 13,
        "AtkMod": 5,
        "Damage" : random.randint(1,12) + 3
    },
    "Troll": {
        "HP" : 84,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 4
    },
    "Mindflayer": {
        "HP" : 71,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + 4
    },
    "Dragon": {
        "HP" : 127,
        "Init": 2,
        "AC" : 18,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4
    },
}

#Combat consists of these steps:

#1. Rolling for 'initiative' to see who goes first. This is determined by rolling a
#20-sided die (d20) and adding their initiative modifier (If the roll is the same,
#assume the hero goes first).
player1num = random.randint(1,20) + (partyDict["Shadowheart"]["Init"])
print(f"Shadowheart: {player1num}")
time.sleep(0.7)
player2num = random.randint(1,20) + (enemyDict["Troll"]["Init"])
print(f"Troll: {player2num}")

if player1num >= player2num:
    print("Shadowheart goes first!")
    HeroFirst = True
else:
    print("Troll goes first!")
    HeroFirst = False


#2. Rolling to attack. This is determined by rolling a 20-sided die (d20) and adding their
#attack modifier. The attack hits if it matches or is higher than the target's Armor Class (AC).
#If the d20 rolled to attack is an unmodified ("natural") 20, the attack automatically hits and
#the character deals double damage. If the d20 rolled to attack is an unmodified ("natural") 1,
#the attack automatically misses
while partyDict["Shadowheart"]["HP"] > 0 and enemyDict["Troll"]["HP"] > 0:
    if HeroFirst == True:
        d20 = random.randint(1, 20)
        if d20 == 20:
            enemyDict["Troll"]["HP"] -= (partyDict["Shadowheart"]["Damage"] * 2)
            print(f"Shadowheart Attack hits troll for {(partyDict["Shadowheart"]["Damage"] * 2)} damage with double damage")
            print(enemyDict["Troll"]["HP"])
            time.sleep(0.7)
        elif d20 == 1:
            print("Shadowheart rolled a natural 1 and missed her attack!")
        elif d20 + partyDict["Shadowheart"]["AtkMod"] >= enemyDict["Troll"]["AC"]:
            print(f"Shadowheart Attack hits troll for {(partyDict["Shadowheart"]["Damage"])} damage")
            enemyDict["Troll"]["HP"] -= (partyDict["Shadowheart"]["Damage"])
            print(enemyDict["Troll"]["HP"])
            time.sleep(0.7)
        else:
            print("Shadowheart missed her attack")

        d20_1 = random.randint(1, 20)
        if d20_1 == 20:
            print(f"Troll Attack hits Shadowheart for {enemyDict["Troll"]["Damage"] * 2} damage with double damage")
            partyDict["Shadowheart"]["HP"] -= enemyDict["Troll"]["Damage"] * 2
            print(partyDict["Shadowheart"]["HP"])
            time.sleep(0.7)
        elif d20 == 1:
                print("Troll rolled a natural 1 and missed his attack!")
        elif d20_1 + enemyDict["Troll"]["AtkMod"] >= partyDict["Shadowheart"]["AC"]:
            print(f"Troll Attack hits Shadowheart for {enemyDict["Troll"]["Damage"]} damage")
            partyDict["Shadowheart"]["HP"] -= enemyDict["Troll"]["Damage"]
            print(partyDict["Shadowheart"]["HP"])
            time.sleep(0.7)
        else:
            print("Troll missed his attack!")
    else:
        d20_1 = random.randint(1, 20)
        if d20_1 == 20:
            print(f"Troll Attack hits Shadowheart for {enemyDict["Troll"]["Damage"] * 2} damage with double damage")
            partyDict["Shadowheart"]["HP"] -= enemyDict["Troll"]["Damage"] * 2
            print(partyDict["Shadowheart"]["HP"])
            time.sleep(0.7)
        elif d20 == 1:
                print("Troll rolled a natural 1 and missed his attack!")
        elif d20_1 + enemyDict["Troll"]["AtkMod"] >= partyDict["Shadowheart"]["AC"]:
            print(f"Troll Attack hits Shadowheart for {enemyDict["Troll"]["Damage"]} damage")
            partyDict["Shadowheart"]["HP"] -= enemyDict["Troll"]["Damage"]
            print(partyDict["Shadowheart"]["HP"])
            time.sleep(0.7)
        else:
            print("Troll missed his attack!")

        d20 = random.randint(1, 20)
        if d20 == 20:
            enemyDict["Troll"]["HP"] -= (partyDict["Shadowheart"]["Damage"] * 2)
            print(
                f"Shadowheart Attack hits troll for {(partyDict["Shadowheart"]["Damage"] * 2)} damage with double damage")
            print(enemyDict["Troll"]["HP"])
            time.sleep(0.7)
        elif d20 == 1:
            print("Shadowheart rolled a natural 1 and missed her attack!")
        elif d20 + partyDict["Shadowheart"]["AtkMod"] >= enemyDict["Troll"]["AC"]:
            print(f"Shadowheart Attack hits troll for {(partyDict["Shadowheart"]["Damage"])} damage")
            enemyDict["Troll"]["HP"] -= (partyDict["Shadowheart"]["Damage"])
            print(enemyDict["Troll"]["HP"])
            time.sleep(0.7)
        else:
            print("Shadowheart missed her attack")

else:
    if partyDict["Shadowheart"]["HP"] <= 0:
        print("Shadowheart died in action! Troll has won!")
    else:
        print("Troll has died! Shadowheart has won!")

#3. If the attack hits, roll damage and subtract it from the target's hit points.

#4. The second in initiative rolls to attack (and rolls damage) afterwards.

#5. Repeat steps 2-5 until one of the characters is dead.
