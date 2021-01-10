from termcolor import colored


# Coordinates are
# (0,0) --> +
# |
# V
# +

class Robot(object):

    __SPRITE_UP = "^"
    __SPRITE_DOWN = "V"
    __SPRITE_LEFT = ">"
    __SPRITE_RIGHT = "<"

    __GHOST_LETTERS = ["B", "R", "O", "P"]

    # ONLY ACCESS THE ROBOTS ATTRIBUTES EXPOSED BY GET METHODS
    def __init__(self):
        self.__MAP = self.__load_map()

        self.__pos = [1,1] # First coordinate is the row number, the second is the column number

        self.__direction = [1, 0]
        self.__sprite = self.__SPRITE_DOWN


    def __vector_addition(self, vec1, vec2):
        return [vec1[i] + vec2[i] for i in range(2)]


    def __load_map(self):

        with open("map.txt") as f:

            MAP = [list(line.strip()) for line in f.readlines()]

        return MAP

    def __update_sprite(self):
        '''Updates the sprite so that it's facing the correct direction'''
        if self.__direction == [1, 0]:
            self.__sprite = self.__SPRITE_DOWN
        
        elif self.__direction == [0, 1]:
            self.__sprite = self.__SPRITE_RIGHT
        
        elif self.__direction == [0, -1]:
            self.__sprite = self.__SPRITE_LEFT
        
        elif self.__direction == [-1, 0]:
            self.__sprite = self.__SPRITE_UP


    def is_wall_ahead(self):
        '''Returns true if there is a wall in front of the robot'''

        ahead_coordinates = self.__vector_addition(self.__pos, self.__direction)

        if self.__MAP[ahead_coordinates[0]][ahead_coordinates[1]] == "#":
            return True
        return False

    def move_forward(self):
        '''Moves the robot one unit forward'''

        # Only move forward if there isn't a wall ahead
        if not self.is_wall_ahead():
            self.__pos = self.__vector_addition(self.__pos, self.__direction)

            if self.__MAP[self.__pos[0]][self.__pos[1]] in self.__GHOST_LETTERS: # If we've walked into a ghost
                print("ON GHOST!!!")

    def turn_right(self):
        '''Rotates the robot right by 90 degrees'''
        self.__direction = [-self.__direction[1], self.__direction[0]]
        
        self.__update_sprite()

    def turn_left(self):
        '''Rotates the robot left by 90 degrees'''
        self.__direction = [self.__direction[1], -self.__direction[0]]

        self.__update_sprite()


    def print_map(self):
        '''Prints the current state of the map to the terminal'''
        for i, row in enumerate(self.__MAP):

            for j, char in enumerate(row):
          
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

                # Draw the robot, but importantly preserve the on colour
                if i == self.__pos[0] and j == self.__pos[1]:
                    char = self.__sprite
                    color = 'grey'

                if on_colour:
                    text = colored(char, colour, on_colour, attrs=['bold']) 
                else:
                    text = colored(char, colour)

                print(text, end ="")

            print("") # Newline



