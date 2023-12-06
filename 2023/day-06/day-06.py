import re

# input_location = "day-06_example.txt"
input_location = "day-06_input.txt"

def part01(input_location):
	[times, distances] = get_data(input_location)

	answer = 1
	for i in range(len(times)):
		answer *= calculate_possible_wins(times[i], distances[i])

	print("Part01| The amount of ways to win the race is:", answer)


def part02(input_location):
	with open(input_location) as puzzle_input:
		line = puzzle_input.readline()
		
		time_strings = ""
		for c in line:
			if c.isdigit():
				time_strings += c
		time = int(time_strings)

		distance_strings = ""
		line = puzzle_input.readline()
		for c in line:
			if c.isdigit():
				distance_strings += c
		distance = int(distance_strings)

		answer = calculate_possible_wins(time, distance)

		print("Part02| The amount of ways to win the race is:", answer)



def get_data(input_location):
	with open(input_location) as puzzle_input:
		time_strings = re.findall(r'\d+', puzzle_input.readline())
		times = [int(x) for x in time_strings]

		distance_strings = re.findall(r'\d+', puzzle_input.readline())
		distances = [int(x) for x in distance_strings]
		
	return [times, distances]

def calculate_distance(t_press, t_total):
	return t_press * (t_total - t_press) # t_press is also speed

def calculate_possible_wins(t_total, distance_record):
	counter = 0
	for t_press in range(t_total):
		if distance_record < calculate_distance(t_press, t_total):
			counter += 1
	return counter

part01(input_location)
part02(input_location)