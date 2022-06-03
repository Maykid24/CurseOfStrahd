"""This function page will serve as functions to get the character sheet up and running"""
import python_code.dnd_character_sheet.Ability_Modifier_Calc
import python_code.dnd_character_sheet.dnd_attributes as dnd_attributes
from python_code.lists.dnd_attribute_list import dnd_attribute_list

print(*dnd_attribute_list, sep=', ')
user_input = input("What would you like to see: ").lower()


if user_input == 'ability raw':
    for key, value in dnd_attributes.CharAbilityRaw.items():
        print(key, ':', value)
elif user_input == 'main stats':
    for key, value in dnd_attributes.CharMainStats.items():
        print(key, ':', value)
elif user_input == 'modifier':
    for key, value in dnd_attributes.CharModifier.items():
        print(key, ':', value)
elif user_input == 'secondary stats':
    for key, value in dnd_attributes.CharSecondaryStats.items():
        print(key, ':', value)
elif user_input == 'saves':
    for key, value in dnd_attributes.CharSaving.items():
        print(key, ':', value)
elif user_input == 'skills':
    for key, value in dnd_attributes.CharSkills.items():
        print(key, ':', value)
else:
    print('Please enter a valid answer')
