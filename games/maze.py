
import queue
import time


maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', 'O', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', "#"],
    ['#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]



def find_start(maze):
    for index,row in enumerate(maze):
        for inner_pos,val in enumerate(row):
            if val == 'O':
                return (index,inner_pos)
            
def find_neighbors(maze,cur_pos):
    neighbors = []

    if cur_pos[1]-1 > 0:
        neighbors.append((cur_pos[0],cur_pos[1]-1))
    if cur_pos[1]+1 < len(maze[0])-1:
        neighbors.append((cur_pos[0],cur_pos[1]+1))
    if cur_pos[0]+1 < len(maze)-1:
        neighbors.append((cur_pos[0]+1,cur_pos[1]))
    if cur_pos[0]-1 > 0:
        neighbors.append((cur_pos[0]-1,cur_pos[1]))

    return neighbors

def find_path(maze):
    
    que = queue.Queue()
    start_pos = find_start(maze)
    que.put((start_pos,[start_pos]))
    seen = set()


    while not que.empty():

        cur_pos, track = que.get()
        r,c = cur_pos
        neighbors = find_neighbors(maze,cur_pos)
        if maze[r][c] == 'X':
                return track
        
        for cord in neighbors:
            row,col = cord[0],cord[1]
            if cord in seen or maze[row][col] == '#':
                continue

            new_path = track+[cord]
            que.put((cord,new_path))
            seen.add(cord)

track  = find_path(maze)

mazecpy = maze
for row,d in enumerate(mazecpy):
    for col,f in enumerate(d):
        if (row,col) in track and mazecpy[row][col]!='X':
            mazecpy[row][col] = 'O'
        

for rows in mazecpy:
    print(rows)