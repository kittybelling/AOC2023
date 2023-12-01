
# IMPORT
from aoc_helper import aoc_helper 
chelp = aoc_helper()

# SETUP 
line_outputs = []

# FUNCTION
def get_first_number(instr):
    #for i in instr:
    #    if i.isdigit():
    #        return i
    for i in range(len(instr)):
        if instr[i].isdigit():
            return instr[i]
        else:
            l = check_for_spelled_letter(instr[i:])
            if l != "":
                return l

def check_for_spelled_letter(instr):
    if len(instr) >= 3:
        #print(instr[0:3])
        if instr[0:3] == "one":
            return "1"
        elif instr[0:3] == 'two':
            return "2"
        elif instr[0:3] == "six":
            return "6"
    if len(instr) >= 4:
        if instr[0:4] == "four":
            return "4"
        elif instr[0:4] == "five":
            return "5"
        elif instr[0:4] == "nine":
            return "9"
    if len(instr) >= 5:
        if instr[0:5] == "three":
            return "3"
        elif instr[0:5] == "seven":
            return "7"
        elif instr[0:5] == "eight":
            return "8"
    return ""
    

def get_last_number(instr):
    for i in range(len(instr)):
        j = len(instr) - i - 1
        if instr[j].isdigit():
            return instr[j]
        else:
            l = check_for_spelled_letter(instr[j:])
            if l != "":
                return l

# MAIN
iLines = chelp.get_input_text("input.txt")
#print(iLines)

for line in iLines:
    f = get_first_number(line)
    l = get_last_number(line) 
    #print("Line: ", line, "; First Num: ", f, "; Last Num: ",l)
    o = f + l 
    #print(o)
    line_outputs.append(o)

print(line_outputs)

s = 0
for o in line_outputs:
    s += int(o)

print(s)



