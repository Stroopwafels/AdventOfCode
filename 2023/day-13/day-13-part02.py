# input_file = "day-13-example.txt"
input_file = "day-13-input.txt"

def part02(input_file):
	all_patterns = get_input(input_file)
	score = 0
	for pattern in all_patterns:
		score += get_mirror_score(pattern)
		print(score)
	
	print("part02| The answer is:", score)


def get_input(input_file):
	with open(input_file) as puzzle_input:
		all_patterns = puzzle_input.read().split("\n\n")
		for i in range(len(all_patterns)):
			all_patterns[i] = all_patterns[i].split("\n")
	return all_patterns


def get_mirror_score(pattern):
	mirror_score = 0
	mirror_score = 100* find_mirror(pattern)
	
	if not mirror_score:
		pattern = list(map(lambda *x: list(x), *pattern)) # transpose pattern
		mirror_score = find_mirror(pattern)

	return mirror_score


def find_mirror(pattern):
	for i in range(len(pattern)-1):
		defects = find_row_defects(pattern[i],pattern[i+1])
		if defects <= 1:
			# Potential mirror found
			upper_pattern = pattern[:i]
			mirror_pattern = pattern[-1:i+1:-1]
			# print(upper_pattern, '\n', mirror_pattern)

			# Check if patterns match
			j_range = min(len(upper_pattern), len(mirror_pattern))

			for j in range(-1, -j_range-1, -1):
				defects += find_row_defects(upper_pattern[j], mirror_pattern[j])

			if defects == 1:
				return i+1
			
	# If no mirror has been found in any row
	return 0

def find_row_defects(row1, row2):
	if row1 != row2:
		defects = 0
		for i in range(len(row1)):
			if row1[i] != row2[i]:
				defects += 1
		return defects
	else:
		return 0

part02(input_file)