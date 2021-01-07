even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]

even.extend(odd)
print(even)
even.sort()
even.sort(reverse=True)
print(even)

pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram, key=str.casefold)
print(letters)