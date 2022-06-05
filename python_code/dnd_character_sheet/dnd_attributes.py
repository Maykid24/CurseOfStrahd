import python_code.dnd_character_sheet.Ability_Modifier_Calc as Ability_Modifier

dnd_dice = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']


CharAbilityRaw = {
    'str_ability': 9,
    'dex_ability': 17,
    'con_ability': 16,
    'int_ability': 18,
    'wis_ability': 12,
    'cha_ability': 12
}

CharMainStats = {
    'hit_dice': 'd6',
    'hit_points': 9,
    'character_level': 1,
    'speed': 30,
    'prof_bonus': 2,
    'initiative': 3,
    'attack_modifier': 0
}

CharModifier = {
    'str_modifier': Ability_Modifier.ability_score(CharAbilityRaw.get('str_ability')),
    'dex_modifier': Ability_Modifier.ability_score(CharAbilityRaw.get('dex_ability')),
    'con_modifier': Ability_Modifier.ability_score(CharAbilityRaw.get('con_ability')),
    'int_modifier': Ability_Modifier.ability_score(CharAbilityRaw.get('int_ability')),
    'wis_modifier': Ability_Modifier.ability_score(CharAbilityRaw.get('wis_ability')),
    'cha_modifier': Ability_Modifier.ability_score(CharAbilityRaw.get('cha_ability'))
}

CharSecondaryStats = {
    'armor_class': 10 + CharModifier.get('dex_modifier'),
    'passive_perception': 10 + CharModifier.get('wis_modifier'),
    'spell_attack': CharMainStats.get('prof_bonus') + CharModifier.get('int_modifier'),
    'spell_dc': 8 + CharMainStats.get('prof_bonus') + CharModifier.get('int_modifier')
}

CharSaving = {
    'str_saving': CharModifier.get('str_modifier'),
    'dex_saving': CharModifier.get('dex_modifier'),
    'con_saving': CharModifier.get('con_modifier'),
    'int_saving': CharModifier.get('int_modifier') + CharMainStats.get('prof_bonus'),
    'wis_saving': CharModifier.get('wis_modifier') + CharMainStats.get('prof_bonus'),
    'cha_saving': CharModifier.get('cha_modifier')
}

CharSkills = {
    'acrobatics': CharModifier.get('dex_modifier'),
    'animal_handling': CharModifier.get('dex_modifier'),
    'arcana': CharModifier.get('int_modifier') + CharMainStats.get('prof_bonus'),
    'athletics': CharModifier.get('str_modifier'),
    'deception': CharModifier.get('cha_modifier'),
    'history': CharModifier.get('int_modifier'),
    'insight': CharModifier.get('wis_modifier'),
    'intimidation': CharModifier.get('cha_modifier'),
    'investigation': CharModifier.get('int_modifier') + CharMainStats.get('prof_bonus'),
    'medicine': CharModifier.get('wis_modifier'),
    'nature': CharModifier.get('int_modifier'),
    'perception': CharModifier.get('wis_modifier') + CharMainStats.get('prof_bonus'),
    'performance': CharModifier.get('cha_modifier'),
    'persuasion': CharModifier.get('cha_modifier'),
    'religion': CharModifier.get('int_modifier'),
    'sleight_of_hand': CharModifier.get('dex_modifier'),
    'survival': CharModifier.get('wis_modifier')
}
