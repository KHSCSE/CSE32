import random

print("\nLearning about calling functions from the random class")
ans = random.randint(1,10)
print("Here's a random number:", ans)

ans = random.uniform(10.1, 15.3)
print("Here's a random decimal number:", ans)


print("\nWe'll learn about lists later, but here's a preview.")
ans = random.choice(['banana', 'potato', 'crocodile'])
print("Selecting random item from list:", ans)

