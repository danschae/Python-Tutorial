data = [4, 5, 104, 7, 105, 110, 120, 130, 
        150, 160, 170, 183, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

stop = 0
for index, value in enumerate(data):
  if value >= min_valid:
    # del data[index] # won't delete all the items because the index will change
    stop = index
    break

del data[:stop]
print(data)