import os
import commands
import dbus
import urllib
import re
import time
import sys

def nopunc(s):
    return ''.join(e for e in s if e.isalnum())

def getSong():
	"""Grabs the currently playing song from Banshee"""
	Artist = os.popen('banshee --query-artist').readline().replace('artist: ', '').replace('\n', '')
	Title = os.popen('banshee --query-title').readline().replace('title: ', '').replace('\n', '')
	song = [Artist,Title]
	return song

def getLyrics(song):
	"""Fetches the lyrics from the internet"""
	Artist = song[0]
	Title = song[1]
	artist = nopunc(Artist.replace('The', '')).lower()
	title = nopunc(Title).lower()

	# construct the lyrics URL
	urlstring = "http://www.azlyrics.com/lyrics/{0}/{1}.html".format(artist, title)
	# get the HTML at the proper URL
	lyricsf = urllib.urlopen(urlstring)

	try:
		 lyrics = lyricsf.read().split('<!-- start of lyrics -->')[1]
	except IndexError:
		print "Sorry, no lyrics were found."
		return
	
	lyrics = cleanupLyrics(lyrics) 

	generateTitle(Title, Artist)
	print lyrics


def cleanupLyrics(lyrics):
	"""Cleans up lyrics"""
	lyrics = lyrics.split('<!-- end of lyrics -->')[0]
	# remove HTML tags
	lyrics = re.sub('<.*?>', '', lyrics)
	return lyrics

def generateTitle(Title, Artist):
	"""Generates a title for the lyrics"""
	title = "{0} by {1}".format(Title, Artist)
	print title
	
	for characters in title:
		sys.stdout.write('-')		

song = getSong()
getLyrics(song)
while True:
	if song != getSong():
		song = getSong() 
		getLyrics(song)
	time.sleep(1)
