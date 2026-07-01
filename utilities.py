import os
import random
import time

from inputs import get_player_action


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause(seconds: float):
    time.sleep(seconds)


def print_section(title):
    print("\n" + "=" * 24)
    print(title)
    print("=" * 24)


def welcome_game_message():
    print("Welcome to the terminal RPG adventure!")
    pause(2.0)


def welcome_player(player_name):
    print(f"Welcome, {player_name}!")
    print("Prepare yourself for the fight ahead.\n")


def get_first_attacker(player, enemy):
    attacker = random.choice([player, enemy])

    if attacker is player:
        print(f"You will take the first turn")
    else:
        print(f"{attacker.name} take's the first turn")
    pause(1.5)

    return attacker


def check_winner(player):
    if not player.is_alive():
        print("\nDefeat. The enemy has defeated you.")
    else:
        print("\nVictory! You defeated your opponent.")

    pause(2.0)


def format_battle_status(player, enemy):
    return (
        f"{player.name} | HP: {player.hp}/{player.max_hp} | Stamina: {player.stamina}\n"
        f"{enemy.name} | HP: {enemy.hp}/{enemy.max_hp} | Stamina: {enemy.stamina}"
    )


def show_battle_status(player, enemy):
    print_section("Battle Status")
    print(format_battle_status(player, enemy))
    print()


def play_game(player, enemy):
    while player.is_alive() and enemy.is_alive():
        clear_console()
        show_battle_status(player, enemy)
        pause(1.5)

        attacker = get_first_attacker(player, enemy)
        defender = enemy if attacker is player else player
        while player.is_alive() and enemy.is_alive():
            if attacker is player:
                action = get_player_action()
                match action:
                    case "attack":
                        result = player.attack(defender)
                    case "special attack":
                        result = player.special_attack(defender)
                    case "heal":
                        result = player.heal()
                    case "defend":
                        result = player.defend_attack()
                    case _:
                        result = "Invalid option"
                print(result)
            else:
                result = attacker.attack(defender)
                print(result)

            attacker, defender = defender, attacker
            pause(3.5)
            clear_console()

    check_winner(player)