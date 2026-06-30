def get_player_name():
    name = input("Enter your character's name: ").strip()

    while name == "":
        name = input("Name cannot be empty. Try again: ").strip()
    
    return name

def get_player_action():
    print("1 - Attack")
    print("2 - Special Attack")
    print("3 - Heal")
    print("4 - Defend")

    option = int("Enter the number of the action: ")

    try:
        while 1 > option > 4:
            option = int("Enter the number of a valid action: ")
    
    except ValueError:
        return "That's not a valid input"
    
    match option:
        case 1:
            return "attack"
        case 2:
            return "special attack"
        case 3:
            return "heal"
        case 4:
            return "defend"
        case __:
            return "invalid option"
        
    return option