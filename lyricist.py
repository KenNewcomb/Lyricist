import os
import commands
import dbus
import urllib
import re
import time
import sys
import fetchLyrics, nowPlaying
	
# Program Start:
song = nowPlaying.getSong()
fetchLyrics.getLyrics(song)

while True:
	if song != nowPlaying.getSong():
		song = nowPlaying.getSong() 
		fetchLyrics.getLyrics(song)
	time.sleep(1)
