import python_code.dnd_character_sheet.Ability_Modifier_Calc as Ability_Modifier

dnd_dice = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']

EquipmentStats = {
    'cloak_of_protection': 1,
}

CharAbilityRaw = {
    'str_ability': 9,
    'dex_ability': 17,
    'con_ability': 16,
    'int_ability': 20,
    'wis_ability': 12,
    'cha_ability': 12,
}

CharMainStats = {
    'hit_dice': 'd6',
    'hit_points': 35,
    'character_level': 4,
    'speed': 30,
    'blade_speed': 40,
    'prof_bonus': 2,
    'initiative': 3,
}

CharModifier = {
    'str_modifier': Ability_Modifier.ability_score(CharAbilityRaw.get('str_ability')),
    'dex_modifier': Ability_Modifier.ability_score(CharAbilityRaw.get('dex_ability')),
    'con_modifier': Ability_Modifier.ability_score(CharAbilityRaw.get('con_ability')),
    'int_modifier': Ability_Modifier.ability_score(CharAbilityRaw.get('int_ability')),
    'wis_modifier': Ability_Modifier.ability_score(CharAbilityRaw.get('wis_ability')),
    'cha_modifier': Ability_Modifier.ability_score(CharAbilityRaw.get('cha_ability')),
}

CharSecondaryStats = {
    'armor_class': 12 + CharModifier.get('dex_modifier') + EquipmentStats.get('cloak_of_protection'),
    'blade_armor_class': 12 + CharModifier.get('dex_modifier') + CharModifier.get('int_modifier')
                            + EquipmentStats.get('cloak_of_protection'),
    'passive_perception': 10 + CharModifier.get('wis_modifier') + CharMainStats.get('prof_bonus'),
    'spell_attack': CharMainStats.get('prof_bonus') + CharModifier.get('int_modifier'),
    'spell_dc': 8 + CharMainStats.get('prof_bonus') + CharModifier.get('int_modifier'),
    'attack_modifier_str': CharMainStats.get('prof_bonus') + CharModifier.get('str_modifier'),
    'attack_modifier_dex': CharMainStats.get('prof_bonus') + CharModifier.get('dex_modifier'),
}

CharSaving = {
    'str_saving': CharModifier.get('str_modifier') + EquipmentStats.get('cloak_of_protection'),
    'dex_saving': CharModifier.get('dex_modifier') + EquipmentStats.get('cloak_of_protection'),
    'con_saving': CharModifier.get('con_modifier') + EquipmentStats.get('cloak_of_protection'),
    'int_saving': CharModifier.get('int_modifier') + CharMainStats.get('prof_bonus') + EquipmentStats.get(
        'cloak_of_protection'),
    'wis_saving': CharModifier.get('wis_modifier') + CharMainStats.get('prof_bonus') + EquipmentStats.get(
        'cloak_of_protection'),
    'cha_saving': CharModifier.get('cha_modifier') + EquipmentStats.get('cloak_of_protection'),
}

CharSkills = {
    'acrobatics': CharModifier.get('dex_modifier'),
    'animal_handling': CharModifier.get('dex_modifier'),
    'arcana': CharModifier.get('int_modifier') + CharMainStats.get('prof_bonus'),
    'athletics': CharModifier.get('str_modifier'),
    'deception': CharModifier.get('cha_modifier'),
    'history': CharModifier.get('int_modifier') + CharMainStats.get('prof_bonus'),
    'insight': CharModifier.get('wis_modifier'),
    'intimidation': CharModifier.get('cha_modifier'),
    'investigation': CharModifier.get('int_modifier') + CharMainStats.get('prof_bonus'),
    'medicine': CharModifier.get('wis_modifier'),
    'nature': CharModifier.get('int_modifier'),
    'perception': CharModifier.get('wis_modifier') + CharMainStats.get('prof_bonus'),
    'performance': CharModifier.get('cha_modifier') + CharMainStats.get('prof_bonus'),
    'persuasion': CharModifier.get('cha_modifier'),
    'religion': CharModifier.get('int_modifier'),
    'sleight_of_hand': CharModifier.get('dex_modifier'),
    'stealth': CharModifier.get('dex_modifier'),
    'survival': CharModifier.get('wis_modifier'),
}

CharSpells = {
    'Level 1': 4,
    'Level 2': 3,
    'Level 3': 0,
    'Level 4': 0,
    'Level 5': 0,
    'Level 6': 0,
    'Level 7': 0,
    'Level 8': 0,
    'Level 9': 0,
}
