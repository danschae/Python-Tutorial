albums = [
  ("Welcome to my Nightmare", "Alice Copper", 1975),
  ("Bad Company", "Bad Company", 1974),
  ("Nightflight", "Budgie", 1981),
  ("More Mayhem", "Emilda May", 2011),
  ("Ridge the Lightning", "Metallica", 1984)
]

for name, artist, year in albums:
  print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))


for album in albums:
  name, artist, year = album
  print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))

