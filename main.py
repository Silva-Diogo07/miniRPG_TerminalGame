from Characters.enemy import Enemy
from Characters.player import Player
from inputs import get_player_name
from utilities import clear_console, pause, print_section, show_battle_status, welcome_game_message, welcome_player, play_game


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

    print_section(f"Battle Start: {player.name} vs {enemy.name}")
    show_battle_status(player, enemy)
    pause(1.5)
    clear_console()

    play_game(player, enemy)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nGame closed by user.")