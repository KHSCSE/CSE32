# this is the function definition
def is_teenager(age):
    if age > 12 and age < 20:
        return True
    else:
        return False

def area_calculator(diameter):
    radius = diameter / 2
    ans = 3.14 * radius**2
    return ans




# the runnable code begins here
print("\n...learning from the is_teenager() function...")

ans = is_teenager(15)
print("This is what the function returned:", ans)


print(is_teenager(42))





print("\n\n...learning from the area_calculator() function...")
size = float(input("What is the size of the circle (all the way across)?"))
ans = area_calculator(size)
print("The area of this circle is:", ans, "units**2")