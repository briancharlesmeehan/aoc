"""
Your calculation isn't quite right. It looks like some of the digits are actually
spelled out with letters: one, two, three, four, five, six, seven, eight, and nine
also count as valid "digits".

Equipped with this new information, you now need to find the real first and last
digit on each line.
"""
output = 0

# Dictionary for quick lookup of valid digit strings
digit_dict = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}



# Read from input file
with open('/Users/brianmeehan/Repos/aoc/2023/day1/input.txt', 'r') as f:
    for line in f:
        num_str = "" # store all found numbers 
        letters = "" # store temp line of potential char matches
        
        i = 0
        for i in range(len(line)):
            # If num char, reset word matching and add to found numbers
            try:
                num = int(line[i])
                num_str += line[i]
                print("found digit: " + line[i])
            except:
                # From this start, try to find a dict match
                j = i
                letters = ""
                while j < len(line) and len(letters) < 6:
                    letters += line[j]
                    print(letters)
                    if digit_dict.get(letters) is not None:
                        print("dict match: " + digit_dict.get(letters))
                        num_str += digit_dict.get(letters)
                    j += 1

        # Take first and last numerical chars
        first = num_str[0]
        last = num_str[-1]

        # Convert to number 
        cal_val = int(first+last)

        # Add calibration value to total
        output += cal_val

print(output)
