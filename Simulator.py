from termcolor import colored


# Coordinates are
# (0,0) --> +
# |
# V
# +

class Robot(object):

    __STARTING_POS = [1,1]

    __SPRITE_UP = "^"
    __SPRITE_DOWN = "V"
    __SPRITE_LEFT = ">"
    __SPRITE_RIGHT = "<"

    __GHOST_LETTERS = ["B", "R", "O", "P"]

    __TRUFFLE_SPRITE = "t"

    # ONLY ACCESS THE ROBOTS ATTRIBUTES EXPOSED BY GET METHODS
    def __init__(self):
        self.__MAP = self.__load_map()

        self.__pos = self.__STARTING_POS # First coordinate is the row number, the second is the column number

        self.__direction = [1, 0]
        self.__sprite = self.__SPRITE_DOWN

        self.__holding_truffle = False


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
            self.__sprite = self.__SPRITE_LEFT
        
        elif self.__direction == [0, -1]:
            self.__sprite = self.__SPRITE_RIGHT
        
        elif self.__direction == [-1, 0]:
            self.__sprite = self.__SPRITE_UP

    def __check_ahead(self, chars_to_check_for)
        ahead_coordinates = self.__vector_addition(self.__pos, self.__direction)

        if self.__MAP[ahead_coordinates[0]][ahead_coordinates[1]] in chars_to_check_for:
            return True
        return False

    def is_wall_ahead(self):
        '''Returns true if there is a wall in front of the robot'''

        return self.__check_ahead(["#"])

    def is_truffle_ahead(self):
        '''Returns true if there is a truffle in front of the robot'''

        return self.__check_ahead([self.__TRUFFLE_SPRITE])

    def is_ghost_ahead(self):
        '''Returns true if there is a ghost in front of the robot '''
        
        return self.__check_ahead(self.__GHOST_LETTERS)

    def move_forward(self):
        '''Moves the robot one unit forward'''

        # Only move forward if there isn't a wall ahead
        if not self.is_wall_ahead():
            self.__pos = self.__vector_addition(self.__pos, self.__direction)

            if self.__MAP[self.__pos[0]][self.__pos[1]] in self.__GHOST_LETTERS: # If we've walked into a ghost
                print("ON GHOST!!!")

    def turn_left(self):
        '''Rotates the robot left by 90 degrees'''
        self.__direction = [-self.__direction[1], self.__direction[0]]
        
        self.__update_sprite()

    def turn_right(self):
        '''Rotates the robot right by 90 degrees'''
        self.__direction = [self.__direction[1], -self.__direction[0]]

        self.__update_sprite()

    def pick_up_truffle(self):
        ''' Picks up a truffle if it's infront of the robot, and the robot has space for it'''

        if not self.__holding_truffle and self.is_truffle_ahead():
            self.__holding_truffle == True

            truffle_location = self.__vector_addition(self.__pos, self.__direction)

            self.__MAP[truffle_location[0]][truffle_location[1]] = " " # Remove the truffle from the map

            print("Picked up truggle")

    def drop_truffle(self):
        ''' Drops a truffle at the robot's current location '''

        print(self.__holding_truffle)
        if self.__holding_truffle:
            self.__MAP[self.__pos[0]][self.__pos[1]] = "t" # Drop the truffle
            self.__holding_truffle = False
        
            if self.__pos == self.__STARTING_POS:
                print("DELIVERED TRUFFLE!") 

    def print_map(self):
        '''Prints the current state of the map to the terminal'''
        for i, row in enumerate(self.__MAP):

            for j, char in enumerate(row):
          
                colour = 'white'
                on_colour = None

                if char == "#":
                    colour = 'white'
                elif char == self.__TRUFFLE_SPRITE:
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



