def make_album(artist_name, album_name):
	"""Displays the musicians name, album, and how many songs are in that album"""
	artist = {'artist name': artist_name, 'album name' : album_name}

	
	return artist

while True:
	print("\nPlease enter the name of the artist and the name of the album")
	print("(enter 'q' at any time to quit)")

	music_name = input("Artist name: ")
	
	if music_name == 'q':
		break

	alb_name = input("Album name: ")
	
	if alb_name == 'q':
		break

	formatted_album = make_album(music_name, alb_name)

	print(formatted_album)


