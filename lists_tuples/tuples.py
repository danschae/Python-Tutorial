# t = ("a", "b", "c") # tuples are immutable
# print(t)

 
welcome = "Welcome to my Nightmare", "Alice Copper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ridge the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])
metallica2 = list(metallica) # can change tuple to list
print(metallica2)

"""
tuples are good because they use less memory than lists
tuples are good for protecting the integrity of your data 
"""

title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("Coffee Table", 200, 100, 75, 34.50)
print(table[1] * table[2])

name, length, width, height, price = table
print(length * width)