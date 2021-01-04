name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age > 18:
  print("You are old enough to vote")
elif age == 18:
  print("You can drink in Canada, but not the US. Just gotta wait {0} years".format(21-age))
else: 
  print("You're a bit young, please come back in {0} years".format(18 - age))
