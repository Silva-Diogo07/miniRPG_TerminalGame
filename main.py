import random

from Characters.enemy import Enemy
from Characters.player import Player
from inputs import get_player_name
from utilities import *

def main():
    
    player = Player()
    enemy = Enemy.create_random_enemy()

    clear_console()

    print("Welcome to my RPG game")
    pause(1.25)

    clear_console()

    player.name = get_player_name()
    print(f"Welcome {player.name}")

    pause(1.25)
    clear_console()
    print(f"Debug: enemy spawned is {enemy.name}")
    pause(2.5)

    attacker = random.choice([player, enemy])

    print(f"First to attack will be: {attacker.name} (player)")
    pause(1)

    defender = enemy if attacker is player else player

    clear_console()

    # game loop
    while player.is_alive() and enemy.is_alive():
        
        attack_result = attacker.attack(defender)
        print(attack_result)

        attacker, defender = defender, attacker

        pause(2.5)
        clear_console()

    
    if not player.is_alive():
        print("Enemy won")
    else:
        print("Player won")
    
    pause(1.5)
    return


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nGame closed by user.")