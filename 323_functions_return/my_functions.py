import math


# this function receives two parameters
# (the price of a pizza and the size of the pizza)
# and returns the price per square inch
def value_calculator(price, size):
    radius = size / 2  # divide by 2 to find the radius
    area = 3.14 * radius**2 # the area of a circle
    val = price / area
    return val



# this function receives one parameter
# and returns a value
def power_ranger(param):
    if param == 'eagle':
        ans = "You are the pink Power Ranger."
        ans += " You wield the Power Bow."
    elif param == 'horse':
        ans = "You are the blue Power Ranger."
        ans += " You wield the Power Lance."
    elif param == 'snake':
        ans = "You are the red Power Ranger."
        ans += " You wield the Power Sword."
    else:
        ans = "Not a valid selection"
    return ans
  


# TODO define your functions for 'apply' here