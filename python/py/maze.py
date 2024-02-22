import time
import queue 


maze = [
['#','#','#','#','#','#','#','#','#','#','#','#'],
['#','O',' ',' ',' ',' ',' ',' ','#','#','#','#'],
['#',' ','#','#','#',' ','#',' ','#','#',' ','#'],
['#',' ','#',' ',' ',' ','#',' ','#',' ',' ','#'],
['#',' ','#','#','#',' ','#',' ','#','#',' ','#'],
['#',' ','#','#','#',' ','#',' ','#','#',' ','#'],
['#',' ','#','#','#','X','#',' ','#','#',' ','#'],
['#',' ',' ',' ','#','#','#',' ',' ',' ',' ','#'],
['#','#','#',' ','#','#','#',' ','#','#','#','#'],
['#',' ','#',' ','#',' ',' ',' ','#','#','#','#'],
['#',' ',' ',' ','#','#','#',' ','#','#','#','#'],
['#','#','#','#','#','#','#','#','#','#','#','#']]


def find_start(maze):
    for index, row in enumerate(maze):
        for row_index, val in enumerate(row):
            if val == 'O':
                return (index,row_index)
    return None

def find_neighbors(maze,pos):
    neighbors = []

    if pos[1]-1>0:
        neighbors.append((pos[0],pos[1]-1))
    if pos[1]+1<len(maze)-1:
        neighbors.append((pos[0],pos[1]+1))
    if pos[0]+1<len(maze[0])-1:
        neighbors.append((pos[0]+1,pos[1]))
    if pos[0]-1>0:
        neighbors.append((pos[0]-1,pos[1]))

    return neighbors

def find_path(maze,que,cur_path,pos, seen):
    neighbors = find_neighbors(maze,pos)
    for cords in neighbors:
        if maze[cords[0]][cords[1]]=='#' or maze[cords[0]][cords[1]] in seen:
            continue
        que.put(cords,cur_path)
        set.add(cords)

    return        

testqueue = queue.Queue()
testqueue.put((1,2),[(1,2),(1,3)])
position = testqueue.get()
track = testqueue.get()
print(position,track)

start = find_start(maze)
cur_path=[]
cur_path.append(start)
qu = queue.Queue()
