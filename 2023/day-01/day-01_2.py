import re

valid_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def string2number(raw_string):
	if raw_string.isnumeric():
		return int(raw_string)
	else:
		return int(valid_digits.index(raw_string))

def get_calibration_value(calibration_string):
	# Gebruik regular expression om alle getallen in een array te krijgen
	numbers = re.findall(r'(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))', calibration_string)
	print(numbers)
	return 10* string2number(numbers[0]) + string2number(numbers[len(numbers)-1])
	


counter = 0
i = 1

calibration_document = open("AoC-2023-01_input.txt", "r")

#### BEGIN TEST CODE ####

# for x in range(1,50):
# 	cal_line = calibration_document.readline()

# 	print("\nLine " + str(i) + ": " + str(cal_line))
# 	value = get_calibration_value(cal_line)
# 	print("Value: " + str(value))

# 	counter += value
# 	print("Counter: " + str(counter))
	
# 	i+=1

#### END TEST CODE ####

cal_line = calibration_document.readline()

while cal_line:
	print("\nLine " + str(i) + ": " + str(cal_line))
	value = get_calibration_value(cal_line)
	print("Value: " + str(value))

	counter += value
	print("Counter: " + str(counter))
	cal_line = calibration_document.readline()
	i+=1

print( "The calibration value is: " + str(counter) )
