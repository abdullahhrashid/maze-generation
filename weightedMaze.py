import numpy as np
import random
import matplotlib.pyplot as plt
import heapq

def generateMaze(width,height,max=10,min=1):
    
    maze=[[0 for _ in range(width)] for _ in range(height)]
    
    def carve(x,y):
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        random.shuffle(directions)
        
        for dx,dy in directions:
            nx,ny=x+2*dx,y+2*dy
            if 0<=nx<width and 0<=ny<height and maze[ny][nx]==0:
                maze[y+dy][x+dx]=random.randint(min,max)
                maze[ny][nx]=random.randint(min,max)
                carve(nx,ny)
    
    startX,startY=random.randrange(1,width,2),random.randrange(1,height,2)
    maze[startY][startX]=random.randint(min,max)
    carve(startX,startY)
    
    return maze

maze=generateMaze(21,21)
    
for row in maze:
    print(' '.join([f"{cell:2}" if cell != 0 else "##" for cell in row]))

def visualize_weighted_maze(maze):
    grid = np.array(maze)
    grid[grid == 0] = -1
    plt.imshow(grid, cmap="viridis", interpolation="nearest")
    plt.colorbar(label="Path Weights")
    plt.show()

visualize_weighted_maze(maze)


"""def aStar(maze,start,goal):
    
    def manhattan(x,y):
        return abs(goal[0]-x) + abs(goal[1]-y)
    
    path=[[start],0]
    x,y=start
    X,Y=goal
    height, width = len(maze), len(maze[0])
    
    while path:
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        scores=[]
        
        for dx,dy in directions:
            
            if 0<=x+dx<width and 0<=y+dy<height and maze[y+dy][x+dx]!=0:
                scores.append(path[1]+manhattan(x+dx,y+dy))
            else:
                directions.remove((dx,dy))

        if len(directions)!=0 and len(scores)!=0:
            dx,dy=directions[scores.index(min(scores))]
            
            path[0].append((x+dx,y+dy))
            path[1]+=maze[y+dy][x+dx]
            
            if x+dx==X and y+dy==Y:
                return path
            else:
                x=x+dx
                y=y+dy
                continue
        else:
            path[0].pop()
    
    if path[0][-1]!=(X,Y):
        return None"""


"""def visualize_maze(maze, path=None):
    maze_np = np.array(maze)
    plt.imshow(maze_np, cmap="viridis", origin='upper')

    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, color='red', linewidth=2, marker='o', markersize=5)

    plt.title("Maze Visualization")
    plt.axis("off")
    plt.show()

maze = generateMaze(21, 21)
print(maze)

start = (1, 1)  
goal = (19, 19)
path = aStar(maze, start, goal)

if path:
    print("Path found:", path)
    #print("Total cost:", total_cost)
else:
    print("No path found.")

visualize_maze(maze, path[0])"""
 