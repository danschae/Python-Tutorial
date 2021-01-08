menu = [
  ["eggs", "spam", "cheese"],
  ["beef", "spam", "pasta"],
  ["chicken", "cheese", "rice"]
]

for meal in menu:
  for index in range(len(meal) -1, -1, -1):
    if meal[index] == "spam":
      del meal[index]
  print(", ".join(meal))