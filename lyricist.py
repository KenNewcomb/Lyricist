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
	# Prepare Artist and Title for lyrics query.
	Artist = song[0]
	Title = song[1]
	artist = nopunc(Artist.replace('The', '')).lower()
	title = nopunc(Title).lower()
	
	AZLyrics(artist, title)

def AZLyrics(artist, title):
	# construct the lyrics URL
	urlstring = "http://www.azlyrics.com/lyrics/{0}/{1}.html".format(artist, title)
	# get the HTML at the proper URL
	lyrics = urllib.urlopen(urlstring)

	try:
		raw_lyrics = lyrics.read().split('<!-- start of lyrics -->')[1]
	except IndexError:
		print "AZLyrics: No lyrics found..."
		return false
	
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

# Program Start:
song = getSong()
getLyrics(song)

while True:
	if song != getSong():
		song = getSong() 
		raw_lyrics = getLyrics(song)
		processed_lyrics = cleanLyrics(raw_lyrics)
	time.sleep(1)
