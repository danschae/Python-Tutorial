shopping_list = ["milk", "eggs", "cheese", "pasta"]

item_to_find = "eggs"
found_at = None # values can be initiated as none

for index in range(len(shopping_list)):
  if shopping_list[index] == item_to_find:
    found_at = index
    break

print(found_at)