

import random as r
user_name = input("what is your name?: ")
print('Hello {}'.format(user_name))

r = r.randint(0,11)

win_num = int(input("Guess the number between 1 to 10: "))

if r == win_num:
	print('Congratulation you win {}'.format(user_name))
else:
	print("Game over")
		
