from termcolor import colored

with open("map.txt") as f:

    MAP = [list(line.strip()) for line in f.readlines()]

def print_map():

    for row in MAP:

        for char in row:

            colour = 'white'
            on_colour = None

            if char == "#":
                colour = 'white'
            elif char == "t":
                colour = 'grey'
                on_colour = 'on_white'
            elif char == 'S':
                colour = 'magenta'
                on_colour = 'on_magenta'
            elif char == 'B':
                colour = 'blue'
                on_colour = "on_red"
            elif char == 'O':
                colour = 'yellow'
                on_colour = "on_red"
            elif char == 'P':
                colour = 'magenta'
                on_colour = "on_red"
            elif char == 'R':
                colour = "yellow"
                on_colour = "on_red"

            if on_colour:
                text = colored(char, colour, on_colour, attrs=['bold']) 
            else:
                text = colored(char, colour)

            print(text, end ="")

        print("") # Newline
            

print_map()