import random
import matplotlib.pyplot as plt

def generateMaze(width,length):
    
    maze=[[0 for _ in range(width)] for _ in range(length)]
    
    def carve(x,y):
        
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        random.shuffle(directions)
        
        for dx,dy in directions:
            nx,ny=x+2*dx,y+2*dy
            if 0<=nx<width and 0<=ny<length and maze[ny][nx]==0:
                maze[y+dy][x+dx]=1
                maze[ny][nx]=1
                carve(nx,ny)
        
    startX,startY=random.randrange(1,width,2),random.randrange(1,length,2)
    maze[startY][startX]=1
    carve(startX,startY)
        
    return maze

maze=generateMaze(91,91)

# Plotting the maze
plt.figure(figsize=(21, 21))
plt.imshow(maze, cmap='binary')  # Use a binary colormap to display 0 as black and 1 as white
plt.axis('off')  # Turn off axes for better visualization
plt.title("Generated Maze")
plt.show()
