class State:
    # this initializer does not require paremeters
    def __init__(self):
        self.name = input("what is the name of the state? ")
        self.abbr = input("what is the abbreviation? ")
        self.pop = int(input("what is the population? "))
    
    def __str__(self):
        return "TODO"
    
