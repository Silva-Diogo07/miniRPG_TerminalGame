def get_player_name():
    name = input("Enter your character's name: ").strip()

    while name == "":
        name = input("Name cannot be empty. Try again: ").strip()
    
    return name