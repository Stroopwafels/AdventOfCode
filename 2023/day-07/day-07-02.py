from itertools import groupby

# file_location = "day-07_example.txt"
file_location = "day-07_input.txt"


def part02(file_location):
	with open(file_location) as puzzle_input:
		score_bet_list = []
		for line in puzzle_input:
			hand, bet = line.split()
			score = get_hand_score(hand)
			score_bet_list.append([score, hand, int(bet)])
	score_bet_list.sort()

	total_winnings = 0
	for i, score_bet in enumerate(score_bet_list):
		total_winnings += (i+1) * score_bet[-1]

	print("part02| The total winnings are:", total_winnings)


def get_hand_score(hand):
	return get_hand_rank(hand) * 0x100000 + get_hand_power(hand)

def get_hand_power(hand):
	card_order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
	multiplier = 1
	power = 0
	for card in reversed(hand):
		power += multiplier * card_order.index(card)
		multiplier *= 0x10
	return power

def get_hand_rank(hand):
	hand_groups = [list(y) for x, y in groupby(sorted(hand))]
	hand_groups.sort(key=len, reverse=True)

	# Jokers must be added to the largest non-joker group for maximum score
	for i, group in enumerate(hand_groups):
		if "J" in group:
			if not len(group) == 5: # nothing needs to be done if the hand is jokers only
				hand_groups[0] += hand_groups.pop(i)

	match len(hand_groups):
		case 5:
			return 0 # High card
		case 4:
			return 1 # One pair
		case 3:
			if len(hand_groups[0]) == 2:
				return 2 # Two of a kind
			else:
				return 3 # Three of a kind
		case 2:
			if len(hand_groups[0]) == 3:
				return 4 # Full house
			else:
				return 5 # Four of a kind
		case 1:
			return 6 # Five of a kind


part02(file_location)