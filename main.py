# RPG based on the comic book series published by DC Comics
# 12 issue run: April 1985 - March 1986
import sys
import hero
import map
from tabulate import tabulate
from time import sleep
import inventory


def play():
    """Print an action menu and allow for continous game play"""
    # print title of game
    intro_text()
    # valid directions and actions for the characters
    action = ["quit", "characters", "map"]
    directions = ["north", "south", "east", "west"]
    # print a list a valid actions before user input. Organized according to
    # possible direction and actions
    print("\n")
    print_actions(action)
    while True:
        # after user input, print out the action choosen by the user
        action_input = get_player_command("Action: ")
        if action_input in action:
            print(f"{action_input.title()}!")
            if action_input == "quit":
                sys.exit()
            # after the map is choosen, player chooses character
            elif action_input == "map":
                choose_map()
                choose_character()
                add_action(action)
            # after the character is choosen, player chooses the map to play
            elif action_input == "characters":
                choose_character()
                choose_map()
                add_action(action)
            elif action_input == "move":
                # directions menu and options appear when move is choosen
                for d in directions:
                    print(d)
                user_direction = get_player_command("What direction?")
                if user_direction in directions:
                    print(f"Moving {user_direction}")
                    print("\n")
                else:
                    print("Invalid direction")
                    print("\n")
        else:
            print("Invalid action!")
            print("\n")


def get_player_command(message):
    """Get user input and convert the string to lowercase"""
    action_input = input(message)
    return action_input.lower()


def choose_character():
    """User chooses which hero they wish to play as"""
    print("Possible Characters:")
    character = hero.heroes
    for heroes in character:
        print(heroes)
    while True:
        input = get_player_command("What character would you like to play?")
        player = input.title()
        # prevent input error if the user does not input The Flash
        if player == "The Flash":
            player = "Flash"
        if player == "Wonder Woman":
            player = "WonderWoman"
        # put all the hero subclasses into a list
        hero_subclass = [cls.__name__ for cls in hero.Hero.__subclasses__()]
        # print(hero_subclass)
        # compare the inputted player to see if it is valid
        # print the choosen character with characteristics and inventory
        if player in hero_subclass:
            if player == "Flash":
                player = "The Flash"
            if player == "WonderWoman":
                player = "Wonder Woman"
            print(f"Welcome, {player}!")
            hero.hero_check(player)
            # inventory.vehicle_owner(player)
            # inventory.player_inventory(player)
            print("\n")
            break
        else:
            print("Invalid Character")
            print("\n")


def choose_map():
    """The player chooses which city they would like to play"""
    city = map.city_level
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
            city_map = map.main_map[city_choice]
            print(tabulate(city_map, tablefmt="grid"))
            break
        else:
            print("Invalid location")
            print("\n")


def add_action(list):
    """Unlock actions after characters and map is chosen"""
    unlock_action = ["move", "attack", "defend", "heal"]
    list.remove("map")
    list.remove("characters")
    for action in unlock_action:
        list.append(action)
    print_actions(list)
    print("\n")


def print_actions(action):
    print(f"Complete one of the following actions:")
    for user_action in action:
        print(f"* {user_action}")
    print("\n")


def intro_text():
    """Prints title of game in a typewriter style"""
    words = r"""
       _              _    _
      | |            | |  (_)
      | | _   _  ___ | |_  _   ___  ___
  _   | || | | |/ __|| __|| | / __|/ _ \
 | |__| || |_| |\__ \| |_ | || (__|  __/
  \____/  \__,_||___/ \__||_| \___|\___|
  _
 | |                                      _
 | |      ___   __ _   __ _  _   _   ___ (_)
 | |     / _ \ / _` | / _` || | | | / _ \
 | |____|  __/| (_| || (_| || |_| ||  __/ _
 |______|\___| \__,_| \__, | \__,_| \___|(_)
                       __/ |
                      |___/
   _____        _       _
  / ____|      (_)     (_)
 | |      _ __  _  ___  _  ___    ___   _ __
 | |     | '__|| |/ __|| |/ __|  / _ \ | '_ \
 | |____ | |   | |\__ \| |\__ \ | (_) || | | |
  \_____||_|   |_||___/|_||___/  \___/ |_| |_|
  _____          __  _         _  _
 |_   _|        / _|(_)       (_)| |
   | |   _ __  | |_  _  _ __   _ | |_  ___
   | |  | '_ \ |  _|| || '_ \ | || __|/ _ \
  _| |_ | | | || |  | || | | || || |_|  __/
 |_____||_| |_||_|  |_||_| |_||_| \__|\___|
  ______              _    _
 |  ____|            | |  | |
 | |__    __ _  _ __ | |_ | |__   ___
 |  __|  / _` || '__|| __|| '_ \ / __|
 | |____| (_| || |   | |_ | | | |\__ \
 |______|\__,_||_|    \__||_| |_||___/
"""
    for char in words:
        sleep(0.005)
        print(char, end=" ", flush=True)


play()
