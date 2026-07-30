options = '''
Here are your options:
(two) for first_two
(hello) for hello_name
(abba) for make_abba
(end) for extra_end
(tags) for make_tags
(quit) to quit
'''

choice = ''
while choice != 'quit':
    print(options)
    choice = input("\nWhich? ")
    if choice == 'two':
        # EXAMPLE first_two
        # given two strings
        # display a concatenation of their first two letters
        x = input("enter first string: ")
        y = input("enter second string: ")
        ans = x[0] + x[1] + y[0] + y[1]
        print(ans)
    elif choice == 'hello': 
        # TODO hello_name
        pass
    elif choice == 'abba':
        # TODO make_abba
        pass
    elif choice == 'end':
        # TODO extra_end
        pass
    elif choice == 'tags':
        # TODO make_tags
        pass

