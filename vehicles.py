class Vehicle():
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


# define hero's vehciles and characteristics
invisiblePlane = Vehicle("Invisible Plane", "Wonder Woman", 100, 20)
tumbler = Vehicle("Tumbler", "Batman", 100, 50)
batmobile = Vehicle("Batmobile", "Batman", 100, 50)
bat = Vehicle("Bat", "Batman", 0, 20)
batpod = Vehicle("Batpod", "Batman", 50, 50)

vehicles = [invisiblePlane, tumbler, batmobile, bat, batpod]

# hero_vehicle(vehicles)
