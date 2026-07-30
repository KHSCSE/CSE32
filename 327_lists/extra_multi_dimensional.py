# A two-dimensional list
# note that this is a "list of lists"
all_schedules = [ ["PE", "CSE", "Physics"], 
                  ["History", "Journalism", "Biology"],
                  ["Painting", "Culinary", "Engineering"]
                ]
                  
                  
# Another way to create the same 2-D list
schedule1 = ["PE", "CSE", "Physics"]
schedule2 = ["History", "Journalism", "Biology"]
schedule3 = ["Painting", "Culinary", "Engineering"]
all_schedules = [schedule1, schedule2, schedule3]


print("\nUsing nested loops to visit every class:")
# iterating through requires two loops!
for one_schedule in all_schedules:
  for one_class in one_schedule:
    print(one_class)