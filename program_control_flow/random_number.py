import random

highest = 10
answer = random.randint(1, highest)

print("Please guess number between 1 and 10")
guess = int(input())

while guess is not answer:
  if guess == 0:
    break
  if guess == answer:
    print("good job getting it on the first shit")
    break
  else:
    if guess < answer:
      print("guess higher")
      guess = int(input())
    elif guess > answer:
      print("guess lower")
      guess = int(input())

print("you've guessed the right number, the number is {}".format(answer))