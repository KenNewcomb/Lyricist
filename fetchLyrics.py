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
	AZLyrics(song) #AZLyrics.com


def AZLyrics(song):

	artist = nopunc(song[0].replace('The', '')).lower()
	title = nopunc(song[1]).lower()
	
	# construct the lyrics URL
	urlstring = "http://www.azlyrics.com/lyrics/{0}/{1}.html".format(artist, title)
	# get the HTML at the proper URL
	lyrics = urllib.urlopen(urlstring)

	try:
		raw_lyrics = lyrics.read().split('<!-- start of lyrics -->')[1]
	except IndexError:
		print "AZLyrics: No lyrics found..."
		return False
	
	raw_lyrics = raw_lyrics.split('<!-- end of lyrics -->')[0]
	
	processed_lyrics = cleanLyrics(raw_lyrics) 

	print processed_lyrics
	return True


def cleanLyrics(lyrics):
	"""Cleans up lyrics, removing HTML tags"""
	# remove HTML tags
	lyrics = re.sub('<.*?>', '', lyrics)
	return lyrics
	
	
	title = "{0} by {1}".format(Title, Artist)
	print title
	
	for characters in title:
		sys.stdout.write('-')		

