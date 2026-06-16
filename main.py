import time
import random

from Characters.character import Character
from input import get_action
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

        # verify if player is attacker
        # check player action

        if attacker is player:
            player_action = get_action()

            if player_action == 1:
                print(f"{attacker.name} attacked {defender.name}")
                print(attacker.attack(defender))

            elif player_action == 2:
                print(f"{attacker.name} is focused...")
                attacker.focus()
        
        else:
            print(f"{attacker.name} attacked {defender.name}")
            print(attacker.attack(defender))

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