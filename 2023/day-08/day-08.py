import re
from math import gcd

# file_location = "day-08-example3.txt"
file_location = "day-08-input.txt"


def part01():
	directions, nodes = get_input(file_location)

	node = 'AAA'
	dir_index = 0
	steps = 0

	while node != 'ZZZ':
		node = find_next_node(dir_index, directions, node, nodes)
		dir_index += 1
		steps += 1

	print("part01| It takes", steps, "steps to reach ZZZ")



def part02():
	directions, nodes = get_input(file_location)

	ghost_node = find_ghost_start(nodes)

	ghost_node_lengths = []
	
	for node in ghost_node:
		dir_index = 0

		while node[2] != 'Z':
			node = find_next_node(dir_index, directions, node, nodes)
			dir_index += 1

		ghost_node_lengths.append(dir_index)

	# for i, node, in enumerate(ghost_node):
	# 	print("node",node,"has a loop length of", ghost_node_lengths[i])

	steps = 1
	for i in ghost_node_lengths:
		steps = steps*i//gcd(steps, i)

	print("part02| It takes", steps, "steps to reach **Z on all ghost nodes")


def find_next_node(dir_index, directions, node, nodes):
	match directions[dir_index%len(directions)]:
		case "L":
			i = 1
		case "R":
			i = 2
		case _:
			print("Invalid direction:", direction)

	return [node_line[i] for node_line in nodes if node == node_line[0]][0]


def get_input(file_location):
	with open(file_location) as puzzle_input:
		directions, nodes_str = puzzle_input.read().split("\n\n")

	nodes = [re.findall(r'[A-Z]{3}', line)
		for line in nodes_str.split('\n')]

	return directions, nodes


def find_ghost_start(nodes):
	return [node_line[0] for node_line in nodes
		if node_line[0][2] == 'A']


part01()
part02()

