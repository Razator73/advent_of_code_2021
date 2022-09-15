with open('day_1/depths.txt') as f:
    depth_data = [int(x.strip()) for x in f.readlines()]
data_len = len(depth_data)

# part 1
increases = 0
for i in range(1, data_len):
    if depth_data[i] > depth_data[i - 1]:
        increases += 1
print(increases)

# part 2
pre = 0
increases = -1
for i in range(2, data_len):
    cur = depth_data[i] + depth_data[i - 1] + depth_data[i - 2]
    if cur > pre:
        increases += 1
    pre = cur
print(increases)
