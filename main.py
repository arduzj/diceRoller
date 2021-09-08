import random

while True:     
	print('''1. Roll the dice\n2. Exit''')
	user = int(input("What you want to do?\n"))
	if user == 1:
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
		print(f'\nDice #1 = {d1}  /  Dice #2 = {d2}\n')
		if(d1 + d2 == 7):
			print("CONGRATS!!! You have a 7")
	elif user == 2:
		break
	else:
		print("Please read first")
