import random

# this file contains functions (it is *not* a class)
# this file can be called a 'utility' file 

# this function shows how we can receive a Player object as a parameter
# we can also access items in the players inventory
def cave(character):
    print("\nyou have entered a cave...")
    obstacle = random.choice(['darkness', 'a monster', 'a steep wall'])
    print("you have encountered... " + obstacle)
    print("and you have " + str(character.inventory))
    if obstacle =='a steep wall' and 'rope' in character.inventory:
        print("good fortune, you climbed the wall!")
        return 10
    elif obstacle == 'darkness' and ('candle' in character.inventory or 'dog' in character.inventory):
        print("good fortune, you found your way out!")
        return 10
    elif obstacle == 'a monster' and 'dog' in character.inventory:
        print("good fortune, you fought the monster!")
        return 10
    else:
        print("something went wrong!")
        return -10


def player_wins_rps(move1, move2):
    if move1 == 'r' and move2 == 's':
        return True
    elif move1 == 'p' and move2 == 'r':
        return True
    elif move1 == 's' and move2 == 'p':
        return True
    else:
        return False

def rps():
    print("\nwe will engage in a game of rock, paper, scissors!")
    p_choice = ''
    while p_choice not in ['r', 'p', 's']:
        p_choice = input("Choose (r)ock, (p)aper, (s)cissors: ")
    comp_choice = random.choice(['r', 'p', 's'])
    print("computer chose " + str(comp_choice))
    if player_wins_rps(p_choice, comp_choice):
        print("congrats, you get more health!")
        return 5
    else:
        print('you lost this round. too bad :(')
        return -5
    


