# RPG based on the comic book series published by DC Comics
# 12 issue run: April 1985 - March 1986
import sys
import hero
import map
from tabulate import tabulate
from time import sleep
# import inventory


def play():
    """Print an action menu and allow for continous game play"""
    # print title of game
    # intro_text()
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
        print("\n")
        if action_input in action:
            print(f"{action_input.title()}!")
            print("\n")
            if action_input == "quit":
                sys.exit()
            # after the map is choosen, player chooses character
            elif action_input == "map":
                map.choose_map()
                hero.choose_character()
                add_action(action)
            # after the character is choosen, player chooses the map to play
            elif action_input == "characters":
                hero.choose_character()
                map.choose_map()
                add_action(action)
            elif action_input == "move":
                # directions menu and options appear when move is choosen
                for d in directions:
                    print(d)
                user_direction = get_player_command("What direction? ")
                print("\n")
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
