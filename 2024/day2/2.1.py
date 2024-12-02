path = '/home/brian/repos/aoc/2024/day2/input.txt'

"""
1. Parse all lines into lists.
2. Iterate over all items in each list.
    After first gap. if same, unsafe. 
    if increasing, set increasing flag to only check for increasing going fwd.
    if gap >= 4 unsafe.
3. For rest of list, check if adjacent gap is same or >=4 -> unsafe. 
    And check if gap matches existing direction.
"""

reports = []

with open(path, 'r') as f:
    for line in f:
        # Need to assign back to line. 
        line = line.removesuffix('\n')
        report = line.split(' ')
        for i in range(len(report)):
            report[i]= int(report[i])
        reports.append(report)

num_safe_reports = 0

for r in reports:
    is_increasing = False
    is_safe = True
    for i in range(1, len(r)):
        # Find direction of the report levels
        if i == 1 and r[i] > r[i-1]:
            is_increasing = True

        # Distance between levels
        dist = r[i] - r[i-1]
        if dist == 0 or abs(dist) > 3:
            is_safe = False
            break
        
        # Need to check both violations, increase or decrease
        # example that found the bug [1 -1 2 4 6]
        if (is_increasing and dist < 0) or (not is_increasing and dist > 0):
            is_safe = False
            break
    if is_safe:
        num_safe_reports += 1

print(num_safe_reports)