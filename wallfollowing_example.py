from Simulator import *

r = Robot() # Make a new robot

r.print_map()

# We start facing downwards at [0,0]

# This is going to be a simple edge following algorithm

def is_wall_left():

    r.turn_left()
    is_ahead = r.is_wall_ahead()
    r.turn_right()

    return is_ahead

def is_wall_right():
    r.turn_right()
    is_ahead = r.is_wall_ahead()
    r.turn_left()

    return is_ahead

distance = 0 # If the distance is 0 we are back at the start
while True: # Main loop

    # Check to see if there is a truffle or a ghost

    if r.is_ghost_ahead(): # If there is a ghost ahead do a 180

        print("GHOST AVOIDED")
        r.turn_left()
        r.turn_left()

    elif r.is_truffle_ahead():
        r.pick_up_truffle()
        print("TRUFFLE AQUIRED!")
        # Now to take the truffle home

        # Turn around
        r.turn_right()
        r.turn_right()

        # Maze follow but in reverse

        while distance > 0:
            
            if not is_wall_right(): # Turn right to follow the wall
                r.turn_right()
            elif r.is_wall_ahead(): # We're at a dead end, turn around
                r.turn_left()

            if r.is_ghost_ahead(): # If there is a ghost ahead do a 180

                print("GHOST AVOIDED")
                r.turn_left()
                r.turn_left()

            r.move_forward()
            distance -= 1

            r.print_map()
            input()

        # Turn around

        r.turn_left()
        r.turn_left()

    # Check to see if there is a wall left of us

    if not is_wall_left():
        r.turn_left()
    elif r.is_wall_ahead():
        r.turn_right()

    if r.is_ghost_ahead(): # If there is a ghost ahead do a 180

        print("GHOST AVOIDED")
        r.turn_left()
        r.turn_left()


    r.move_forward()
    distance += 1


    r.print_map()

    input()
    




