import random
from tabulate import tabulate


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")


class Start(MapTile):
    def intro_text(self):
        return """ """


class Blank(MapTile):
    def intro_text(self):
        return """There are no items to collect or enemies to fight.
                  Enjoy your rest."""


def append_list(dictionary, list):
    """Create a list from elements of a dictionary"""
    for x in dictionary:
        list.append(x)


def replace_tile(list, tile1, tile2):
    """Make sure that replaced tiles do not overwrite each other"""
    while random_tile(list, tile1) == random_tile(list, tile2):
            random_tile(list, tile1)
            random_tile(list, tile2)


def random_tile(list, tile):
    """Choose a random tile to replace and return the indices"""
    x = random.choice(list)
    y = random.choice(x)
    n = list.index(x)
    m = x.index(y)
    list[n][m] = tile
    return (n, m)


def generate_map(list):
    """randomly generate a 5x5 city map from tile types"""
    map = [[random.choice(list) for i in range(5)] for j in range(5)]
    # add boss and start tiles
    replace_tile(map, "BigBoss", "Start")
    return map


def print_map(dictionary):
    """print out each city map generated"""
    for key in dictionary:
        map = dictionary[key]
        print(f"{key}")
        # format the maps in rows and columns
        print(tabulate(map, tablefmt="plain"))
        print("\n")


# game cities
cities = {"Central City": "home of The Flash",
          "Hall Of Justice": "headquarters for the Justice League",
          "Gotham City": "home of Batman",
          "Metropolis": "home of Superman",
          "Themyscira": "birth place of Wonder Woman"
          }
# map tile types
map_tiles = {"Enemy": {"description": "location of an enemy",
                       "abbreviation": "ET",
                       "action": "must defeat the enemy to continue"},
             "BigBoss": {"description":
                          "Big Boss enemy location and the exit for the city",
                          "abbreviation": "BT",
                          "action":
                          "may run away or fight the boss to continue"},
             "Weapons": {"description": "location of a weapon",
                         "abbreviation": "WT",
                         "action":
                         "may pick up items or move to another location"},
             "Supplies": {"description":
                          "location of protection and healing items",
                          "abbreviation": "ST",
                          "action": "must pick up the weapon to continue"},
             "Blank": {"description":
                       "location with no items",
                       "abbreviation": "BT",
                       "action": "may rest or move to another location"},
             "Start": {"description": "entrance to the city",
                       "abbreviation": "S",
                       "action": "may rest or move to another location"}
             }

# generate a list of cities
city_level = []
append_list(cities, city_level)
# generate a list of tile types removing the start and boss tiles
tile_types = []
append_list(map_tiles, tile_types)
tile_types.remove("BigBoss")
tile_types.remove("Start")

# organize each city level and its map in a dictionary
main_map = {}
for city in city_level:
    city_map = generate_map(tile_types)
    main_map[city] = city_map

# print_map(main_map)


def choose_map():
    """The player chooses which city they would like to play"""
    city = city_level
    print("Cities")
    for place in city:
        print(place)
    print("\n")
    while True:
        # player chooses which city level they want play and then a random
        # 5x5 map is generated and printed
        input = get_player_command("What city do you want to start in? ")
        city_choice = input.title()
        if city_choice in city:
            print(f"Welcome to {city_choice}!")
            city_map = main_map[city_choice]
            print(tabulate(city_map, tablefmt="grid"))
            with open("map.txt", "w") as f:
                f.write(tabulate(city_map, tablefmt="grid"))
            return city_map
            # break
        else:
            print("Invalid location")
            print("\n")


def get_player_command(message):
    """Get user input and convert the string to lowercase"""
    action_input = input(message)
    return action_input.lower()
