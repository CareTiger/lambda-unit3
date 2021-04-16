# SQLite Read Queries
GET_charactercreator_characters = """
    SELECT * FROM charactercreator_character;
    """

# SQLite Queries
GET_CHARACTER_TABLE = """
    SELECT *
    FROM charactercreator_character;
    """

GET_ITEM_TABLE = """
    SELECT ai.name as item_name
    FROM (SELECT *
    FROM charactercreator_character as cc_char
    INNER JOIN charactercreator_character_inventory as cc_ci
    WHERE cc_char.character_id = cc_ci.character_id) as char_ci
    INNER JOIN armory_item as ai
    WHERE ai.item_id = char_ci.item_id
    AND char_ci.name = {};
    """
    
GET_WEAPON_TABLE = """
    SELECT aw_ai.name
    FROM (SELECT *
    FROM armory_item as ai
    INNER JOIN armory_weapon as aw
    WHERE ai.item_id = aw.item_ptr_id) as aw_ai
    INNER JOIN (SELECT *
    FROM charactercreator_character as cc_char
    INNER JOIN charactercreator_character_inventory as  cc_ci
    WHERE cc_char.character_id = cc_ci.character_id) as char_ci
    WHERE aw_ai.item_id = char_ci.item_id;
    """    