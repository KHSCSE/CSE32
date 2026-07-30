import random, my_functions

options = '''
1 for pizza_calculator
2 for power_ranger
'''
user_input = int(input(options))

if user_input == 1:
    price_of_pizza = float(input("\nHow much does the pizza cost?"))
    size_of_pizza = int(input("What size?"))
    # TODO call the value_calculator function
    
elif user_input == 2:
    print("\nChoose one of these:")
    print("eagle, horse, snake")
    print("and I'll reveal which Power Ranger you are.")
    response = input().lower()
    # TODO call the power_ranger function
    


