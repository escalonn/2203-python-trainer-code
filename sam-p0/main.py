import menu

def main() -> None:
    display = """
|******************************
|Welcome to SQL Dungeon
|******************************
|Press 1 to Start New Game
|******************************
|Press 2 to Continue
|******************************
|Press 3 to Edit Character
|******************************
|Press 4 to Delete Character
|******************************
|Press 5 to Show All Characters
|******************************
|Press 6 to View a Character Sheet
|******************************
|Press 7 to Create a New Character
|******************************
|"""
    print(display)

    selection = None
    while not selection or not (1 <= selection <= 7):
        try:
            selection = int(input())
        except ValueError:
            print('\nInvalid input, try again\n')
    print('success')

    menu.first_selection(selection)

main()
