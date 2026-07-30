from player import * # this is an object class
import adventures # this is a file with functions


again = 'y'
while again == 'y':
    p = Player()
    
    print("\nthere is a fork in the road")
    choice = input("do you choose (l)eft or (r)ight? ")
    if choice == 'l':
        p.health += adventures.cave(p)
    else:
        p.health += adventures.rps()
    
    # TODO create more choices and more adventures
    
    again = input("\n\nThat's the end! Want to play again (y) or (n)? ")
    

# the end.


