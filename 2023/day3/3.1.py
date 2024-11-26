"""
https://adventofcode.com/2023/day/3

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""

# 1. Load input into a matrix [["", "", ""], ["", ]] where each text line is a row

"""
Example Input

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

becomes [["4", "6", "7", ...], [".", ".", ".", "*", ...], ...]
"""

schematic = []
with open("/Users/brianmeehan/Repos/aoc/2023/day3/input.txt", "r") as f:
    for line in f:
        line = line.removesuffix('\n')
        schematic.append(line)


# Iterate through a line. Once you see a number, find entire number (how long is it?)
# Start a "found a symbol" tracker
# for each number schematic[line[i]], check all 9 adjacent tiles for a symbol
# if we found a symbol for this number, add to running total. 
# Return total

part_number_total = 0

for i in range(len(schematic)):
    row = schematic[i]
    j = 0
    while j < len(row):
        
        # Check for start of a number
        num_str = ""
        start = j
        try: 
            num = int(row[j])
            num_str = row[j]
        except:
            j += 1
            continue

        # Find entire number
        end = start + 1
        e = None
        while end < len(row) and e is None:
            try:
                num_str += row[end]
                num = int(num_str) # check if adding a char is still a number
            except Exception as exception:
                end -= 1
                e = exception
                break
            end += 1
        
        # Entire number
        num_str = row[start:end+1]

        # Check for symbols adjacent to row[start:end]
        found_symbol = False

        # Check to the left of the number
        if start > 0:
            if row[start - 1] != '.':
                found_symbol = True
        
        # Check to the right 
        if end + 1 < len(row) and not found_symbol:
            if row[end + 1] != '.':
                found_symbol = True

        # Check row above [start-1, end+1]
        if i - 1 >= 0 and not found_symbol:
            above_row = schematic[i-1]
            for idx in range(start-1, end+2):
                if idx >= 0 and idx < len(above_row) and above_row[idx] != '.':
                    found_symbol = True
                    break

        # Check row below [start-1, end+1]
        if i + 1 < len(schematic) and not found_symbol:
            below_row = schematic[i+1]
            for idx in range(start-1, end+2):
                if idx >= 0 and idx < len(below_row) and below_row[idx] != '.':
                    found_symbol = True
                    break

        if found_symbol:
            part_number_total += int(num_str)

        j = end + 1

print(part_number_total)