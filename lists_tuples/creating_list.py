even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]
odd[3:] = [9] # slicing
del odd[3:] # deleting

numbers = even + odd

sorted_numbers = sorted(numbers)
print(sorted_numbers)
digits = sorted("345981276")
print(digits)