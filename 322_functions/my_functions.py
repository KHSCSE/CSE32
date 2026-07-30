import random

def check_guess(g, s):
    '''this function receives two parameters: guess, secret'''
    if g == s:
        print("correct")
    elif g > s:
        print("too high")
    else:
        print("too low")

# this function does not receive parameters
# and does not return a value
def magic_8():
    question = input("\nAsk the magic 8 ball a question: ")
    messages = ['absolutely', 'most likely']
    # TODO add more messages to the list
    print(random.choice(messages))


# this function recieves one parameter
# and determines if that is of voting age
def can_vote(age):
    if age >= 18:
        print("This person is of legal age to vote.")
    else:
        print("This person is not of legal age to vote.")
    
    

# ----- TODO write your functions for 'apply' here -----


