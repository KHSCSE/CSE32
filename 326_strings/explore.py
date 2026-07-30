name = input("Type your name: ")
print("...some string functionality...")
print("LOUD:", name.upper())
print("soft:", name.lower())
print("proper:", name.title())
print("count something:", name.count("a"))

print("how many letters?", len(name))

print("first letter:", name[0])
print("last letter:", name[-1])
print("first letter + last letter:", name[0]+name[-1])

print("repeat *3:", name*3)

ans = name + "potato"
print("concatenation:", ans)



# --------- other string tools ----------
print("\n...The keyword 'in'...")
if 'a' in name:
    print("your name contains an 'a'")


if 'aa' in name or 'ee' in name or 'ii' in name or 'oo' in name or 'uu' in name:
    print("your name contains double vowels")
else:
    print("your name does not contain double vowels")

print("\n...A special loop!...")
for letter in name:
    print(letter)
  
