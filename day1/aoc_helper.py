
import os 

class aoc_helper:

    def get_input_text(fname,fpath=""):
        if fpath != "":
            os.chdir(fpath)
        with open(fname,"r") as f:
            Lines = f.readlines()
        return Lines
