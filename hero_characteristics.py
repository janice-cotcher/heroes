# game characters
heroes = {
         "Batman": {"identity": "Bruce Wayne", "power": "martial arts",
                    "health points": 150},
         "Wonder Woman": {"identity": "Diana Prince",
                          "power": "super strength",
                          "health points": 200},
         "The Flash": {"identity": "Barry Allen", "power": "super speed",
                       "health points": 90}
         }

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
# dictionary of DC heroes and their vehicles. Nested set for Batman
# to account for multiple vehicles
vehicles = {"Wonder Woman": "Invisible Plane",
            "The Flash": None,
            # Batman has a nested set of vehicles
            "Batman": {"Tumbler", "Batmobile", "The Bat", "Batpod"}
            }


def hero(dictionary, hero):
    """print out the characters with their characteristics"""
    # for hero in dictionary:
    i = dictionary[hero]["identity"]
    p = dictionary[hero]["power"]
    hp = dictionary[hero]["health points"]
    print(f"{hero}'s secret identity is {i}")
    print(f"{hero}'s super power is {p}")
    print(f"{hero} has {hp} health points")
    print("\n")


def hero_inventory(inventory, hero):
    """print out the inventory for the choosen character, along with the
    characteristics of each item"""
    print(f"{hero}'s Inventory:")
    for item in inventory:
        print(f"* {item}")
        for characteristics in inventory[item]:
            detail = inventory[item][characteristics]
            print(f"   {characteristics}: {detail}")
    print("\n")


def hero_vehicle(vehicles):
    """print a list of the hero's vehicles"""
    for heroes in vehicles:
        vehicle = vehicles[heroes]
        # we need a nested loop for Batman because he has multiple vehicles
        if heroes == "Batman":
            batvehicles = vehicles["Batman"]
            print(f"{heroes}'s vehicles:")
            for results in batvehicles:
                print(f"* {results}")
        else:
            print(f"{heroes}'s vehicles:")
            print(f"* {vehicle}")
        print("\n")

#
# hero()
# hero_inventory()
# hero_vehicle()
