import time
import sys
from modules import nowPlaying
from modules import fetchLyrics	
# If parameters are given "python lyricist.py "red hot chili peppers" "under the bridge"

if(len(sys.argv) >= 2):
                Artist = sys.argv[1]
		Title = sys.argv[2]
		print(Artist, Title)
		fetchLyrics.getLyrics([Artist,Title])
else:
	song = nowPlaying.getSong()
	fetchLyrics.getLyrics(song)

	while True:
		if song != nowPlaying.getSong():
			song = nowPlaying.getSong() 
			fetchLyrics.getLyrics(song)
		time.sleep(1)
