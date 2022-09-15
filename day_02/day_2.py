with open('day_2/directions.txt') as f:
    dir_data = [direction.strip().split(' ') for direction in f.readlines()]
dir_data = [(x[0], int(x[1])) for x in dir_data]

# part 1
loc = [0, 0]
dir_map = {'forward': (0, 1), 'up': (1, -1), 'down': (1, 1)}
for command in dir_data:
    loc[dir_map[command[0]][0]] += dir_map[command[0]][1] * command[1]
print(loc)
print(loc[0] * loc[1])

# part 2
loc = [0, 0]
aim = 0
for command in dir_data:
    if command[0] == 'forward':
        loc[0] += command[1]
        loc[1] += command[1] * aim
    elif command[0] == 'down':
        aim += command[1]
    elif command[0] == 'up':
        aim -= command[1]
print(loc)
print(loc[0] * loc[1])
