from character import Character
from file_database import FileDatabase


def first_selection(selection: int) -> None:
    '''the function'''
    if selection == 1:
        set_up_new_char()
    else:
        print('under construction')


def set_up_new_char() -> None:
    new_char = input('Enter Name of New Character: ')
    new_class = input('Enter Name of Character\'s Class: ')
    new_race = input('Enter your Character\'s Race: ')
    print(
"""
|Choose a Faction:
|Enter 1 for the Alliance
|Enter 2 for the Horde
|""")

    faction = None
    while faction not in [1, 2]:
        try:
            faction = int(input())
        except ValueError:
            print('\nInvalid input, try again\n')

    health = None
    while not health or health < 0:
        try:
            health = int(input('Enter Health: '))
        except ValueError:
            print('\nInvalid input, try again\n')

    char = Character(new_char, health, new_class, new_race, faction)
    db = FileDatabase()
    db.create_character(char)
    db.commit()

    # id = char.getCharId(newChar)
