# input_file = "day-11-example.txt"
input_file = "day-11-input.txt"

space_multiplier = 1000000

def part01(input_file):
	with open(input_file) as puzzle_input:
		space_matrix = puzzle_input.read().split('\n')

	space_matrix = expand_space(space_matrix)
	galaxy_coordinates = get_galaxy_coordinates(space_matrix)
	answer = calc_distance_sum(galaxy_coordinates)

	print("part01: The total distance is", answer)

def part02(space_multiplier, input_file):
	with open(input_file) as puzzle_input:
		space_matrix = puzzle_input.read().split('\n')
	galaxy_coordinates = fast_galaxy_coordinates(space_multiplier, space_matrix)

	answer = calc_distance_sum(galaxy_coordinates)

	print("part02: The total distance is", answer)


def expand_space(space_matrix):
	i = 0
	j = 0

	# Expand vertically
	while i < len(space_matrix):
		if '#' not in space_matrix[i]:
			space_matrix.insert(i, space_matrix[i])
			i += 1
		i += 1

	# Expand horizontally
	while j < len(space_matrix[0]):
		if '#' not in [space_matrix[x][j] for x in range(len(space_matrix))]:
			for i in range(len(space_matrix)):
				space_matrix[i] = space_matrix[i][:j] + '.' + space_matrix[i][j:]
			j += 1
		j += 1

	return space_matrix

def get_galaxy_coordinates(space_matrix):
	galaxy_coordinates = []
	for i in range(len(space_matrix)):
		for j in range(len(space_matrix[i])):
			if space_matrix[i][j] == '#':
				galaxy_coordinates.append([i,j])
	return galaxy_coordinates

def fast_galaxy_coordinates(multiplier, space_matrix):
	galaxy_coordinates = []
	expandable_rows = get_expandable_rows(space_matrix)
	expandable_cols = get_expandable_cols(space_matrix)
	expansion_vertical = 0


	for i in range(len(space_matrix)):
		if i in expandable_rows:
			expansion_vertical += multiplier - 1

		expansion_horizontal = 0
		for j in range(len(space_matrix[i])):
			if j in expandable_cols:
				expansion_horizontal += multiplier - 1

			if space_matrix[i][j] == '#':
				galaxy_coordinates.append([
					i + expansion_vertical,
					j + expansion_horizontal])
	return galaxy_coordinates

def get_expandable_rows(space_matrix):
	expandable_rows = []
	for i in range(len(space_matrix)):
		if '#' not in space_matrix[i]:
			expandable_rows.append(i)
	return expandable_rows

def get_expandable_cols(space_matrix):
	expandable_cols = []
	for j in range(len(space_matrix[0])):
		if '#' not in [space_matrix[x][j] for x in range(len(space_matrix))]:
			expandable_cols.append(j)
	return expandable_cols

def calc_galaxy_distance (coordinate_1, coordinate_2):
	return abs(coordinate_1[0] - coordinate_2[0]) + abs(coordinate_1[1] - coordinate_2[1])

def calc_distance_sum(galaxy_coordinates):
	distance_sum = 0
	for n in range(1, len(galaxy_coordinates)):
		for m in range(n):
			distance_sum += calc_galaxy_distance(galaxy_coordinates[n], galaxy_coordinates[m])
	return distance_sum

part01(input_file)
part02(space_multiplier, input_file)