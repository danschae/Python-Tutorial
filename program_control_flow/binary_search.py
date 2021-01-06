low = 1
high = 1000
guess_count = 1

print("please think of a number between {} and {}".format(low, high))
input("Press enter to start")

while low != high:
  guess = low + (high - low) // 2
  high_low = input("My guess is {}. Should I guess higher or lower? "
                   "Enter h or l or c: "
                   .format(guess)).casefold()
  if high_low == "h":
    # guess higher
    low = guess + 1
  elif high_low == "l":
    # guess lower
    high = guess - 1
  elif high_low == "c":
    print("I got it in {} guesses".format(guess_count))
    break
  else:
    print("please enter h, l or c")
  
  guess_count += 1
else:
  print("You thought of the number {}".format(low))
  print("I got it in {} guesses".format(guess_count))
