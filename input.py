def get_action():

    while True:
        try:
            print("1 - Attack")
            print("2 - Focus")

            option = int(input("Choose an option: "))
            
            if option in (1, 2):
                return option
            
            print("Choose a valid option.")

        except ValueError:
            print("Please enter a number.")