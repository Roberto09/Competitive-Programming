import random
import pprint
import time

# small sample maze
maze = ['.....',
        '...#.',
        '.#...',
        '.#.#.',
        '.#...']
# convert to boolean maze
maze_bin = [[True if cell == '.' else False for cell in line] for line in maze]

#print (maze_bin)


# uncomment to generate a random maze
# maze_size = 500
# threshold = 0.2
# maze_bin = [[1 if random.random() >= threshold else 0 for _ in range(maze_size)] for _ in range(maze_size)]

# take start time
t1 = time.time()

# rotate the maze (first column becomes first row, first row becomes first column)
maze_bin_rot = [[maze_bin[i][j] for i in range(len(maze_bin))] for j in range(len(maze_bin[0]))]

print(maze_bin_rot)
"""

# horizontal_lengths is a two-dimensional list that contains the number of possible steps to the right for every cell.
horizontal_lengths = []
for line in maze_bin:
    num = 0
    line_lengths = []
    for i in reversed(line):
    	print(i)
        line_lengths.append(i*num)
        num = i * (num + i)
    horizontal_lengths.append(tuple(reversed(line_lengths)))

print(horizontal_lengths)
print(False*1)





# vertical_lengths is a two-dimensional list that contains the number of possible steps to the bottom for every cell.
vertical_lengths_rot = []
for line in maze_bin_rot:
    num = 0
    line_lengths = []
    for i in reversed(line):
        line_lengths.append(i*num)
        num = i * (num + i)
    vertical_lengths_rot.append(tuple(reversed(line_lengths)))
# do the rotation again to be back in normal coordinates
vertical_lengths = [[vertical_lengths_rot[i][j] for i in range(len(vertical_lengths_rot))] for j in range(len(vertical_lengths_rot[0]))]

# calculate the maximum size of a square that has it's upper left corner at (x, y).
# this is the minimum of the possible steps to the right and to the bottom.
max_possible_square = []
for y in range(len(maze_bin)):
    line = []
    for x in range(len(maze_bin[0])):
        line.append(min(horizontal_lengths[y][x], vertical_lengths[y][x]))
    max_possible_square.append(line)

# search for squares
results = []
max_size_square = (-1, -1, -1)
for y in range(len(max_possible_square)):
    for x in range(len(max_possible_square[0])):
        # start with maximum possible size and decrease size until a square is found.
        for size in reversed(range(1, max_possible_square[y][x]+1)):
            # look at the upper right (x+size,y) and bottom left corner (x,y+size).
            # if it's possible to make at least size steps to the right from the bottom left corner
            # and at least size steps to the bottom from the upper right corner, this is a valid square.
            if horizontal_lengths[y+size][x] >= size and vertical_lengths[y][x+size] >= size:
                results.append((x, y, size+1))
                if size+1 > max_size_square[2]:
                    max_size_square = (x, y, size+1)
                # break after the the largest square with upper left corner (x,y) has been found.
                break

t2 = time.time()

# comment this print section if you use larger grids
print('Maze:')
pprint.pprint(maze_bin)
print('\n')
print('Horizontal possible steps:')
pprint.pprint(horizontal_lengths)
print('\n')
print('Vertical possible steps:')
pprint.pprint(vertical_lengths)
print('\n')
print('Maximum possible size of square:')
pprint.pprint(max_possible_square)
print('\n')
print('Results:')
for square in results:
    print('Square: x={}, y={}, size={}'.format(*square))
print('\n')

# final results
print('Finished after {:.3f} seconds.'.format(t2-t1))
print('Result: {} squares found, maximum square (x={}, y={}, size={}).'.format(len(results), *max_size_square))



"""










































































