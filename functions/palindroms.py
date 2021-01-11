def is_palindrome(string):
  string = string.casefold()
  return string[::-1] == string

word = input("Enter a word: ")
if is_palindrome(word):
  print("{} is a palindrome".format(word))
else:
  print("{} is not a palindrome".format(word))


def is_palindrome_sentence(sentence):
  edited_sentence = ""
  for letter in sentence:
    if letter.isalpha():
      edited_sentence += letter
  return is_palindrome(edited_sentence)

phrase = input("please write a sentence: ")

if is_palindrome_sentence(phrase):
  print("{} is a palindrome".format(phrase))
else:
  print("{} is not a palindrome".format(phrase))

  
