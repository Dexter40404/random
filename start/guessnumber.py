import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"write a number between 0 a {x}:"))
        if guess < random_number:
            print("you drink 2x")
        elif guess > random_number:
            print("you drink 1x")

    print("you dont drink")
guess(1000)



