import random

def game(x):
    print(f"you have to guess a number between 1 and {x} that computer has choosen.".upper())
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x}: '))
        if guess < random_number:
            print("your guess is low, try again...")
        elif guess > random_number:
            print("your guess is high, try again...")

    print(f'hurray, you got it right!!! {random_number} is the correct guess.'.upper())


def compguess(x):
    print(f"computer will try to guess a number between 1 and {x} that you have choosen. ".upper())
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'is {guess} high(H), low(L) or correct(C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'yay!! computer has guessed it, the number in your mind was {guess} '.upper())
if __name__ == "__main__":
    a =0
    while a != 3:
        a = int(input("\nhey there, we have a guessing game for you.\
 press 1 for player and 2 for computer\nand 3 for exit:".upper()))
        if a == 1:
            game(15)
        elif a == 2:
            compguess(15)
        elif a > 3:
            print("invalid")
