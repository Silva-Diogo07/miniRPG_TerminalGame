import os
import random
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause(seconds: float):
    time.sleep(seconds)
    

def welcome_game_message():
    print("Welcome to my RPG game")
    pause(1.25)


def welcome_player(player_name):
    print(f"Welcome {player_name}")


def get_first_attacker(player, enemy):
    attacker = random.choice([player, enemy])

    if attacker is player:
        print(f"First to attack will be: {attacker.name} (player)")
    else:
        print(f"First to attack will be: {attacker.name}")
    pause(1)

    return attacker


def check_winner(player):
    if not player.is_alive():
        print("Enemy won")
    else:
        print("Player won")
    
    pause(1.5)
    return


def play_game(player, enemy):
    while player.is_alive() and enemy.is_alive():
        
        attack_result = attacker.attack(defender)
        print(attack_result)

        attacker, defender = defender, attacker

        pause(2.5)
        clear_console()