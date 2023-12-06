import re

def part_01():
	puzzle_matrix = openPuzzleMatrix("day-03_input.txt")
	counter = 0

	# print(puzzle_matrix)
	matrix_height = len(puzzle_matrix)
	matrix_width = len(puzzle_matrix[0])-1
	
	# print("Width: " + str(matrix_width))
	# print("Height: " + str(matrix_height))

	for x, line in enumerate(puzzle_matrix):
		for m in re.finditer(r'\d+', line):
			is_part_nr = False

			x_search_min = max(0, x-1)
			x_search_max = min(matrix_height-1, x+1)
			y_search_min = max(0, m.span()[0]-1)
			y_search_max = min(matrix_height-1, m.span()[1]+1)
			# print(m.group())
			# print(x_search_min)
			# print(x_search_max)
			# print(y_search_min)
			# print(y_search_max)
			for x_search in range(x_search_min, x_search_max+1):
				# print(puzzle_matrix[x_search][y_search_min:y_search_max])
				if re.findall(r'(?=\D)(?!\.)', puzzle_matrix[x_search][y_search_min:y_search_max]):
					is_part_nr = True

			if is_part_nr:
				counter += int(m.group())
				# print(str(m.group()) + " is a part nr")
			# else:
				# print(str(m.group()) + " is not a part nr")

	print("The answer of part_01 is: " + str(counter))


def part_02():
	puzzle_matrix = openPuzzleMatrix("day-03_input.txt")
	counter = 0

	matrix_height = len(puzzle_matrix)
	matrix_width = len(puzzle_matrix[0])-1

	for x in range(len(puzzle_matrix)):
		for m in re.finditer(r'\*', puzzle_matrix[x]):
			gear_numbers = []
			x_search_min = max(0, x-1)
			x_search_max = min(matrix_height-1, x+1)

			for x_search in range(x_search_min, x_search_max+1):
				for gear_number_match in re.finditer(r'\d+', puzzle_matrix[x_search]):
					if (gear_number_match.span()[0] < m.span()[0]+2)&(gear_number_match.span()[1] > m.span()[0]-1):
						gear_numbers.append(int(gear_number_match.group()))
			
			print(gear_numbers)

			if len(gear_numbers) is 2:
				counter += gear_numbers[0] * gear_numbers[1]

	print("The answer of part_02 is: " + str(counter))


def openPuzzleMatrix(file_path):
	with open(file_path) as puzzle_input_file:
		puzzle_matrix = []
		for line in puzzle_input_file:
			puzzle_matrix.append(line)

		return puzzle_matrix
		
		
part_01()
part_02()
