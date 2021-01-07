current_choice = "-"
computer_parts = []
available_parts = ["computer", 
                  "monitor", 
                  "keyboard",
                  "mouse",
                  "mousepad", 
                  "HDMI cable"]

valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
print(valid_choices)
while current_choice != '0':
  if current_choice in valid_choices: 
    index = int(current_choice) - 1
    chose_part = available_parts[index]
    if chose_part in computer_parts:
      print("Removing {}".format(chose_part))
      computer_parts.remove(chose_part)
    else:
      print('Adding {}'.format(chose_part))
      computer_parts.append(chose_part)
  else:
    print("Please add options on the list below")
    for number, part in enumerate(available_parts): # enumerate is another option instead of looking for an index
      print("{}: {}".format(number + 1, part))
  current_choice = input()
  print(computer_parts)