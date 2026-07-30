s = "hello world!"
l = ['banana', 'potato', 'giraffe']

print("\nstrings and lists have a lot in common, and some differences.")

print("\nboth are indexed:")
print(s[0]+s[1])
print(l[0]+l[1])

print("\nboth have a length:")
print(len(s))
print(len(l))



print("\nboth are iterable (can be looped):")
for item in s:
    print(item)
for item in l:
    print(item)
  
print("\nboth use dot notation to access their functions:")
print(s.upper())
l.append('bologna')
print(l)


# DIFFERENCE
# strings are *immutable*
# lists are *mutable*
string_ans = 'banana'
string_ans.upper() # does *not* change the variable
string_ans = string_ans.upper() # must reassign to change

list_ans = ['banana', 'potato']
list_ans.append('bologna') # *does* change the variable
