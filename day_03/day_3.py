with open('day_3/binary.txt') as f:
    binary_lines = f.readlines()

split_bits = []
for line in binary_lines:
    split_bits.append([int(c) for c in line.strip()])
lines = len(split_bits)


def convert_binary(bits):
    bits = bits[::-1]
    number = 0
    for i in range(len(bits)):
        number += 2 ** i * bits[i]
    return number


# part 1
gamma = []
epsilon = []
for i in range(len(split_bits[0])):
    bit_sum = sum([b[i] for b in split_bits])
    if bit_sum > lines / 2:
        gamma.append(1)
        epsilon.append(0)
    elif bit_sum < 500:
        gamma.append(0)
        epsilon.append(1)
    else:
        print(i)

gamma_decimal = convert_binary(gamma)
epsilon_decimal = convert_binary(epsilon)
print(f'{gamma_decimal} * {epsilon_decimal} = {gamma_decimal * epsilon_decimal}')

# part 2
oxy_gen_rating = split_bits[:]
carbon_scrub_rating = split_bits[:]
for i in range(len(split_bits[0])):
    oxy_len = len(oxy_gen_rating)
    car_len = len(carbon_scrub_rating)
    if oxy_len > 1:
        bit_sum = sum([b[i] for b in oxy_gen_rating])
        keep_bit = 1 if bit_sum >= oxy_len / 2 else 0
        oxy_gen_rating = [b for b in oxy_gen_rating if b[i] == keep_bit]
    if car_len > 1:
        bit_sum = sum([b[i] for b in carbon_scrub_rating])
        keep_bit = 1 if bit_sum < car_len / 2 else 0
        carbon_scrub_rating = [b for b in carbon_scrub_rating if b[i] == keep_bit]
oxy_rating = convert_binary(oxy_gen_rating[0])
carbon_rating = convert_binary(carbon_scrub_rating[0])
print(f'{oxy_rating} * {carbon_rating} = {oxy_rating * carbon_rating}')
