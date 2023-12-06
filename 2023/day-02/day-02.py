import re

def part_01():
	benchmark = [12, 13, 14] # resp. Red, Green, and Blue cubes
	counter = 0

	with open("day-02_input.txt") as puzzle_input:
		for line in puzzle_input:
			gamenumber = int(re.findall(r'(?<=Game )\d+', line)[0])
			impossible_game = False
			
			# print("Game " + str(gamenumber) + ": ", end="")

			rounds = (line.split(": ")[1]).split("; ")
			# print(rounds)

			for single_round in rounds:
				reds = re.findall(r'\d+(?= red)', single_round)
				if reds:
					if (int(reds[0]) > benchmark[0]):
						impossible_game = True
				greens = re.findall(r'\d+(?= green)', single_round)
				if greens:
					if (int(greens[0]) > benchmark[1]):
						impossible_game = True
				blues = re.findall(r'\d+(?= blue)', single_round)
				if blues:
					if (int(blues[0]) > benchmark[2]):
						impossible_game = True

			if not impossible_game:
				counter += gamenumber
			# 	print("This game is possible. Counter is: " + str(counter))
			# else:
			# 	print("")

		print("The answer for part 01 is: " + str(counter))

def part_02():
	counter = 0

	with open("day-02_input.txt") as puzzle_input:
		for line in puzzle_input:
			gamenumber = int(re.findall(r'(?<=Game )\d+', line)[0])
			red_min = 0
			green_min = 0
			blue_min = 0

			rounds = (line.split(": ")[1]).split("; ")

			for single_round in rounds:
				reds = re.findall(r'\d+(?= red)', single_round)
				for i in reds:
					if int(i) > red_min:
						red_min = int(i)

				greens = re.findall(r'\d+(?= green)', single_round)
				for i in greens:
					if int(i) > green_min:
						green_min = int(i)
				blues = re.findall(r'\d+(?= blue)', single_round)
				for i in blues:
					if int(i) > blue_min:
						blue_min = int(i)

			
			counter += red_min * green_min * blue_min

		print("The answer for part 02 is: " + str(counter))
			

part_01()
part_02()