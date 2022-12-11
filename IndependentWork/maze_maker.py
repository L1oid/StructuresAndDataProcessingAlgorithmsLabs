from PIL import Image
import random
import time

print("Enter width: ")
width = int(input())
print("Enter height: ")
height = int(input())
bigger_dimension = width if width > height else height


def generate_blank_maze(w, h):
    maze = [[0 for i in range(w)] for i2 in range(h)]
    entrance_x, exit_x = random.randint(1, width - 2), random.randint(1, width - 2)
    maze[0][entrance_x] = 1
    maze[1][entrance_x] = 1
    maze[-1][exit_x] = 1
    maze[-2][exit_x] = 1
    return (maze, entrance_x, exit_x)


def make_main_path():
    start = time.time()
    x = entrance_x
    y = 1
    while not next_to_goal(x, y):
        x, y = move_in_maze(x, y)
        if (time.time() - start) > bigger_dimension / 100:
            return False
    return True


def next_to_goal(x, y):
    return (abs(x - exit_x) == 1 and y == height - 2) or (abs(y - height + 2) == 1 and x - exit_x == 0)


def ones_around(x, y):
    total = 0
    if maze[y + 1][x] == 1:
        total += 1
    if maze[y - 1][x] == 1:
        total += 1
    if maze[y][x + 1] == 1:
        total += 1
    if maze[y][x - 1] == 1:
        total += 1
    return total


def move_in_maze(x, y):
    moves = []
    if x > 1 and (next_to_goal(x - 1, y) or ones_around(x - 1, y) < 2):
        moves.append((-1, 0))
    if x < width - 2 and (next_to_goal(x + 1, y) or ones_around(x + 1, y) < 2):
        moves.append((1, 0))
    if y < height - 2 and (next_to_goal(x, y + 1) or ones_around(x, y + 1) < 2):
        moves.append((0, 1))
    if y > 1 and (next_to_goal(x, y - 1) or ones_around(x, y - 1) < 2):
        moves.append((0, -1))
    if len(moves) == 0:
        global steps
        if (len(steps) > 5):
            for i in range(5):
                steps.pop()
        else:
            steps = [steps[0]]
        return (steps[-1][0], steps[-1][1])
    move = moves[random.randrange(0, len(moves))]
    x2 = x + move[0]
    y2 = y + move[1]
    steps.append((x2, y2))
    maze[y2][x2] = 1
    return (x2, y2)


maze, entrance_x, exit_x = generate_blank_maze(width, height)
steps = []
while not make_main_path():
    maze, entrance_x, exit_x = generate_blank_maze(width, height)
    steps = []


def ones_around_not_mine(x, y, steps_taken):
    total = 0
    if maze[y + 1][x] == 1 and (maze[y + 1][x] not in steps_taken):
        total += 1
    if maze[y - 1][x] == 1 and (maze[y - 1][x] not in steps_taken):
        total += 1
    if maze[y][x + 1] == 1 and (maze[y][x + 1] not in steps_taken):
        total += 1
    if maze[y][x - 1] == 1 and (maze[y][x - 1] not in steps_taken):
        total += 1
    return total


def move_branching_path(x, y, steps_taken):
    moves = []
    if x > 1 and ones_around_not_mine(x - 1, y, steps_taken) < 2:
        moves.append((-1, 0))
    if x < width - 2 and ones_around_not_mine(x + 1, y, steps_taken) < 2:
        moves.append((1, 0))
    if y < height - 2 and ones_around_not_mine(x, y + 1, steps_taken) < 2:
        moves.append((0, 1))
    if y > 1 and ones_around_not_mine(x, y - 1, steps_taken) < 2:
        moves.append((0, -1))
    if len(moves) == 0:
        return (y, x, None, True)
    move = moves[random.randrange(0, len(moves))]
    x = x + move[0]
    y = y + move[1]
    steps_taken.append((x, y))
    if maze[y][x] == 1:
        maze[y][x] = 1
        return (x, y, None, True)
    maze[y][x] = 1
    return (x, y, steps_taken, False)


def empty_spot_here(x, y):
    total = 0
    for yy in range(y - 1, y + 2):
        for xx in range(x - 1, x + 2):
            total += maze[yy][xx]
    return total == 0


for y in range(2, height - 2, 3):
    for x in range(2, width - 2, 3):
        if empty_spot_here(x, y):
            xx, yy, steps_taken, done = x, y, [], False
            maze[yy][xx] = 1
            while not done:
                xx, yy, steps_taken, done = move_branching_path(xx, yy, steps_taken)


def fill_crack(x, y):
    s = maze[y][x] + maze[y + 1][x] + maze[y][x + 1] + maze[y + 1][x + 1]
    if s == 0:
        if (maze[y - 1][x] == 0 or maze[y - 1][x + 1] == 0) and (maze[y][x - 1] == 1 or maze[y][x + 2] == 1):
            maze[y][x] = 1
            maze[y][x + 1] = 1
        elif (maze[y + 2][x] == 0 or maze[y + 2][x + 1] == 0) and (maze[y + 1][x - 1] == 1 or maze[y + 1][x + 2] == 1):
            maze[y + 1][x] = 1
            maze[y + 1][x + 1] = 1
        elif (maze[y][x - 1] == 0 or maze[y + 1][x - 1] == 0) and (maze[y - 1][x] == 1 or maze[y + 2][x] == 1):
            maze[y][x] = 1
            maze[y + 1][x] = 1
        elif maze[y][x + 2] == 0 or maze[y + 1][x + 2] == 0:
            maze[y][x + 1] = 1
            maze[y + 1][x + 1] = 1
    elif s == 4:
        if maze[y][x - 1] == 0 and maze[y - 1][x] == 0:
            maze[y][x] = 0
        if maze[y][x + 2] == 0 and maze[y - 1][x + 1] == 0:
            maze[y][x + 1] = 0
        if maze[y + 1][x - 1] == 0 and maze[y + 2][x] == 0:
            maze[y + 1][x] = 0
        if maze[y][x + 2] == 0 and maze[y + 2][x + 1] == 0:
            maze[y + 1][x + 1] = 0


for y in range(1, height - 2):
    for x in range(1, width - 2):
        fill_crack(x, y)


def create_image(w, h):
    image = Image.new("1", (w, h), "black")
    return image

img = create_image(width, height)
for y in range(height):
    for x in range(width):
        img.putpixel((x, y), maze[y][x])

i = 0
while True:
    p = str(width) + "x" + str(height) + "_" + str(i) + ".png"
    try:
        tmp = Image.open(p)
        tmp.close()

    except:
        break
    i += 1

path = str(width) + "x" + str(height) + "_" + str(i) + ".png"
img.save(path)
img.show()
