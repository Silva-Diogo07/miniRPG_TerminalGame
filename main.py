from Characters.enemy import Enemy
from Characters.player import Player
from inputs import get_player_name
from utilities import *

def main():
    
    player = Player()
    enemy = Enemy.create_random_enemy()

    clear_console()

    welcome_game_message()

    clear_console()

    player.name = get_player_name()
    welcome_player(player.name)
    pause(1.5)

    clear_console()

    attacker = get_first_attacker(player, enemy)
    defender = enemy if attacker is player else player

    clear_console()

    # game loop
    while player.is_alive() and enemy.is_alive():
        
        attack_result = attacker.attack(defender)
        print(attack_result)

        attacker, defender = defender, attacker

        pause(2.5)
        clear_console()

    check_winner(player)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nGame closed by user.")