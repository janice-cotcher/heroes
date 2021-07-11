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
        self.inventory = []
        self.supplies = inventory.player_inventory("The Flash",
                                                   inventory.inventory)


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
    print(f"{hero.name}'s current inventory:")
    for items in hero.supplies:
        print(f"* {items}")

#
# hero_characteristics("The Flash")
