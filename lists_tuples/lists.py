computer_parts = [
  "monitor",
  "mouse",
  "mousepad",
  "keyboard"
]

computer_parts += ["GPU"] # interesting way of pushing to an array
computer_parts.append("CPU")

for part in computer_parts:
  print(part)


a = b = c = d = e = f = computer_parts
print(a)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
print(min(even))
print(max(odd))
print(len(odd))
print(computer_parts[0].count("o"))