# o = 0, x = 1
current_player = 0
player_won = -1
game_over = False
playfield = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
counter_turns = 0
rows = 3
columns = 3


def start_game():
	global playfield
	global game_over
	global current_player
	global counter_turns
	playfield = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
	game_over = False
	if player_won == 0:
		current_player = 1
	else:
		current_player = 0
	print("🏁 Startspieler " + get_symbol(current_player))
	counter_turns = 0
	game_loop()

def get_symbol(number):
	if number == -1:
		return " "
	if number == 0:
		return "o"
	if number == 1:
		return "x"

def print_playfield():
	output = ""
	for row in playfield:
		for entry in row:
			output += "[" + get_symbol(entry) + "]"
		output += "\n"
	print(output)

def game_loop():
	global current_player
	while not game_over:
		get_next_input()
		if current_player == 0:
			current_player = 1
		else:
			current_player = 0
	user_input = input("Nochmal (y/n)? ")
	if user_input == 'y':
		start_game()
	

def get_next_input():
	print_playfield()
	print("Spieler " + get_symbol(current_player) + " ist am Zug.")
	valid_input = False
	x = -1
	y = -1
	while not valid_input:
		user_input = input("Bitte Koordinaten eingeben (yx). 📐")
		if len(user_input) < 2 or len(user_input) > 2:
			print("Du kannst das ja gar nicht. Du sollst doch yx eingeben. Zum Beispiel 12 🚨")
			continue
		x_char = user_input[1]
		y_char = user_input[0]
		if x_char.isdigit() and y_char.isdigit():
			x = int(x_char)
			y = int(y_char)
			if is_in_playfield(x, y) and playfield[y][x] == -1:
				playfield[y][x] = current_player
				valid_input = True
		if valid_input == False:
			print("Du kannst das ja gar nicht. Du sollst doch yx eingeben. Zum Beispiel 12 🚨")
	global game_over
	global player_won
	global counter_turns
	counter_turns += 1
	if evaluate_field(x,y):
		game_over = True
		player_won = current_player
		print("Spieler " + get_symbol(current_player) + " hat gewonnen 🎉")
		print_playfield()
	elif counter_turns == rows * columns:
		player_won = -1
		game_over = True
		print("Dödüm - Spiel vorbei 🤷🏽‍♀️")
		print_playfield()


def evaluate_field(x, y):
	if evaluate_horizontal(x, y):
		return True
	if evaluate_vertical(x, y):
		return True
	if evaluate_diagonal(x, y):
		return True
	return False

def evaluate_horizontal(x, y):
	counter = 1
	counter += evaluate_direction(x, y, 1, 0)
	counter += evaluate_direction(x, y, -1, 0)
	return counter >= 3

def evaluate_vertical(x, y):
	counter = 1
	counter += evaluate_direction(x, y, 0, 1)
	counter += evaluate_direction(x, y, 0, -1)
	return counter >= 3

def evaluate_diagonal(x, y):
	return evaluate_diagonal0(x, y) or evaluate_diagonal1(x, y)

def evaluate_diagonal0(x, y):
	counter = 1
	counter += evaluate_direction(x, y, -1, -1)
	counter += evaluate_direction(x, y, 1, 1)
	return counter >= 3

def evaluate_diagonal1(x, y):
	counter = 1
	counter += evaluate_direction(x, y, -1, 1)
	counter += evaluate_direction(x, y, 1, -1)
	return counter >= 3

def is_in_playfield(x, y):
	return x < columns and y < rows and x >= 0 and y >= 0

def evaluate_direction(x, y, dx, dy):
	target_char = playfield[y][x]
	counter = 0
	x_current = x + dx
	y_current = y + dy
	while is_in_playfield(x_current, y_current) and playfield[y_current][x_current] == target_char:
		counter += 1
		x_current += dx
		y_current += dy
	return counter

start_game()
