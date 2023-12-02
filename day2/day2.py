
# Kitty Belling

# IMPORT
from aoc_helper import aoc_helper 
chelp = aoc_helper()

# SETUP 
bag = [12,13,14]    # R,G,B

# FUNCTION
def sum_possible_lines(Lines):
    global bag 
    s = 0
    for line in Lines:
        num, split_draws = break_line(line)
        valid = True
        for draw in split_draws:
            color_split = draw.split(",")
            for color in color_split:
                if "blue" in color:
                    c = color.replace("blue","")
                    c = c.strip()
                    if int(c) > bag[2]:
                        valid = False 
                        break
                elif "red" in color:
                    c = color.replace("red","")
                    c = c.strip()
                    if int(c) > bag[0]:
                        valid = False 
                        break
                elif "green" in color:
                    c = color.replace("green","")
                    c = c.strip()
                    if int(c) > bag[1]:
                        valid = False 
                        break
            if not valid:
                break 
        if valid:
            s += int(num)
    return s

def break_line(line):
    [game,draws] = line.split(":")
    try:
        num = game.replace("Game ","") 
    except:
        print("ERROR #1: Cannot extract game number")
    draws = draws.strip()
    split_draws = draws.split(";")
    return num, split_draws



# MAIN
iLines = chelp.get_input_text("input.txt")
s = sum_possible_lines(iLines)
print(s)

