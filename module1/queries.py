TOTAL_CHARACTERS = """
    SELECT COUNT(*) FROM charactercreator_character;
    """
TOTAL_SUBCLASS = """
    SELECT COUNT(*) FROM charactercreator_necromancer;
    """
TOTAL_ITEMS = """
    SELECT COUNT(*) FROM armory_item;
    """
WEAPONS = """
    SELECT COUNT(*) FROM armory_weapon;
    """
NON_WEAPONS = """
    SELECT
    (SELECT COUNT(*) FROM armory_item) - 
    (SELECT COUNT(*) FROM armory_weapon);
    """
CHARACTER_ITEMS = """
    SELECT character_id, COUNT(id)
	FROM charactercreator_character_inventory
	GROUP BY character_id
	LIMIT 20;
    """
CHARACTER_WEAPONS = """

    """
AVG_CHARACTER_ITEMS = """

    """
AVG_CHARACTER_WEAPONS = """

    """
