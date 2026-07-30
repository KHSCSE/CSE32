# this is the function definition
def check_guess(g, s):
    if g == s:
        print("correct")
    elif g > s:
        print("too high")
    else:
        print("too low")


# the runnable code begins here
secret = 42

guess = int(input("Guess the number: "))

check_guess(guess, secret)

# TODO
# get input for another guess, call the function


