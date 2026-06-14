import time
import random

from Characters.character import Character
from utilities import clear_console

player = Character("Player", 100, 10, "Melee")
enemy = Character("Enemy", 75, 20, "Axe")

def main():

    clear_console()

    print("Welcome to RPG console mini game")

    time.sleep(1.5)

    clear_console()

    print("First to attack will be ...")

    time.sleep(1.25)

    attacker = random.choice([player, enemy])

    clear_console()

    print(attacker.name)
    time.sleep(1)

    defender = enemy if attacker == player else player

    clear_console()

    while player.hp > 0 and enemy.hp > 0:

        # todo : implement dodge in the Character class instead of locally

        dodged = random.choice([True, False])

        if dodged:
            print(f"{defender.name} dodged the attack!")
        else:
            attacker.attack(defender)
            print(f"{attacker.name} attacked {defender.name}")
        
        print(f"{defender.name} HP remaining: {defender.hp}")

        attacker, defender = defender, attacker

        time.sleep(1.5)
        clear_console()

    if player.hp <= 0:
        print("Enemy won")
        time.sleep(1)
        return 0
    else:
        print("Player won")
        time.sleep(1)
        return 0    

if __name__ == "__main__":
    main()