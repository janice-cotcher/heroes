import sys

# inventory paired with characters
inventory = {"Wonder Woman": {"Lasso of Truth":
                              {"description": "extracts truth from people",
                               "damage": 0, "protection": 5, "healing": 0},
                              "Bracelets of Submission":
                              {"description": "bulletproof bracelets",
                               "damage": 100, "protection": 50, "healing": 0},
                              "Sword of Athena":
                              {"description":
                               "magically-empowered sword wielded",
                               "damage": 500, "protection": 0, "healing": 0},
                              "Purple Ray":
                              {"description":
                               "can heal and rejuvenate the sick and injured",
                               "damage": 0, "protection": 0, "healing": 50}
                              },
             "Batman": {"Batarang":
                        {"description": "boomerang shaped like a bat",
                         "damage": 10, "protection": 0, "healing": 0},
                        "Grapple hook":
                        {"description": "pear-shooting spring-based device",
                         "damage": 5, "protection": 0, "healing": 0},
                        "Sonic Bat Device":
                        {"description":
                         "high-frequency emitter allowing the control of bats",
                         "damage": 15, "protection": 100, "healing": 0},
                        "First Aid Kit":
                        {"description": "kit to heal wounds", "damage": 0,
                         "protection": 0, "healing": 5}
                        },
             "The Flash": {"Red suit":
                           {"description":
                            "protection when travelling at super speed",
                            "damage": 5, "protection": 100, "healing": 0},
                           "First Aid Kit":
                            {"description": "kit to heal wounds", "damage": 0,
                             "protection": 0, "healing": 5}
                           }
             }


def weapons(character, dict):
    """
    Check if an inventory item can cause damage
    Ask for user input for weapon
    """
    defend = []
    for item in dict[character]:
        if dict[character][item]["damage"] != 0:
            defend.append(item)
    print("\n" * 2)
    print("Available Weapons:")
    if len(defend) == 0:
        print("You have no weapons available")
        print("\n" * 2)
    else:
        for weapon in defend:
            print(f"* {weapon}")
        weapon_input = input("Which weapon would you like to use?")
        print("\n" * 2)
        if weapon_input in defend:
            print(f"Using {weapon_input}!")
            damage = dict[character][weapon_input]["damage"]
            print(f"You inflicted {damage} damage points")
            print("\n" * 2)
        else:
            print("Invalid input. Try again.")
            print("\n" * 2)


def protect(character, dict):
    """
    Check if an inventory item can protect
    Ask user for input of protection item
    """
    protection = []
    for item in dict[character]:
        if dict[character][item]["protection"] != 0:
            protection.append(item)
    print("\n" * 2)
    print("Available Protection:")
    if len(protection) == 0:
        print("You have no protection items available")
        print("\n" * 2)
    else:
        for p in protection:
            print(f"* {p}")
        protect_input = input("Which protection item would you like to use?")
        print("\n" * 2)
        if protect_input in protection:
            print(f"Using {protect_input}!")
            print("\n" * 2)
        else:
            print("Invalid input. Try again.")
            print("\n" * 2)


def heal(character, dict):
    """
    Check for healing items
    Ask user for input of healing item
    """
    healing = []
    for item in dict[character]:
        if dict[character][item]["healing"] != 0:
            healing.append(item)
    print("\n" * 2)
    print("Available Healing Items:")
    if len(healing) == 0:
        print("You have no healing items available")
        print("\n" * 2)
    else:
        for h in healing:
            print(f"* {h}")
        heal_input = input("Which healing item would you like to use?")
        print("\n" * 2)
        if heal_input in healing:
            print(f"Using {heal_input}!")
            print("\n" * 2)
        else:
            print("Invalid input. Try again.")
            print("\n" * 2)


print("Justice League: Crisis on Infinite Earths")
print("Character Choices:")
while True:
    for char in inventory:
        print(f"- {char}")
    character = input("Choose your character: ")
    print("\n" * 2)
    if character == "Wonder Woman":
        p_inventory = inventory["Wonder Woman"]
        break
    elif character == "Batman":
        p_inventory = inventory["Batman"]
        break
    elif character == "The Flash":
        p_inventory = inventory["The Flash"]
        break
    else:
        print("Invalid character. Try again.")


print("Valid actions for current location")
# valid directions and actions for the characters
valid_actions = {"directions": ["north", "south", "east", "west"],
                 "actions": ["quit", "explore", "attack", "defend", "heal"],
                 "inventory": p_inventory
                 }

while True:
    # print a list a valid actions before user input. Organized according to
    # possible direction and actions
    for user_action in valid_actions:
        if user_action == "actions":
            # prints out a list of valid actions from the list in valid_actions
            print(f"Complete one of the following {user_action}:")
            possible_actions = valid_actions["actions"]
            # using a loop, print out all the actions the user can use
            for action in possible_actions:
                print(f"* {action}")
        elif user_action == "inventory":
            print("* inventory")
    # after user input, print out the action choosen by the user
    action_input = input("Action: ")
    print("\n" * 2)
    direction = valid_actions["directions"]
    action = valid_actions["actions"]
    # convert the user input to all lower case to prevent errors
    # print out the action chosen
    if action_input.lower() == "quit":
        print("Goodbye! Thanks for playing!")
        sys.exit()
    elif action_input.lower() == "attack":
        weapons(character, inventory)
    elif action_input.lower() == "defend":
        protect(character, inventory)
    elif action_input.lower() == "heal":
        heal(character, inventory)
    elif action_input.lower() == "explore":
        print(f"Go in one of the following directions:")
        # all the directions the user can go
        for d in direction:
            print(f"* {d}")
        direction_input = input("Which direction would you like to go?")
        print("\n" * 2)
        if direction_input.lower() in direction:
            print(f"Going {direction_input}!")
            print("\n" * 2)
        else:
            print("Invalid input. Try again.")
            print("\n" * 2)
    # print the inventory for the chosen character with details
    elif action_input.lower() == "inventory":
        for item in p_inventory:
            print(f"* {item}")
            for description in p_inventory[item]:
                print(f"{description} - {p_inventory[item][description]}")
        print("\n" * 2)
    else:
        print("Invalid action!")
        print("\n" * 2)
