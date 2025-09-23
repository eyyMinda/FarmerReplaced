clear()

def calculate_pair_steps(world_size):
	return ((world_size - 6) // 2 + 2)

def try_move(direction):
	return move(direction)

def move_home():
	while get_pos_x() != 0:
		try_move(West)
	while get_pos_y() != 0:
		try_move(South)

def return_and_reset():
	change_hat(Hats.Straw_Hat)
	move_home()
	change_hat(Hats.Dinosaur_Hat)
	perform_dino_pattern()

def move_north_or_reset():
	if not try_move(North):
		return_and_reset()

def move_east_or_reset():
	if not try_move(East):
		return_and_reset()

def move_south_or_reset():
	if not try_move(South):
		return_and_reset()

def move_west_or_reset():
	if not try_move(West):
		return_and_reset()

def repeat_move(direction, steps):
	for _ in range(steps):
		if not try_move(direction):
			return_and_reset()
			return False
	return True

def perform_dino_pattern():
	world_size = get_world_size()
	max_index = world_size - 1

	while True:
		if not repeat_move(North, max_index):
			return
		if not repeat_move(East, max_index):
			return
		if not repeat_move(South, 1):
			return

		directions = []
		for _ in range(calculate_pair_steps(world_size)):
			directions.append(West)
			directions.append(East)

		for i in range(0, len(directions), 2):
			dir1 = directions[i]
			if i + 1 < len(directions):
				dir2 = directions[i + 1]
			else:
				dir2 = dir1

			if not repeat_move(dir1, max_index - 1):
				return
			if not repeat_move(South, 1):
				return
			if not repeat_move(dir2, max_index - 1):
				return
			if not repeat_move(South, 1):
				return

		if not repeat_move(West, max_index):
			return

world_size = get_world_size()
if world_size % 2 == 1:
	set_world_size(world_size - 1)
	world_size -= 1

change_hat(Hats.Straw_Hat)
move_home()
change_hat(Hats.Dinosaur_Hat)

while True:
	perform_dino_pattern()
