import random, math


print("\nLearning about functions and the math class\n")

# the math class has many 'built in' functions
# all of them 'return' a value

# many require just one parameter
print("using square root:", math.sqrt(20)) # square root
print("using fabs:", math.fabs(-3)) # absolute value
print("using abs:", abs(-20)) # not part of the math class
print("using floor:", math.floor(3.7)) # round down always
print("using ceil:", math.ceil(3.7)) # round up always
print("using round:", round(3.5)) # round normally, not part of the math class

# some require more than one parameter
print("using pow:", math.pow(2, 3)) # power

# note that we can call the function in a variety of other ways
ans = math.sqrt(20) # in an assignment
ans2 = round(math.sqrt(28+30)) # in a calculation

print("printing ans:", ans)
print("printing ans2", ans2)
