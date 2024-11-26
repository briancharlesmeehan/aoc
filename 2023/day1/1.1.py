output = 0

# Read from input file
with open('/Users/brianmeehan/Repos/aoc/2023/day1/input.txt', 'r') as f:
    for line in f:
        num_str = ""
        
        for c in line:
            try:
                i = int(c)
            except:    
                continue
            num_str += c

        # Take first and last numerical chars
        first = num_str[0]
        last = num_str[-1]

        # Convert to number 
        cal_val = int(first+last)

        # Add calibration value to total
        output += cal_val

print(output)
