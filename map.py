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

class Supplies(MapTile):
    """Position that contains survival supplies"""
    def __init__(self, x, y):
        """Intitial supplies at tile"""
        self.i = 0
        self.name = "Supplies"
        self.inventory = []

        super().__init__(x, y)

class Weapons(MapTile):
    """Position that contains weapons"""
    def __init__(self, x, y):
        """Intitial weapons at tile"""
        self.i = 0
        self.name = "Weapons"
        self.inventory = []

        super().__init__(x, y)

class BigBoss(MapTile):
    """Position of the main villian"""
    def intro_text(self):
        return """ Big Boss"""

class Enemy(MapTile):
    """Position of underling of the main villian"""
    def intro_text(self):
        return """ Enemy """

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
            print(tabulate(city_map, tablefmt="github"))
            with open("map.txt", "w") as f:
                f.write(tabulate(city_map, tablefmt="github"))
            return city_map
            # break
        else:
            print("Invalid location")
            print("\n")


def get_player_command(message):
    """Get user input and convert the string to lowercase"""
    action_input = input(message)
    return action_input.lower()


# initialize the city map
city_map = []

map_dsl = open('map.txt').read().strip()
map_dsl = map_dsl.replace("+", "")
map_dsl = map_dsl.replace(" ", "")
map_dsl = map_dsl.replace("-", "")

def tile_at(x, y):
    """Locates the tile at a coordinate"""
    if x < 0 or y < 0:
        return None
    try:
        return city_map[y][x]
    except IndexError:
        return None


# city's map
with open("map.txt", "r") as file:
    city_dsl = file.read()


def is_dsl_valid(dsl):
    """
    Check to make sure there is only one start tile and escape pod.
    Also check that each row has the same number of columns
    """
    if dsl.count("|Start|") != 1:
        return False
    if dsl.count("|BigBoss|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True


# key to the city's map
tile_type_dict = {"Supplies": Supplies,
                  "Start": Start,
                  "Weapons": Weapons,
                  "Enemy": Enemy,
                  "BigBoss": BigBoss,
                  "Blank": Blank}
# initialize the start tile
start_tile_location = None


def parse_city_dsl():
    """Taking the city map as a string and returning a list"""
    # if not is_dsl_valid(city_dsl):
    #     raise SyntaxError("DSL is invalid!")

    dsl_lines = map_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]
    # Iterate over each line in the DSL.
    for y, dsl_row in enumerate(dsl_lines):
        # Create an object to store the tiles
        row = []
        # Split the line into abbreviations
        dsl_cells = dsl_row.split("|")
        # The split method includes the beginning
        # and end of the line so we need to remove
        # those nonexistent cells
        dsl_cells = [c for c in dsl_cells if c]
        # Iterate over each cell in the DSL line
        for x, dsl_cells in enumerate(dsl_cells):
            # Look up the abbreviation in the dictionary
            tile_type = tile_type_dict[dsl_cells]
            # set the start tile location
            if tile_type == Start:
                global start_tile_location
                start_tile_location = x, y
            # If the dictionary returned a valid type, create
            # a new tile object, pass it the X-Y coordinates
            # as required by the tile __init__(), and add
            # it to the row object. If None was found in the
            # dictionary, we just add None.
            row.append(tile_type(x, y) if tile_type else None)
        # Add the whole row to the city_map
        city_map.append(row)

# print(city_dsl)
parse_city_dsl()
