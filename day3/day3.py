
# Kitty Belling
# 2023/12/3

# IMPORT
from aoc_helper import aoc_helper 
chelp = aoc_helper()

# SETUP 
grid = []

# FUNCTION
def create_grid(iLines):
    w = len(iLines[0])
    l = len(iLines)
    global grid
    for i in range(l):
        s = []
        for j in range(w):
            x = iLines[i][j]
            if x.isdigit():
                s.append("d")
            elif x == ".":
                s.append(".")
            else:
                s.append("o")
        grid.append(s.copy())

def parse_grid(iLines):
    global grid
    for i in range(len(iLines)):
        for j in range(len(iLines[0])):
            if grid[i][j] == "d":
                check_valid(i,j,iLines)
                if grid[i][j] != "d":
                    fill_digit(i,j,iLines)

def check_valid(i,j,iLines):
    global grid
    x = iLines[i][j]
    if j < len(iLines) -1:
        if grid[i][j+1].isdigit():
            grid[i][j] = iLines[i][j]
        if grid[i][j+1] == "o":
            grid[i][j] = x 
    if j > 0:
        if grid[i][j-1].isdigit():
            grid[i][j] = iLines[i][j]
        if grid[i][j-1] == "o":
            grid[i][j] = x 
    if i > 0:
        if grid[i-1][j] == "o":
            grid[i][j] = iLines[i][j]
        if j > 0:
            if grid[i-1][j-1] == "o":
                grid[i][j] = iLines[i][j]
        if j < len(iLines) - 1:
            if grid[i-1][j+1] == "o":
                grid[i][j] = iLines[i][j] 
    if i < len(iLines)-1: 
        if grid[i+1][j] == "o":
            grid[i][j] = iLines[i][j]
        if j > 0:
            if grid[i+1][j-1] == "o":
                grid[i][j] = iLines[i][j]
        if j < len(iLines) - 1:
            if grid[i+1][j+1] == "o":
                grid[i][j] = x

def fill_digit(i,j,iLines):
    global grid
    done = False 
    g = j 
    while not done:
        g -= 1 
        try:
            if grid[i][g] == "d": 
                grid[i][g] = iLines[i][g]
            else:
                done = True
        except:
            done = True
    done = False
    g = j 
    while not done:
        g += 1
        try:
            if grid[i][g] == "d":
                grid[i][g] = iLines[i][g]
            else:
                done = True
        except:
            done = True

def calculate_grid():
    global grid 
    numbers = []
    g = []
    for row in grid:
        s = ""
        for i in row:
            s += i 
        g.append(s) 
    for r in g:
        x = r.replace("o",".")
        x = x.replace("d",".")
        x = x.replace("."," ")
        split = x.split()
        numbers += split 
    s = get_sum(numbers)
    return s, numbers

def get_sum(numbers):
    s = 0
    for n in numbers:
        s += int(n)
    return s



# MAIN
iLines = chelp.get_input_text("input.txt")

# Part 1

create_grid(iLines)
#for g in grid:
#    print(g)

print("")

parse_grid(iLines)
for g in grid:
    print(g)

s, numbers = calculate_grid()
print("Numbers:\t", numbers) 
print("Sum:\t\t", s)
