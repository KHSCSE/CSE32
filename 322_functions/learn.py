
def star_wars_spoiler():
  print("\nIn a galaxy far, far away...")
  print("...Death Star destroyed!")
  print("Luke Skywalker, hero!")
  print("\nAlso, Darth is Luke's father")
  print("...and Luke and Leia are siblings")
  

star_wars_spoiler()

print("\n\n\n")

def my_max(num1, num2):
  if num1 == num2:
    print("these numbers are equal")
  elif num1 > num2:
    print(num1, "is the maximum")
  else:
    print(num2, "is the maximum")

ans1 = int(input("Type a number:"))
ans2 = int(input("Type another number:"))
my_max(ans1, ans2)





# my_max(13, 42)



print("\n\n\n\n\n")





def is_teenager(age):
  if age > 12 and age < 20:
    return True
  else:
    return False


print(is_teenager(17))

ans = is_teenager(20)
print(ans)


print("\n\n")



