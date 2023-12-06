import re

def part01():
	with open("day-04_input.txt") as puzzle_input:
		score = 0

		###
		contains_double_win_nrs = 0

		for line in puzzle_input:

			numbers_win = get_numbers_win(line)
			numbers_lot = get_numbers_lot(line)
			# print(numbers_win)
			# print(numbers_lot)

			winning_numbers = calculate_wins(numbers_win, numbers_lot)

			# print("Wins: " + str(winning_numbers))
			if winning_numbers:
				round_score = 2**(winning_numbers-1)
				score += round_score
				# print("Score: " + str(round_score))
			# else:
				# print("Score: 0")

		print("The answer of part 01 is: " + str(score))

		if contains_double_win_nrs:
			print("this data set contains double win nrs")

def part02():
	target_file = "day-04_input.txt"
	ticket_counter = []

	with open(target_file) as puzzle_input:
		for line in puzzle_input:
			ticket_counter.append(1)
		
		# print(len(ticket_counter))
	with open(target_file) as puzzle_input:
		for i, line in enumerate(puzzle_input):
			# print(line)
			wins = calculate_wins(get_numbers_win(line), get_numbers_lot(line))
			# print(wins)
			for x in range(1, wins+1):
				if i+x < len(ticket_counter):
					ticket_counter[i+x] += ticket_counter[i]
		# print(ticket_counter)
		print("The answer of part 02 is: " + str(sum(ticket_counter)))
				
			

def get_numbers_win(line):
	number_str_all = line.split(": ")[1] 
	numbers_str_win = number_str_all.split(" | ")[0]
	numbers_win = re.findall(r'\d+', numbers_str_win)
	return numbers_win

def get_numbers_lot(line):
	number_str_all = line.split(": ")[1]
	numbers_str_lot = number_str_all.split(" | ")[1]
	numbers_lot = re.findall(r'\d+', numbers_str_lot)
	return numbers_lot

def calculate_wins(numbers_win, numbers_lot):
	winning_numbers = 0
	# print("Winning numbers: ", end="")
	for i, win_nr in enumerate(numbers_win):
		if win_nr in numbers_lot:
			# print(win_nr, end=", ")
			winning_numbers += 1
	# print("")
	return winning_numbers


part01()
part02()