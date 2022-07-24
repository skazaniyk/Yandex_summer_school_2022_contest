from collections import deque


def find_start(array, n, m):
    position = None
    for row in range(n):
        for column in range(m):
            if array[row][column] == 'S':
                position = (row, column)
                break
        if position != None:
            break
    return position

def way_back(x, y):
    if x == 1 and y == 0:
        return 'R'
    elif x == -1 and y == 0:
        return 'L'
    elif x == 0 and y == -1:
        return 'U'
    else:
        return 'D'

def paint_map(array, n, m):
    start_position = find_start(maze, n, m)
    my_deque = deque()
    my_deque.append(start_position)
    while my_deque:
        current_position = my_deque.popleft()
        for delta_x, delta_y in (
                (1, 0),
                (-1, 0),
                (0, -1),
                (0, 1),
        ):
            new_y = current_position[0] + delta_y
            new_x = current_position[1] + delta_x
            if not array[new_y][new_x] == '.':
                continue

            array[new_y] = array[new_y][:new_x] + way_back(delta_x, delta_y) + array[new_y][new_x + 1:]

            my_deque.append((new_y, new_x))


n, m = [int(i) for i in input().split()]
maze = []

for i in range(n):
    maze.append(input())

start = find_start(maze, n, m)

paint_map(maze, n, m)

for row in maze:
    print(row)
