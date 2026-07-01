def get_player_name():
    name = input("Choose your character name: ").strip()

    while name == "":
        name = input("Name cannot be empty. Please try again: ").strip()

    return name


def get_player_action():
    options = {
        "1": "attack",
        "2": "special attack",
        "3": "heal",
        "4": "defend",
    }

    while True:
        print("\nChoose your action:")
        print("1 - Attack")
        print("2 - Special Attack")
        print("3 - Heal")
        print("4 - Defend")

        option = input("Enter number [1-4]: ").strip()

        if option in options:
            return options[option]

        print("Please choose a valid action number.")