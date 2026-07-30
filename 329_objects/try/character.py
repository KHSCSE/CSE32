import random
from math import *

class Character:
    def __init__(self):
        self.name = ""
        self.category = ""
        self.health = 0
    
    def __str__(self):
        return self.name + " is a " + self.category + " with " + str(self.health) + " health"
    
    
