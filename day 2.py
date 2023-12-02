import re

with open("day 2.txt") as f:
	data = f.read().splitlines()

key_part_1 = 0
key_part_2 = 0
for line in data:
	game_id = int(line.split(":")[0].replace("Game ", ""))
	possible = True
	min_red, min_green, min_blue = 0, 0, 0
	for set in line.split(";"):
		blue = sum([int(i.split(" ")[0]) for i in re.findall(r"[0-9]{0,9} blue", set)])
		green = sum([int(i.split(" ")[0]) for i in re.findall(r"[0-9]{0,9} green", set)])
		red = sum([int(i.split(" ")[0]) for i in re.findall(r"[0-9]{0,9} red", set)])
		if not (red <= 12 and green <= 13 and blue <= 14):
			possible = False

		if min_red < red:
			min_red = red

		if min_green < green:
			min_green = green

		if min_blue < blue:
			min_blue = blue

	if possible:
		key_part_1 += game_id
	key_part_2 += min_red * min_green * min_blue

print(key_part_1, key_part_2)
