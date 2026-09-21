# Defining all rooms in the house
inventory = []
rooms = {
    "corridor": {
        "description": "You are in a dark corridor. Doors lead to the kitchen and the bedroom.",
        "exits": {"north": "kitchen", "east": "bedroom"}
    },
    "kitchen": {
        "description": "You are in the kitchen. It's filled with the stench of the rotting meat. A door leads back south and one leads east to the study room",
        "exits": {"south": "corridor", "east": "study room"}
    },
    "study room": {
        "description": "You are in a dusty study room. There's a key on the desk with dried blood! A door leads west back to the kitchen, and south to the front door.",
        "exits": {"west": "kitchen", "south": "front_door"},
        "item": "key"
    },
    "bedroom": {
        "description": "You are in the bedroom. The wallpaper is rotting away like peeling skin. The doors lead west back to the corridor, and north to the ghost room.",
        "exits": {"west": "corridor", "north": "ghost_room"}
    },
    "ghost_room": {
        "description": "It's watching you. You can't see it, but it knows exactly where you are standing.",
        "exits": {"south": "bedroom"}
    },
    "front_door": {
        "description": "You are at the front door. You can escape if you have the key!",
        "exits": {"north": "study room"}
    }
}

# Player's current state
current_room = "corridor"

# Show the Starting Room
print(rooms[current_room]["description"])

# Initializing turns
turns = 0
max_turns = 10
game_over = False

# Using while loop
while not game_over:
        print("\nExits", list(rooms[current_room]["exits"].keys()))
        command = input("In which direction do you want to go?").lower()

        # Check if the exit typed is valid or not
        if command in rooms[current_room]["exits"]:
            current_room = rooms[current_room]["exits"][command]
            print(rooms[current_room]["description"])
            turns += 1
        elif command == "take":
            if "item" in rooms[current_room]:
                item = rooms[current_room]["item"]
                inventory.append(item)
                print(f"You picked up: {item}")
                del rooms[current_room]["item"]
            else:
                print("There's nothing here to take.")
        else:
            print("You cannot go that way.")
        
        # Check win/lose conditions
        if current_room == "ghost_room":
            print("The ghost catches you. Presence erased. Game over.")
            game_over = True
        elif turns >= max_turns:
            print("You ran out of time! Game over.")
            game_over = True
        elif current_room == "front_door" and "key" not in inventory:
            print("You need the key to escape! Find it before the ghost finds you or you run out of time.")
        elif current_room == "front_door" and "key" in inventory:
            print("You escaped the house! The Haunt ends.")
            game_over = True