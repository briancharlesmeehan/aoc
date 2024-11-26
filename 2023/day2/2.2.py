"""
https://adventofcode.com/2023/day/2

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""

# 1. Parse File
# Each line has Game #: with a list of ;-separated games. 
# Red, greeen, and blue are optional. Can't guarantee format # red # green # blue
# Output: dict of {key=game_id : power} where max was the highest encountered num cubes of that color. 

# Calculate power by multiplying max_red * max_green * max_blue

games = {}

# Helper function to parse cubes per roll
# For convention/speed, [green=0, blue=1, red=2] 
def parse_roll(roll):
    scores = [0] * 3
    
    # Parse green
    idx = -1
    try:
        idx = roll.index("green")
    except:
        pass
    
    if idx >= 0:
        cube_str = ""
        i = idx - 2
        while i >= 0 and roll[i] != ',':
            cube_str = roll[i] + cube_str
            i -= 1
        scores[0] = int(cube_str)
    
    # Parse blue
    idx = -1
    try:
        idx = roll.index("blue")
    except:
        pass
    
    if idx >= 0:
        cube_str = ""
        i = idx - 2
        while i >= 0 and roll[i] != ',':
            cube_str = roll[i] + cube_str
            i -= 1
        scores[1] = int(cube_str)

    # Parse red
    idx = -1
    try:
        idx = roll.index("red")
    except:
        pass
    
    if idx >= 0:
        cube_str = ""
        i = idx - 2
        while i >= 0 and roll[i] != ',':
            cube_str = roll[i] + cube_str
            i -= 1
        scores[2] = int(cube_str)
    
    return scores



with open("/Users/brianmeehan/Repos/aoc/2023/day2/input.txt", "r") as f:
    for line in f:
        # Grab game ID
        start = line.index(" ")
        end = line.index(":")
        id = int(line[start+1:end])

        # Parse games
        rolls = []

        start = end + 2
        while True:
            try:
                end = line.index(";", start)
            except:
                # Last game
                roll = line[start:len(line)]
                rolls.append(parse_roll(roll))
                break

            roll = line[start:end]
            rolls.append(parse_roll(roll))

            start = end + 2
        
        # Find max value per color across all game rolls
        maxR, maxG, maxB = 0, 0, 0
        for r in rolls:
            if r[0] > maxG:
                maxG = r[0]
            if r[1] > maxB:
                maxB = r[1]
            if r[2] > maxR:
                maxR = r[2]
        
        # Calculate power of min needed per color
        games[id] = maxG * maxB * maxR
            
# 2. Iterate through dict keys
# if all 3 list vals for that key are less than the input, add key to the running total.

# Sum of valid game IDs
output = 0

# Is there a better way to iter through a dict to get key and values together?
for i in games:
    power = games[i]
    output += power

print(output)