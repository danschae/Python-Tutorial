x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("unpacking a tuple")

data = 1, 2, 76 # data represents tuple
x, y, z = data
print(x)
print(y)
print(z)

print("unpacking a list")

data_list = [12, 13, 14]
# data_list.append(15) problem with unpacking lists is that if the list changes, it'll crash the app
p, q, r = data_list
print(p)
print(q)
print(r)

