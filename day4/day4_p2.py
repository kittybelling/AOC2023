
# Kitty Belling
# 2023/12/04

# IMPORT
from aoc_helper import aoc_helper 
chelp = aoc_helper()

# SETUP 


# FUNCTION
def break_lines(iLines):
	output = []
	for line in iLines: 
		[card, numbers] = line.split(":") 
		[trash, card_num] = card.split()
		[winning, hand] = numbers.split(" | ")
		winning = winning.strip() 
		hand = hand.strip()
		w = []
		h = []
		split = winning.split()
		for s in split:
			w.append(int(s))
		split = hand.split()
		for s in split:
			h.append(int(s))
		output.append([int(card_num),w,h])
	return output

def get_score(cards):
	osum = 0
	for [c,winners,hand] in cards:
		count = 0
		for h in hand:
			if h in winners:
				count += 1
		s = calculate_score(count)
		osum += s 
	return osum

def calculate_score(count):
	score = 0
	while count > 0:
		if score == 0:
			score = 1
		else:
			score = score * 2
		count -= 1
	return score


def get_copies(cards):
	copies = create_copies_list(cards) 
	return copies

def create_copies_list(cards):
	copies = []
	for [c,w,h] in cards:
		copies.append([c,0])
	return copies



# MAIN
iLines = chelp.get_input_text("basic_input.txt")

cards = break_lines(iLines)

# for [c,w,h] in cards:
# 	print("Card: ",c)
# 	print("Winning Numbers: ",w)
# 	print("Numbers in Hand: ",h)
# 	print("")

# score = get_score(cards)

# print(score)

copies = get_copies(cards)

for c in copies:
	print(c)