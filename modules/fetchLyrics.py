import os
import commands
import dbus
import urllib
import re
import time
import sys

def nopunc(s):
    return ''.join(e for e in s if e.isalnum())

def getLyrics(song):
	"""Attempts to gather lyrics from various sources."""
	if(AZLyrics(song) != True):
		SongLyrics(song)

def AZLyrics(song):
	"""Fetches lyrics from AZLyrics.com"""

	# Prepare artist and title for lyrics search.
	artist = nopunc(song[0].replace('The', '')).lower()
	title = nopunc(song[1]).lower()
	
	# construct the lyrics URL
	urlstring = "http://www.azlyrics.com/lyrics/{0}/{1}.html".format(artist, title)
	
	# get the HTML at the proper URL
	lyrics = urllib.urlopen(urlstring)

	try:
		raw_lyrics = lyrics.read().split('<!-- start of lyrics -->')[1]
	except IndexError:
		print "AZLyrics: No lyrics found...\n"
		return False
	
	lyrics = raw_lyrics.split('<!-- end of lyrics -->')[0]
	
	processed_lyrics = re.sub('<.*?>', '', lyrics)
	
	generateTitle(song)
	print processed_lyrics
	return True

def SongLyrics(song):
	"""Fetches lyrics from SongLyrics.com"""

	artist = song[0].replace('The', '').replace(" ", "-").lower()
        title = song[1].replace(" ", "-").lower()
		
	# Construct the lyrics URL
	urlstring = "http://www.songlyrics.com/{0}/{1}-lyrics".format(artist,title)
	# Fetch the HTML at the URL
	lyrics = urllib.urlopen(urlstring)

	try:
		raw_lyrics = lyrics.read().split("<p id=\"songLyricsDiv\"  class=\"songLyricsV14 iComment-text\">")[1]
	except IndexError:
		print "SongLyrics: No lyrics found...\n"
		return False
	
	lyrics = raw_lyrics.split("</div>")[0]
	processed_lyrics = re.sub("<.*?>", "", lyrics).replace("&#039;", "'")
	
	generateTitle(song)
	print processed_lyrics
	return True

def generateTitle(song):
	Artist = song[0]
	Title = song[1]
	
	title = "{0} by {1}".format(Title, Artist)
	print title
	
	for characters in title:
		sys.stdout.write('-')		

	print "\n"
