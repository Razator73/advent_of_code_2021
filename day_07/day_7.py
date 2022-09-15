from math import ceil, floor
from statistics import median, fmean

with open('day_07/crabs.txt') as f:
    crab_positions = [int(num) for num in f.read().strip().split(',')]

# part 1
median_position = int(median(crab_positions))
fuel_consumption = sum([abs(pos - median_position) for pos in crab_positions])
print(fuel_consumption)


# part 2
def sum_n_numbers(n):
    return (n * n + n) // 2


mean_pos = fmean(crab_positions)
fuel_consumption = min(sum([sum_n_numbers(round(abs(pos - ceil(mean_pos)))) for pos in crab_positions]),
                       sum([sum_n_numbers(round(abs(pos - floor(mean_pos)))) for pos in crab_positions]))
print(fuel_consumption)

