#!bin/python3
from sdv import SDV

print("\n--- an SDV simulation ---")

options = '''
(new) to create new SDV
(hi) to say hi
(fwd) to move forward
(right) to turn right
(left) to turn left
(view) to view info
(quit)
'''

choice = ''
the_bot = SDV('temp') # necessary for the loop below
while choice != 'quit':
    print(options)
    choice = input("What's your choice? ")
    if choice == 'new':
        # TODO ask for the name, create the object
        pass
    elif choice == 'hi':
        # TODO call the say_hi function
        pass
    elif choice == 'fwd':
        # TODO call the move_forward function
        pass
    # TODO complete the other options



print("\n\nhere's the final info: ")
print(the_bot)