import random

secret = random.randint(1,100)
guess = 0

while guess != secret:
    guess = int(input("\nwhat is your guess? "))
    if guess == secret:
        print("Correct!")
    elif guess > secret:
        print("too high")
    else:
        print("too low")
    
