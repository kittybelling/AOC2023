
# Kitty Belling
# 2023/12/01

import os 

class aoc_helper:

    def get_input_text(self,fname,fpath=""):
        if fpath != "":
            os.chdir(fpath)
        with open(fname,"r") as f:
            Lines = f.readlines()
        for i in range(len(Lines)): 
            l = Lines[i]
            l = l.strip()
            Lines[i] = l
        return Lines
