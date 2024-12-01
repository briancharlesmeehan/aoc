from collections import defaultdict


path = '/home/brian/repos/aoc/2024/day1/input.txt'

"""
Two collated lists - each line has 1 elem from each list. Unordered.

1. Convert into 2 lists

2. Count number of each elem in list 2, using hashmap

3. Iterate through list 1. For each elem, use hashmap num repeats to calc similarity score.

4. Return total sim score.
"""

# Parse text into 2 lists
list_1, list_2 = [], []

with open(path, 'r') as f:
    for line in f:
        space_idx = line.index(' ')

        elem_1 = int(line[0:space_idx])
        elem_2 = int(line[(space_idx+3):len(line)])

        list_1.append(elem_1)
        list_2.append(elem_2)

# Use defaultdict so that empty map keys return 0 instead of None.
dict = defaultdict(int)

# Track number of each elem in list_2
for i in range(len(list_1)):
    elem = list_2[i]
    dict[elem] += 1

sim_score = 0

for i in range(len(list_1)):
    elem = list_1[i]
    num_repeats = dict[elem]
    sim_score += elem * num_repeats

print(sim_score)