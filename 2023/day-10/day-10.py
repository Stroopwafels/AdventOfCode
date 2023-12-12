# input_file = "day-10-example5.txt"
input_file = "day-10-input.txt"

def part01(input_file):
	puzzle_input = get_puzzle_input(input_file)

	dir0, pos0 = find_start(puzzle_input)

	distance = 0
	while True:
		pos0 = calc_new_location(dir0, pos0)
		distance += 1

		pipe = get_pipe(pos0, puzzle_input)
		if pipe == 'S':
			break

		dir0 = calc_new_direction(dir0, pipe)

	print("part01| The farthest point is", int(distance/2), "away")

def part02(input_file):
	puzzle_input = get_puzzle_input(input_file)

	dir0, pos0 = find_start(puzzle_input)

	tracemap = ['.' * len(line) for line in puzzle_input]

	while True:
		pos0 = calc_new_location(dir0, pos0)

		pipe = get_pipe(pos0, puzzle_input)
		x0,y0 = pos0
		tracemap[x0] = tracemap[x0][:y0] + pipe + tracemap[x0][y0+1:]

		if pipe == 'S':
			break

		dir0 = calc_new_direction(dir0, pipe)
	print("\npuzzle_input:")
	for line in puzzle_input:
		print(line)

	print("\ntracemap:")

	for line in tracemap:
		print(line)

	count = 0
	for line in tracemap:
		crossed_borders = 0
		last_corner = "."

		for c in line:
			if c in "LF":
				last_corner = c
			if c == "|":
				crossed_borders += 1
			if c == "7" and last_corner == "L":
				crossed_borders += 1
			if c == "J" and last_corner == "F":
				crossed_borders += 1
			if crossed_borders % 2 and c == '.':
				count += 1
	
	print("part02| the inside space is", count)

def get_puzzle_input(input_file):
	with open(input_file) as opened_file:
		return opened_file.read().split('\n')


def find_start(puzzle_input):
	for x0, line in enumerate(puzzle_input):
		y0 = line.find('S')
		if y0 >= 0:
			break
	pos0 = [x0, y0]

	if puzzle_input[x0-1][y0] in "|7F":
		dir0 = [-1,0]
	elif puzzle_input[x0+1][y0] in "|LJ":
		dir0 = [1,0]
	elif puzzle_input[x0][y0-1] in "-LF":
		dir0 = [0,-1]
	elif puzzle_input[x0][y0+1] in "-7J":
		dir0 = [0,1]
	else:
		print("whoops")

	return dir0, pos0

def calc_new_location(dir0, pos0):
	return [dir0[0] + pos0[0], dir0[1] + pos0[1]]


def get_pipe(pos, puzzle_input):
	x,y = pos
	return puzzle_input[x][y]


def calc_new_direction(dir0, pipe):
	x0, y0 = dir0

	if pipe in '|-':
		x1 = x0
		y1 = y0
	elif pipe in 'L7':
		x1 = y0
		y1 = x0
	elif pipe in 'JF':
		x1 = -y0
		y1 = - x0
	else:
		print("yikes")

	return [x1, y1]


part01(input_file)
part02(input_file)