
# IMPORT
from aoc_helper import aoc_helper 
chelp = aoc_helper()

# SETUP 
line_outputs = []

# FUNCTION
def get_first_number(instr):
    for i in instr:
        if i.isdigit():
            return i

def get_last_number(instr):
    for i in range(len(instr)):
        j = len(instr) - i - 1
        if instr[j].isdigit():
            return instr[j]

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

#print(line_outputs)

s = 0
for o in line_outputs:
    s += int(o)

print(s)



