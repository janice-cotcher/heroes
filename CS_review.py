# RPG based on the comic book series published by DC Comics
# 12 issue run: April 1985 - March 1986
import sys


print("Justice League: Crisis on Infinite Earths")
print("Valid actions for current location")
# valid directions and actions for the characters
valid_actions = ["actions", "directions"]
possible_directions = ["north", "south", "east", "west"]
possible_actions = ["explore", "attack", "defend", "heal", "quit"]
# print a list a valid actions before user input. Organized according to
# valid actions
while True:
    print("What do you want to do?")
    for action in possible_actions:
        print(f"* {action}")
    # after user input, print out the action choosen by the user
    action_input = input("Action: ")
    if action_input.lower() in possible_actions:
        if action_input.lower() == "explore":
            for direction in possible_directions:
                print(f"* {direction}")
            direction_input = input("Which direction do you want to go? ")
            if direction_input.lower() in possible_directions:
                print(f"Go {direction_input}!")
            else:
                print("Invalid direction!")
        elif action_input.lower() == "quit":
            print("Goodbye!")
            sys.exit()
        elif action_input.lower() in possible_actions:
            print(f"{action_input.title()}!")

        else:
            print("Invalid action!")
