from random import shuffle 
 
 # Generates a maze
 
width = int(input("Width of maze: "))
height = int(input("Height of maze: "))
 
maze = [["@" for i in range(width)] for i in range(height)] # Stores the walls each cell has

visited = [[False for i in range(width)] for i in range(height)] # Stores whether we have visited a tile

directions = [[2,0], [-2,0], [0,2], [0,-2]] # The directions that we can build the maze

start = [0,0]

def build_maze(x, y):
    
    # Look for non visited parts
    directionOrder = list(range(len(directions)))
    shuffle(directionOrder)
  
    for index in directionOrder.copy():
        direction =  directions[index]
        new_x = x + direction[0]
        new_y = y + direction[1]
        
        if new_x > 0 and new_x < width-1 and new_y > 0 and new_y < height-1:
            

            # Check to see if it's visited
            
            if not visited[new_y][new_x]: # If not visited
                '''
                for row in maze:
                    print("".join(row))
                '''
                intermed_x = new_x - direction[0]//2
                intermed_y = new_y - direction[1]//2
                
                visited[intermed_x][intermed_y] = True
                visited[new_y][new_x] = True
    
                maze[new_y][new_x] = "_" # Remove the wall
                maze[intermed_y][intermed_x] = "_" # Remove the wall
                '''
                for row in maze:
                    print("".join(row))
                '''    
                build_maze(new_x,new_y)

maze[0][1] = "_"
build_maze(1,1)

print(maze)
print(visited)

for row in maze:
    print("".join(row))
