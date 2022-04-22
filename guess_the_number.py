import random

def guess(x):
    rand_num = random.randint(1,x)
    guess = 0
    while guess != rand_num:
        guess = int(input(f'Guess a number betweent 1 and {x}: '))
        if guess>rand_num:
            print("Sorry. Your guess is too high.")
        elif guess<rand_num:
            print("Sorry. Your guess is too low.")
    print("Yayy congrats. You guessed it right!!!")
    
guess(10)
