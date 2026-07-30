import random

class SDV:
    wheel_size = 6   # wheel diameter in centimeters
    has_vision = False
    
    def __init__(self, name_param):
        print("...constructing new SDV object...")
        self.id_num = random.randint(1000, 9999)
        self.name = name_param
        self.total_dist = 0
        self.heading = 'NORTH'
    
    def say_hi(self):
        print (self.name + " says hello")
    
    def move_forward(self, speed=30, dist=360):
        self.total_dist += dist
        print(self.name + " is moving forward")
    
    def turn_right(self, speed=30, dist=210):
        print(self.name + " is turning right")
        if self.heading == 'NORTH':
            self.heading = 'EAST'
        elif self.heading == 'EAST':
            self.heading = 'SOUTH'
        elif self.heading == 'SOUTH':
            self.heading = 'WEST'
        else:
            self.heading = 'NORTH'
        print(" and is now facing " + self.heading)
    
    def turn_left(self, speed=30, dist=210):
        print("TODO")
    
    def __str__(self):
        temp = self.name + " has id number " + str(self.id_num)
        temp += "\ndistance traveled: " + str(self.total_dist)
        temp += "\nfacing direction: " + self.heading
        return temp
  
