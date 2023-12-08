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
		seed_ranges_raw = get_line_integers(puzzle_input.readline())
		seed_ranges = [seed_ranges_raw[i:i+2] for i in range(0, len(seed_ranges_raw), 2)]

		# print("start ranges:", seed_ranges, sep="\t")

		puzzle_input.readline() # Skip the first empty line

		all_maps = get_all_maps(puzzle_input)

		for single_map in all_maps:
			single_map.sort(key=takeSecond)
			# print(single_map)

		temp_ranges = seed_ranges
		for single_map in all_maps:
			# print("before trim:",temp_ranges, sep="\t")
			temp_ranges = trim_ranges(temp_ranges, single_map)
			# print("after trim:", temp_ranges, sep="\t")
			for i in range(len(temp_ranges)):
				temp_ranges[i][0] = find_destination_value(temp_ranges[i][0], single_map)
		# print("final ranges:", temp_ranges, sep="\t")
		print("lowest value is", sorted(temp_ranges)[0][0])

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

def trim_ranges(ranges, single_map): # Returns ranges
	for i, single_range in enumerate(ranges):
		# For every input range, cut off the end if it overlaps multiple ranges
		# in the map

		single_range_start = ranges[i][0]
		single_range_end = ranges[i][0] + ranges[i][1]
		# print("single_range_start", single_range_start, "\tsingle_range_end", single_range_end)
		for map_line in single_map:
			# print("\t", map_line)
			map_range_start = map_line[1]
			map_range_end = map_line[1] + map_line[2]

			if map_range_start in range(single_range_start+1, single_range_end):
				# print("\t\tmap_range_start", map_range_start, "single_range_start", single_range_start, "single_range_end", single_range_end)
				ranges.append([map_range_start, single_range_end - map_range_start]) #store overlapped part in new range in ranges
				# print("\t\tappended at index", i)
				single_range_end = map_range_start
				ranges[i][1] = map_range_start - single_range_start #cut off overlapped part
			elif map_range_end in range(single_range_start+1, single_range_end):
				# print("\t\tmap_range_end", map_range_end, "single_range_start", single_range_start, "single_range_end", single_range_end)
				ranges.append([map_range_end, single_range_end - map_range_end]) #store overlapped part in new range in ranges
				# print("\t\tappended at index", i)
				single_range_end = map_range_end
				ranges[i][1] = map_range_end - single_range_start #cut off overlapped part

	return ranges

# part01()
part02()