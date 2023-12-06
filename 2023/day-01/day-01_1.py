import re

def get_calibration_value(calibration_string):
	numbers = []

	for c in cal_line:
		if c.isdigit():
			numbers.append(int(c))

	return 10* numbers[0] + numbers[len(numbers)-1]
	


counter = 0

calibration_document = open("AoC-2023-01_input.txt", "r")

cal_line = calibration_document.readline()

while cal_line:
	counter += get_calibration_value(cal_line)
	cal_line = calibration_document.readline()

print( "The calibration value is: " + str(counter) )