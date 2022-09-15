with open('day_06/fish.txt') as f:
    fish_nums = [int(x) for x in f.read().split(',')]

fish_population = {}
for i in range(-1, 9):
    fish_population[i] = len([f for f in fish_nums if f == i])

# part 1
for day in range(1, 81):
    new_fish_pop = {}
    for i in range(0, 9):
        new_fish_pop[i - 1] = fish_population[i]
    new_fish_pop[8] = new_fish_pop[-1]
    new_fish_pop[6] += new_fish_pop[-1]
    fish_population = new_fish_pop
fish_population[-1] = 0
print(sum([fishes for fishes in fish_population.values()]))

# part 2
for day in range(81, 257):
    new_fish_pop = {}
    for i in range(0, 9):
        new_fish_pop[i - 1] = fish_population[i]
    new_fish_pop[8] = new_fish_pop[-1]
    new_fish_pop[6] += new_fish_pop[-1]
    fish_population = new_fish_pop
fish_population[-1] = 0
print(sum([fishes for fishes in fish_population.values()]))
