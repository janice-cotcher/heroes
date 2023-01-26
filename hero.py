import inventory


class Hero():
    def __init__(self):
        raise NotImplementedError("Do not create raw Hero objects")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

    def __getinventory__(self, inventory):
        return self.inventory


class WonderWoman(Hero):
    """
    Wonder Woman's name, idenity and characteristics. She starts with
    no supplies to begin
    """
    def __init__(self):
        self.name = "Wonder Woman"
        self.identity = "Diana Prince"
        self.power = "super strength"
        self.hp = 200
        self.inventory = inventory.player_inventory("Wonder Woman",
                                                    inventory.inventory)
        self.supplies = []


class Batman(Hero):
    """
    Batman's name, idenity and characteristics. He starts with no
    no supplies to beging with.
    """
    def __init__(self):
        self.name = "Batman"
        self.identity = "Bruce Wayne"
        self.power = "martial arts"
        self.hp = 150
        self.inventory = inventory.player_inventory("Batman",
                                                    inventory.inventory)
        self.supplies = []


class Flash(Hero):
    """
    The Flash's name, idenity and characteristics. He has no
    inventory to collect.
    """
    def __init__(self):
        self.name = "The Flash"
        self.identity = "Barry Allen"
        self.power = "super speed"
        self.hp = 90
        self.inventory = inventory.player_inventory("The Flash",
                                                    inventory.inventory)
        self.supplies = []


# assign variables to hero classes and put them in a list
WonderWoman = WonderWoman()
Batman = Batman()
Flash = Flash()
heroes = [WonderWoman, Batman, Flash]


def hero_check(hero):
    """Checks which hero was chosen and prints out the characteristics"""
    if hero == "Wonder Woman":
        hero_characteristics(WonderWoman)
    elif hero == "The Flash":
        hero_characteristics(Flash)
    else:
        hero_characteristics(Batman)


def hero_characteristics(hero):
    """Prints out the hero's characteristics"""
    print(f"{hero.name}'s true identy is {hero.identity}")
    print(f"{hero.name}'s super power is {hero.power}")
    print(f"{hero.name} has {hero.hp} health points")
    if len(hero.supplies) != 0:
        protection = hero.supplies[0]
        weapon = hero.supplies[1]
        if len(protection) != 0:
            print(f"{hero.name}'s current protection items:")
            for items in protection:
                print(f"* {items}")
        else:
            print(f"{hero.name} has no protection items")
        if len(weapon) != 0:
            print(f"{hero.name}'s current weapons:")
            for items in weapon:
                print(f"* {items}")
        else:
            print(f"{hero.name} has no weapons.")
    else:
        print(f"{hero.name} has no supplies.")
    if len(hero.inventory) != 0:
        protection = hero.inventory[0]
        weapon = hero.inventory[1]
        if len(protection) != 0:
            print(f"{hero.name}'s current protection items:")
            for items in protection:
                print(f"* {items}")
        else:
            print(f"{hero.name} has no protection items")
        if len(weapon) != 0:
            print(f"{hero.name}'s current weapons:")
            for items in weapon:
                print(f"* {items}")
        else:
            print(f"{hero.name} has no weapons.")
    else:
        print(f"{hero.name} has no weapons or protection items.")

#
# hero_characteristics("The Flash")


def get_player_command(message):
    """Get user input and convert the string to lowercase"""
    action_input = input(message)
    return action_input.lower()


def choose_character():
    """User chooses which hero they wish to play as"""
    print("Possible Characters:")
    character = heroes
    for hero in character:
        print(hero)
    print("\n")
    while True:
        input = get_player_command("What character would you like to play? ")
        print("\n")
        player = input.title()
        # prevent input error if the user does not input The Flash
        if player == "The Flash":
            player = "Flash"
        if player == "Wonder Woman":
            player = "WonderWoman"
        # put all the hero subclasses into a list
        hero_subclass = [cls.__name__ for cls in Hero.__subclasses__()]
        # print(hero_subclass)
        # compare the inputted player to see if it is valid
        # print the choosen character with characteristics and inventory
        if player in hero_subclass:
            if player == "Flash":
                player = "The Flash"
            if player == "WonderWoman":
                player = "Wonder Woman"
            print("\n")
            print(f"Welcome, {player}!")
            hero_check(player)
            # inventory.vehicle_owner(player)
            # inventory.player_inventory(player)
            print("\n")
            return player
            # break
        else:
            print("Invalid Character")
            print("\n")
