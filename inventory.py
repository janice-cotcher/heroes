# inventory paired with characters
class Inventory:
    def __init__(self):
        raise NotImplementedError("Do not create raw inventory objects")

    def __str__(self):
        return self.name

    def EmptyInventory(self):
        return self.items > 0


class Weapon(Inventory):
    def __init__(self, name, description, owner, damage, protection):
        self.name = name
        self.description = description
        self.owner = owner
        self.damage = damage
        self.protection = protection


class Protection(Inventory):
    def __init__(self, name, description, owner, protection):
        self.name = name
        self.description = description
        self.owner = owner
        self.damage = 0
        self.protection = protection


class Vehicle(Inventory):
    def __init__(self, name, hero, protection, attack):
        self.name = name
        self.hero = hero
        self.protection = protection
        self.attack = attack

    def __str__(self):
        description = f"""
The {self.name} can only be used by {self.hero}.
The {self.name} has a protection value of {self.protection}.
The {self.name} has an attack value of {self.attack}
        """
        return description


# define hero's vehciles and characteristics
invisiblePlane = Vehicle("Invisible Plane", "Wonder Woman", 100, 20)
tumbler = Vehicle("Tumbler", "Batman", 100, 50)
batmobile = Vehicle("Batmobile", "Batman", 100, 50)
bat = Vehicle("Bat", "Batman", 0, 20)
batpod = Vehicle("Batpod", "Batman", 50, 50)

vehicles = [invisiblePlane, tumbler, batmobile, bat, batpod]


lasso = Protection("Lasso of Truth", "extracts truth from people",
                   "Wonder Woman", 5)
bracelets = Weapon("Bracelets of Submission", "bulletproof bracelets",
                   "Wonder Woman", 100, 50)
sword = Weapon("Sword of Athena", "magically-empowered sword wielded",
               "Wonder Woman", 500, 0)
batrang = Weapon("Batarang", "boomerang shaped like a bat", "Batman", 10, 0)
hook = Weapon("Grapple hook", "spear-shooting spring-based device", "Batman",
              10, 0)
sonic = Weapon("Sonic Bat Device",
               "high frequency emitter allowing the control of bats",
               "Batman", 15, 100)
suit = Protection("Red suit", "protection when travelling at super speed",
                  "The Flash", 100)


def player_inventory(player):
    """Assigns inventory for the choosen character"""
    if player == "Wonder Woman":
        return [lasso, bracelets, sword, invisiblePlane]
    elif player == "Batman":
        return [batrang, hook, sonic, tumbler, bat, batpod]
    else:
        return [suit]


def hero_vehicle(vehicles):
    """print a list of the hero's vehicles"""
    for vehicle in vehicles:
        print(vehicle)


def vehicle_owner(hero):
    """Checks which vehicle is wonded by which hero"""
    if hero == "Wonder Woman":
        print(invisiblePlane)
    elif hero == "The Flash":
        print("The Flash has no vehicles")
    else:
        print(tumbler)
        print(bat)
        print(batpod)

# for i in player_inventory("Batman"):
#     for x in i:
#         print(x)
