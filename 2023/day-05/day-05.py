import re

def part01():
	with open("day-05_input.txt") as puzzle_input:
		seeds = get_line_integers(puzzle_input.readline())
		# print("Seeds: ", seeds)

		puzzle_input.readline() # Skip the first empty line

		all_maps = get_all_maps(puzzle_input)

		for single_map in all_maps:
			single_map.sort(key=takeSecond)
			# print(single_map)

		print("Part01| The lowest location number is:",
			find_lowest_location(seeds, all_maps))


def part02():
	with open("day-05_input.txt") as puzzle_input:
		seed_ranges = get_line_integers(puzzle_input.readline())
		

		# print("Seeds: ", seeds)

		puzzle_input.readline() # Skip the first empty line

		all_maps = get_all_maps(puzzle_input)

		for single_map in all_maps:
			single_map.sort(key=takeSecond)
			# print(single_map)

		for i in range(0, len(seed_ranges), 2):
			print("Analysing seed set", int(i/2))
			temp_lowest_location = find_lowest_location(
				range(seed_ranges[i], seed_ranges[i]+seed_ranges[i+1]), all_maps)
			if 'lowest_location' in locals():
				lowest_location = min(lowest_location, temp_lowest_location)
			else:
				lowest_location = temp_lowest_location

		print("Part02| The lowest location number is:", lowest_location)

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def get_line_integers(line):
	return [int(i) for i in re.findall(r'\d+', line)]

def get_all_maps(puzzle_input):
	all_maps = [[]]
	map_index = 0

	for line in puzzle_input:
		# At the end of a map do this
		if len(line) == 1: 
			map_index += 1 # Increase map index for every empty line
			all_maps.append([])

		if has_numbers(line):
			all_maps[map_index].append(get_line_integers(line))

	return all_maps

def find_destination_value(source_value, single_map):
	destination_range_start = 0
	source_range_start = 0

	for map_line in single_map: # map line: [destination_range_start, source_range_start, range_length]
		if source_value in range(map_line[1], map_line[1] + map_line[2]):
			destination_range_start = map_line[0]
			source_range_start = map_line[1]
	
	return destination_range_start + source_value - source_range_start 

def find_seed_location(seed, all_maps):
	source_value = seed
	# print(source_value)
	for single_map in all_maps:
		destination_value = find_destination_value(source_value, single_map)
		source_value = destination_value
		# print(destination_value)
	return destination_value

def find_lowest_location(seeds, all_maps):
	map_seed_to_location = []

	for seed in seeds:
		map_seed_to_location.append([seed, find_seed_location(seed, all_maps)])

	map_seed_to_location.sort(key=takeSecond)
	return map_seed_to_location[0][1]

# take second element for sort
def takeSecond(elem):
    return elem[1]

part01()
# part02()