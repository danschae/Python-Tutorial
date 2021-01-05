# phrase = "Howdy doody"

# counter = 0

# for character in phrase:
#   counter +=1

# print(counter)

# for i in range(0,21, 2):
#   print("i is now {}".format(i))

# for i in range(21,0, -2):
#   print("i is now {}".format(i))

# for i in range(0,13):
#   for j in range(0,13):
#     print("{} times {} is {}".format(j, i, i * j))
#   print("--------------")

shopping_list = ["milk", "eggs", "cheese", "pasta"]

for item in shopping_list:
  if item == "eggs":
    continue # continue and break are opposites
  print(item)