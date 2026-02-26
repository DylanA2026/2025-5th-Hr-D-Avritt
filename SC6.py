#Name:
#Class: 5th Hour
#Assignment: Scenario 6

import random
import time
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Semester Project 1 using classes instead of dictionaries, include and refactor
#the combat test code below as well.)

class Character:
    def __init__(self,HP, Init, AC, AtkMod, Damage):
        self.HP = HP
        self.Init = Init
        self.AC = AC
        self.AtkMod = AtkMod
        self.Damage = Damage

def rolling():
        player1num = random.randint(1, 20) + Shadowheart.Init
        print(f"Shadowheart: {player1num}")
        time.sleep(0.7)
        player2num = random.randint(1, 20) + Troll.Init
        print(f"Troll: {player2num}")

        if player1num >= player2num:
            print("Shadowheart goes first!")
            Partyattack()
        else:
            print("Troll goes first!")
            Enemyattack()

def Partyattack():
    while Shadowheart.HP > 0 and Troll.HP > 0:

        d20 = random.randint(1, 20)
        if d20 == 20:
            Troll.HP -= (Shadowheart.Damage * 2)
            print(f"Shadowheart Attack hits troll for {(Shadowheart.Damage * 2)} damage with double damage")
            print(Troll.HP)
            time.sleep(0.7)
            Enemyattack()

        elif d20 == 1:
            print("Shadowheart rolled a natural 1 and missed her attack!")
            Enemyattack()
        elif d20 + Shadowheart.AtkMod >= Troll.AC:
            print(f"Shadowheart Attack hits troll for {(Shadowheart.Damage)} damage")
            Troll.HP -= (Shadowheart.Damage)
            print(Troll.HP)
            time.sleep(0.7)
            Enemyattack()
        else:
            print("Shadowheart missed her attack")
            Enemyattack()
    else:
        if Shadowheart.HP <= 0:
            print("Shadowheart died in action! Troll has won!")
            exit()
        else:
            print("Troll has died! Shadowheart has won!")
            exit()


def Enemyattack():
        while Shadowheart.HP > 0 and Troll.HP > 0:
            d20_1 = random.randint(1, 20)
            if d20_1 == 20:
                print(f"Troll Attack hits Shadowheart for {Troll.Damage * 2} damage with double damage")
                Shadowheart.HP -= Troll.Damage * 2
                print(Shadowheart.HP)
                time.sleep(0.7)
                Partyattack()
            elif d20_1 == 1:
                print("Troll rolled a natural 1 and missed his attack!")
                Partyattack()
            elif d20_1 + Troll.AtkMod >= Shadowheart.AC:
                print(f"Troll Attack hits Shadowheart for {Troll.Damage} damage")
                Shadowheart.HP -= Troll.Damage
                print(Shadowheart.HP)
                time.sleep(0.7)
                Partyattack()
            else:
                print("Troll missed his attack!")
                Partyattack()
        else:
            if Shadowheart.HP <= 0:
                print("Shadowheart died in action! Troll has won!")
                exit()
            else:
                print("Troll has died! Shadowheart has won!")
                exit()
#Party Characters
LaeZel = Character(48,1,17,6, random.randint(1,6) + random.randint(1,6) + 3)
Shadowheart = Character(40,1,18,4, random.randint(1,6) + 3)
Gale = Character(32,1,14,6,random.randint(1,10) + random.randint(1,10))
Astraion = Character(40,3,14,5,random.randint(1,8) + random.randint(1,6) + 4)

#Enemy Characters
Goblin = Character(7,0,12,4,random.randint(1,6) + 2)
Orc = Character(15,1,13,5,random.randint(1,12) + 3)
Troll = Character (84,1,15,7,random.randint(1,6) + random.randint(1,6) + 4)
Mindflayer = Character(71,1,15,7,random.randint(1,10) + random.randint(1,10) + 4)
Dragon = Character(127,2,18,7,random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4)


rolling()