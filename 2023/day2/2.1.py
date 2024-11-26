"""
https://adventofcode.com/2023/day/2

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
"""

# 1. Parse File
# Each line has Game #: with a list of ;-separated games. 
# Red, greeen, and blue are optional. Can't guarantee format # red # green # blue
# Output: dict of {key=game_id : [max_red, max_green, max_blue]} where max was the highest encountered num cubes of that color. 

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
        
        # [max_green, max_blue, max_red] from all rolls in that game
        games[id] = [maxG, maxB, maxR]
        print(games[id])
            
# 2. Iterate through dict keys
# if all 3 list vals for that key are less than the input, add key to the running total.

# Vals from the puzzle description
actual_r, actual_g, actual_b = 12, 13, 14

# Sum of valid game IDs
output = 0

# Is there a better way to iter through a dict to get key and values together?
for i in games:
    game = games[i]
    if game[0] <= actual_g and game[1] <= actual_b and game[2] <= actual_r:
        output += i

print(output)