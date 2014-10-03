import time
import sys
from modules import nowPlaying
from modules import fetchLyrics

def usage():
	print("Input Error.\nUsage:	lyricist.py\n	lyricist.py \"Artist\" \"Title\"")

# If Lyricist is executed without parameters
if(len(sys.argv) == 1):

	player = nowPlaying.getPID()

	if not player[0]:
		print("No song is currently playing, or the music player is not supported.")
		sys.exit()
	else:
		song = nowPlaying.getSong(player)
		lyrics = fetchLyrics.getLyrics(song)
		print(lyrics)
		while True:
			if song != nowPlaying.getSong(player):
				song = nowPlaying.getSong(player) 
				lyrics = fetchLyrics.getLyrics(song)
				print(lyrics)
			time.sleep(1)
# Help
elif(len(sys.argv) == 2):
	if(sys.argv[1] == 'help' or sys.argv[1] == '-h'):
		usage()
	else:
		usage()
	
# If launch parameters are given
elif(len(sys.argv) == 3):
	Artist = sys.argv[1]
	Title = sys.argv[2]
	fetchLyrics.getLyrics([Artist,Title])

else:
	usage()
