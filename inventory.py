# inventory paired with characters
inventory = {"Wonder Woman": {"Lasso of Truth":
                              {"description": "extracts truth from people",
                               "damage": 0, "protection": 5},
                              "Bracelets of Submission":
                              {"description": "bulletproof bracelets",
                               "damage": 100, "protection": 50},
                              "Sword of Athena":
                              {"description":
                               "magically-empowered sword wielded",
                               "damage": 500, "protection": 0}},
             "Batman": {"Batarang":
                        {"description": "boomerang shaped like a bat",
                         "damage": 10, "protection": 0},
                        "Grapple hook":
                        {"description": "pear-shooting spring-based device",
                         "damage": 5, "protection": 0},
                        "Sonic Bat Device":
                        {"description":
                         "high frequency emitter allowing the control of bats",
                         "damage": 15, "protection": 100}},
             "The Flash": {"Red suit":
                           {"description":
                            "protection when travelling at super speed",
                            "damage": 0, "protection": 100}}
             }


def player_inventory(player, inventory):
    """Print out the inventory for the choosen character"""
    protection_items = []
    weapons = []
    for item in inventory[player]:
        description = inventory[player][item]["description"]
        damage = inventory[player][item]["damage"]
        protection = inventory[player][item]["protection"]
        print(f"{player}'s {item} - {description}")
        print(f"damage: {damage}")
        print(f"protection: {protection}")
        if protection != 0 and damage == 0:
            protection_items.append(item)
        elif damage != 0:
            weapons.append(item)
    return protection_items, weapons


# player_inventory("The Flash", inventory)
