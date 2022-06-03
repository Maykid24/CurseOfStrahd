"""This page will serve as the forefront of the python scripts to be easily available during DnD campaign.
   Will also update this page so the user may choose very quickly what they are trying to do without slowing down the
   group."""

import python_code.dnd_character_sheet.dnd_attributes as dnd_attributes

from python_code.lists.main_page_lists import main_list
from python_code.lists.main_page_lists import dnd_attribute_list


def stats():
    print(*dnd_attribute_list, sep=', ')
    user_input = input("What would you like to see: ").lower()
    while user_input not in dnd_attribute_list:
        print('Please enter a valid answer')
        user_input = input("What would you like to see: ").lower()
    if user_input == 'ability raw':
        for key, value in dnd_attributes.CharAbilityRaw.items():
            print(key + ':', value)
    elif user_input == 'main stats':
        for key, value in dnd_attributes.CharMainStats.items():
            print(key + ':', value)
    elif user_input == 'modifier':
        for key, value in dnd_attributes.CharModifier.items():
            print(key + ':', value)
    elif user_input == 'secondary stats':
        for key, value in dnd_attributes.CharSecondaryStats.items():
            print(key + ':', value)
    elif user_input == 'saves':
        for key, value in dnd_attributes.CharSaving.items():
            print(key + ':', value)
    elif user_input == 'skills':
        for key, value in dnd_attributes.CharSkills.items():
            print(key + ':', value)
    elif user_input == 'all':
        for key, value in dnd_attributes.CharAbilityRaw.items():
            print(key + ':', value)
        print()
        for key, value in dnd_attributes.CharMainStats.items():
            print(key + ':', value)
        print()
        for key, value in dnd_attributes.CharModifier.items():
            print(key + ':', value)
        print()
        for key, value in dnd_attributes.CharSecondaryStats.items():
            print(key + ':', value)
        print()
        for key, value in dnd_attributes.CharSaving.items():
            print(key + ':', value)
        print()
        for key, value in dnd_attributes.CharSkills.items():
            print(key + ':', value)

    proceed = input("Would you want to see another attribute? ").lower()

    if proceed == 'yes':
        stats()
    elif proceed == 'back':
        front_page_def()
    else:
        print('Run away!!!!!')


def front_page_def():
    print(*main_list)
    user_input = input('What would you like to do? ')
    if user_input == 'attributes':
        stats()


front_page_def()
