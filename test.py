from Simulator import *

r = Robot()


instructions = list("fffflfflfffllfffrffrffff")


for instruction in instructions:

    if instruction == "f":
        r.move_forward()
    elif instruction == "l":
        r.turn_left()
    elif instruction == "r":
        r.turn_right()

    r.print_map()

    if (r.is_truffle_ahead()):
        print("truffle ahead")
        r.pick_up_truffle()

r.drop_truffle()
r.print_map()