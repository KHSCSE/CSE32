import random

# this file defines a Class

class Player:
    # variables must be defined here
    def __init__(self):
        print("...creating a new Player...")
        self.name = ''
        self.inventory = []
        self.alive = False
        self.health = 0
        # call the method to set up a new player
        self.new_player()

    # when a new player is created
    # this method is called from __init__
    def new_player(self):
        self.alive = True
        correct = 'n'
    
        # get their name
        while correct == 'n':
            self.name = input("enter your name: ")
            correct = input("is this correct? (y) or (n): ")
        print("welcome " + self.name)
        
        # players begin by choosing one item for their inventory
        items = ["candle", "rope", "dog"]
        choice = ''
        while choice not in items:
            choice = input("choose one item from " + str(items) + ": ")
        self.inventory.append(choice)
        self.health = random.randint(50,100)
        print("you have been assigned " + str(self.health) + " health points")
        

  
  