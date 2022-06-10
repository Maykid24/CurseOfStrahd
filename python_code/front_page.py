"""This page will serve as the forefront of the python scripts to be easily available during DnD campaign.
   Will also update this page so the user may choose very quickly what they are trying to do without slowing down the
   group."""

import random

import python_code.dnd_character_sheet.dnd_attributes as dnd_attributes

from python_code.lists.main_page_lists import main_list
from python_code.lists.main_page_lists import dnd_attribute_list
from python_code.lists.main_page_lists import dnd_dice


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

    proceed = input("Would you want to see another attribute or go back? ").lower()

    if proceed == 'yes':
        stats()
    elif proceed == 'back':
        front_page_def()
    else:
        print('Run away!!!!!')


def health_points():
    base_hp = [dnd_attributes.CharMainStats.get('hit_points')]
    while True:
        user_input = input('Do you want to Add or Sub from HP or Stop/Back? ').lower()
        if user_input == 'add':
            add_hp = int(input('How much would you like to add? '))
            new_hp = base_hp[-1] + add_hp
            base_hp.append(new_hp)
            print(base_hp[-1])
        elif user_input == 'sub':
            sub_hp = int(input('How much would you like to sub? '))
            new_hp = base_hp[-1] - sub_hp
            base_hp.append(new_hp)
            print(base_hp[-1])
        elif user_input == 'stop':
            print(base_hp[-1])
            print("Goodbye")
            break
        elif user_input == 'back':
            front_page_def()
        else:
            break


def spell_count():
    for key, value in dnd_attributes.CharSpells.items():
        print(key, sep='\n')
    new_spell_dict = dict((k.lower(), v) for k, v in dnd_attributes.CharSpells.items())
    while True:
        spell_input = input("Which spell would you like to use? Would you like to see the Values? Or would you like "
                            "to reset/go back? ").lower()
        if spell_input in new_spell_dict:
            print(new_spell_dict[spell_input])
            if new_spell_dict[spell_input] == 0:
                print("Out of spells for this level")
            else:
                new_spell_dict[spell_input] -= 1
                print(new_spell_dict[spell_input])
        elif spell_input == 'values':
            for key, value in new_spell_dict.items():
                print(key + ': ', value)
        elif spell_input == 'reset':
            new_spell_dict = dict((k.lower(), v) for k, v in dnd_attributes.CharSpells.items())
        elif spell_input == 'back':
            front_page_def()
        else:
            break


def roll_dice():
    dice = input("What would you like to roll? d4, d6, d8, d10, d12, d20, or a d100? ")
    while dice not in dnd_dice:
        print("Please enter one of the following dice: d4, d6, d8, d10, d12, d20, d100")
        dice = input("Please enter dnd dice: ")
    print("Rolling...")
    die = int(dice[1:])
    roll = random.randint(1, die)
    print(roll)

    proceed = input("Would you like to roll another set or go back? ").lower()

    if proceed == "yes":
        dice_input()
    elif proceed == "back":
        front_page_def()
    else:
        print("Good Luck")


def roll_many_dice():
    while True:
        try:
            dice_number = int(input("How many dice would you like to roll: "))
            break
        except ValueError:
            print("Please enter a valid number")
    dice = input("What would you like to roll? d4, d6, d8, d10, d12, d20, or a d100? ")
    while dice not in dnd_dice:
        print("Please enter one of the following dice: d4, d6, d8, d10, d12, d20, d100")
        dice = input("Please enter dnd dice: ")
    die = int(dice[1:])
    individual_dice = []
    sum_roll = 0
    for i in range(int(dice_number)):
        roll = random.randint(1, die)
        individual_dice.append(roll)
        sum_roll = sum_roll + roll
    print(*individual_dice, sep=', ')
    print("Overall Total: ", sum_roll)

    proceed = input("Would you like to roll another set or back? ").lower()

    if proceed == "yes":
        dice_input()
    elif proceed == "back":
        front_page_def()
    else:
        print("Good Luck")


def dice_input():
    while True:
        user_results = input("Are you looking to roll "'"many"'" dice, or "'"single"'" dice? ").lower()
        if user_results == "single":
            roll_dice()
        elif user_results == "many":
            roll_many_dice()
        break


def front_page_def():
    print(*main_list, sep=', ')
    user_input = input('What would you like to do? ')
    if user_input == 'attributes':
        stats()
    elif user_input == 'health points':
        health_points()
    elif user_input == 'spells':
        spell_count()
    elif user_input == 'dice roll':
        dice_input()


front_page_def()
