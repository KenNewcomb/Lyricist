import time
import sys
from modules import nowPlaying
from modules import fetchLyrics

# If command line parameters are given, search for lyrics. "python lyricist.py "red hot chili peppers" "under the bridge"

if(len(sys.argv) >= 2):
	Artist = sys.argv[1]
	Title = sys.argv[2]
	fetchLyrics.getLyrics([Artist,Title])

# If no command line parameters are given, get current song from operating system.

else:
	player = nowPlaying.getPID()

	if not player:
		print("No song is currently playing, or the music player is not supported.")
		sys.exit()
	else:
		song = nowPlaying.getSong(player)
		fetchLyrics.getLyrics(song)

		while True:
			if song != nowPlaying.getSong(player):
				song = nowPlaying.getSong(player) 
				fetchLyrics.getLyrics(song)
			time.sleep(1)
