formations = {
    "4-3-3": ["GK", "D", "D", "D", "D", "MID", "MID", "MID", "ST", "ST", "ST"],
    "4-4-2": ["GK", "D", "D", "D", "D", "MID", "MID", "MID", "MID", "ST", "ST"],
    "4-2-3-1": ["GK", "D", "D", "D", "D", "DM", "DM", "AM", "AM", "AM", "ST"],
    "3-4-3": ["GK", "D", "D", "D", "MID", "MID", "MID", "MID", "ST", "ST", "ST"],
    "3-5-2": ["GK", "D", "D", "D", "MID", "MID", "MID", "MID", "MID", "ST", "ST"],
    "5-3-2": ["GK", "D", "D", "D", "D", "D", "MID", "MID", "MID", "ST", "ST"],
    "5-4-1": ["GK", "D", "D", "D", "D", "D", "MID", "MID", "MID", "MID", "ST"]
}


# List of formation names
formation_names = list(formations.keys())


# Function to display the menu
def show_menu():
    print("\n==============================")
    print(" FOOTBALL FORMATION EXPLORER")
    print("==============================")

    for number, name in enumerate(formation_names, 1):
        print(number, ".", name)

    print("Q. Exit")


# Function to show a formation
def show_formation(name):

    print("\n------------------------------")
    print("FORMATION:", name)
    print("------------------------------")

    players = formations[name]

    # Outer loop
    for position in ["GK", "D", "MID", "DM", "AM", "ST"]:

        line = []

        # Inner loop
        for player in players:

            if player == position:
                line.append(player)

        if len(line) > 0:
            print(" ".join(line))


# Main program
while True:

    show_menu()

    choice = input("\nChoose a formation: ")

    # Exit
    if choice.lower() == "q":
        print("\nThank you for using Football Formation Explorer!")
        break

    # Check if user entered a number
    if choice.isdigit():

        number = int(choice)

        if number >= 1 and number <= len(formation_names):

            selected = formation_names[number - 1]

            show_formation(selected)

        else:
            print("Invalid number.")

    # Check if user entered a formation name
    elif choice in formations:

        show_formation(choice)

    else:
        print("Invalid formation.")
