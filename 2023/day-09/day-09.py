# input_file = "day-09-example.txt"
input_file = "day-09-input.txt"

def part01(input_file):
	answer_pt01 = 0
	answer_pt02 = 0
	with open(input_file) as puzzle_input:
		for line in puzzle_input:
			numbers = [[int(i) for i in line.split()]]
			
			for i in range(1, len(numbers[0])):
				numbers.append(find_differences(numbers[i-1]))
				if not any(numbers[i]):
					break

			numbers = extrapolate_numbers(numbers)
			answer_pt01 += numbers[0][-1]
			numbers = extrapolate_numbers_back(numbers)
			answer_pt02 += numbers[0][0]
			# for number_line in numbers:
			# 	print(number_line) 
	print("part01| The answer to part01 is:", answer_pt01)
	print("part02| The answer to part02 is:", answer_pt02)


# def part02(input_file):
# 	with open(input_file) as puzzle_input:
# 		for line in puzzle_input:
# 			pass

def find_differences(num_list):
	return [num_list[i] - num_list[i-1] 
		for i in range(1, len(num_list))]

def extrapolate_numbers(numbers):
	for i in reversed(range(len(numbers)-1)):
		numbers[i].append(numbers[i][-1] + numbers[i+1][-1])
	return numbers

def extrapolate_numbers_back(numbers):
	for i in reversed(range(len(numbers)-1)):
		numbers[i].insert(0, numbers[i][0] - numbers[i+1][0])
	return numbers

part01(input_file)
# part02(input_file)