def translate_to_numbers(line):
	numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
	           "six": "6", "seven": "7", "eight": "8", "nine": "9"}

	updated_line = ""
	for i in range(len(line)):
		try:
			updated_line += str(int(line[i]))
			continue
		except ValueError:
			pass
		for number, integer in numbers.items():
			if line[i:].startswith(number):
				updated_line += integer

	return updated_line


def get_first_number(line):
	for char in line:
		try:
			return int(char)
		except ValueError:
			continue


with open("day 1.txt") as f:
	data = f.read().splitlines(keepends=False)

key_part_1 = 0
for line in data:
	first_number = str(get_first_number(line))
	last_number = str(get_first_number(line[::-1]))
	key_part_1 += int(first_number + last_number)

print(f"The Answer to Part 1 of Day 1 is: {key_part_1}")

key_part_2 = 0
for line in data:
	new_line = translate_to_numbers(line)
	first_number = str(get_first_number(new_line))
	last_number = str(get_first_number(new_line[::-1]))
	key_part_2 += int(first_number + last_number)

print(f"The Answer to Part 2 of Day 1 is: {key_part_2}")

