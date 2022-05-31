import python_code.dnd_character_sheet.ability_modifier_calc as ability_modifier

dnd_dice = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']


class CharAbilityRaw:
    str_ability = 0
    dex_ability = 0
    con_ability = 0
    int_ability = 0
    wis_ability = 0
    cha_ability = 0


class CharModifier:
    str_modifier = ability_modifier.ability_score(CharAbilityRaw.str_ability)
    dex_modifier = ability_modifier.ability_score(CharAbilityRaw.dex_ability)
    con_modifier = ability_modifier.ability_score(CharAbilityRaw.con_ability)
    int_modifier = ability_modifier.ability_score(CharAbilityRaw.int_ability)
    wis_modifier = ability_modifier.ability_score(CharAbilityRaw.wis_ability)
    cha_modifier = ability_modifier.ability_score(CharAbilityRaw.cha_ability)


class CharMainStats:
    hit_dice = 'd6'
    hit_points = 0
    character_level = 1
    armor_class = 10 + CharModifier.dex_modifier
    speed = 30
    prof_bonus = 2
    passive_perception = 10 + CharModifier.wis_modifier
    spell_attack = prof_bonus + CharModifier.int_modifier
    spell_dc = 8 + prof_bonus + CharModifier.int_modifier
    attack_modifier = 0


class CharSaving:
    str_saving = CharModifier.str_modifier
    dex_saving = CharModifier.dex_modifier
    con_saving = CharModifier.con_modifier
    int_saving = CharModifier.int_modifier + CharMainStats.prof_bonus
    wis_saving = CharModifier.wis_modifier + CharMainStats.prof_bonus
    cha_saving = CharModifier.cha_modifier


class CharSkills:
    acrobatics = CharModifier.dex_modifier
    animal_handling = CharModifier.dex_modifier
    arcana = CharModifier.int_modifier + CharMainStats.prof_bonus
    athletics = CharModifier.str_modifier
    deception = CharModifier.cha_modifier
    history = CharModifier.int_modifier
    insight = CharModifier.wis_modifier
    intimidation = CharModifier.cha_modifier
    investigation = CharModifier.int_modifier + CharMainStats.prof_bonus
    medicine = CharModifier.wis_modifier
    nature = CharModifier.int_modifier
    perception = CharModifier.wis_modifier
    performance = CharModifier.cha_modifier
    persuasion = CharModifier.cha_modifier
    religion = CharModifier.int_modifier
    sleight_of_hand = CharModifier.dex_modifier
    survival = CharModifier.wis_modifier
