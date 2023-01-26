# RPG based on the comic book series published by DC Comics
# 12 issue run: April 1985 - March 1986
print("Justice League: Crisis on Infinite Earths")
print("Valid actions for current location")
# valid directions and actions for the characters
valid_actions = {"directions": ["north", "south", "east", "west"],
                 "actions": ["explore", "attack", "defend", "heal"]}
# print a list a valid actions before user input. Organized according to
# possible direction and actions
for user_action in valid_actions:
    # prints out a list of valid directions from the list in valid_actions
    if user_action == "directions":
        print(f"Go in one of the following {user_action}:")
        # define possible_directions as the list that is the value
        # attached to directions in valid_actions
        possible_directions = valid_actions["directions"]
        # using a loop, print out all the directions the user can go
        for direction in possible_directions:
            print(f"* {direction}")
    elif user_action == "actions":
        # prints out a list of valid actions from the list in valid_actions
        print(f"Complete one of the following {user_action}:")
        possible_actions = valid_actions["actions"]
        # using a loop, print out all the actions the user can use
        for action in possible_actions:
            print(f"* {action}")
# after user input, print out the action choosen by the user
action_input = input("Action: ")
direction = valid_actions["directions"]
action = valid_actions["actions"]
# convert the user input to all lower case to prevent errors
# print out the action chosen
if action_input.lower() in direction:
    print(f"Go {action_input}!")
elif action_input.lower() in action:
    print(f"{action_input}!")

else:
    print("Invalid action!")
