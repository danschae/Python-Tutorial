from nested_data import albums

SONGS_LIST_INDEX = 3 # all capital varialbes mean constants in python but you can technically edit em
SONG_INDEX = 1
while True:
  print("Please choose your album:")
  for index, (title, artist, year, songs) in enumerate(albums):
    print("{}: {}".format(index + 1, title))

  choice = int(input())
  if 1 <= choice <= len(albums):
    songs_list = albums[choice - 1][SONGS_LIST_INDEX]

    print("Please choose what song to play?")
    for index, song in songs_list:
      print("{}: {}".format(index, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
      title = songs_list[song_choice - 1][SONG_INDEX]
      print("Now Playing: {}".format(title))
      break
    print("=" * 40)