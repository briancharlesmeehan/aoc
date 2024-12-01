path = '/home/brian/repos/aoc/2024/day1/input.txt'

"""
Two collated lists - each line has 1 elem from each list. Unordered.

1. Convert into 2 lists

2. Sort each list

3. Match up and calc distance between sorted list elems

4. Return total sum of distances
"""

# Parse text into 2 lists
list_1, list_2 = [], []

with open(path, 'r') as f:
    for line in f:
        space_idx = line.index(' ')

        elem_1 = int(line[0:space_idx])
        # Tried line[x:-1] first.
        elem_2 = int(line[(space_idx+3):len(line)])

        list_1.append(elem_1)
        list_2.append(elem_2)

# Sort lists
list_1.sort()
list_2.sort()

# Calc distance between matching elems
total_distance = 0

for i in range(len(list_1)):
    distance = abs(list_1[i]-list_2[i])
    total_distance += distance

print(total_distance)
