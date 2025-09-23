#Name:
#Class: 5th Hour
#Assignment: Scenario 1
import time

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.

print("Hello World!")

Creatures = {
    "Creature_1" : {
        "Class" : "Support",
        "Damage" : 10,
        "Cooldown" : 20
    },
    "Creature_2" : {
        "Class" : "Entry",
        "Damage" : 40,
        "Cooldown" : 50,
    },
    "Creature_3" : {
        "Class" : "Support",
        "Damage" : 25,
        "Cooldown" : 30
    },
    "Creature_4": {
        "Class": "Anchor",
        "Damage" : 80,
        "Cooldown" : 75
    },
    "Creature_5": {
        "Class": "Intel",
        "Damage" : 35,
        "Cooldown" : 35
    },
}

enemy_Damage = 0
print(f"enemys current damage {enemy_Damage}")
enemy_Damage = enemy_Damage + Creatures["Creature_1"]["Damage"]
print(f"Creature 1 Has attacked enemy. Your current damage is {enemy_Damage}")
enemy_Damage = enemy_Damage + Creatures["Creature_2"]["Damage"]
print(f"Creature 2 Has attacked enemy. Your current damage is {enemy_Damage}")
enemy_Damage = enemy_Damage + Creatures["Creature_3"]["Damage"]
print(f"Creature 3 Has attacked enemy. Your current damage is {enemy_Damage}")
enemy_Damage += Creatures["Creature_4"]["Damage"]
print(f"Creature 4 Has attacked enemy. Your current damage is {enemy_Damage}")
print("You have died and the 5th creature is about to mutulate your body!")
time.sleep(5)
enemy_Damage += Creatures["Creature_5"]["Damage"]
print(f"Creature 5 Has attacked enemy. Your current damage is {enemy_Damage}")
