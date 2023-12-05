
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

def get_score(c,winners,hand):
	count = 0
	for h in hand:
		if h in winners:
			count += 1
	return count

def get_copies(cards):
	copies = create_copies_list(cards) 
	for [c,w,h] in cards:
		# print("Card: ",c)
		sc = get_score(c,w,h)
		# print("Score: ",sc)
		for l in range(copies[c-1][1]+1): 
			i = c 
			# print("COPY: ",l)
			for j in range(sc):
				# print("Copying card: ",i)
				copies[i][1] = copies[i][1] + 1 
				i += 1
	t = []
	for [index,count] in copies:
		t.append([index,count+1])
	return t

def create_copies_list(cards):
	copies = []
	for [c,w,h] in cards:
		copies.append([c,0])
	return copies

def count_scratchcards(copies):
	osum = 0 
	for [i,c] in copies:
		osum += c 
	return osum

# MAIN
iLines = chelp.get_input_text("input.txt")

cards = break_lines(iLines)

# for [c,w,h] in cards:
# 	print("Card: ",c)
# 	print("Winning Numbers: ",w)
# 	print("Numbers in Hand: ",h)
# 	print("")

# score = get_score(cards)

# print(score)

copies = get_copies(cards)

# for c in copies:
# 	print(c)
# print("")

result = count_scratchcards(copies)

print("RESULT:\t",result)