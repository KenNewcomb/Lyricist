import os
import dbus
import urllib.request
import re
import time
import sys

def getLyrics(song):
	"""Attempts to gather lyrics from various sources."""
	foundlyrics = False
	lyrics = None
	
	(foundlyrics, lyrics) =  AZLyrics(song)
	if foundlyrics == True:
		return lyrics
	
	(foundlyrics, lyrics) = SongLyrics(song)
	if foundlyrics == True:
		return lyrics	

def AZLyrics(song):
	"""Fetches lyrics from AZLyrics.com"""
	# Prepare artist and title for lyrics search.
	artist = nopunc(song[0].replace('The', '')).lower()
	title = nopunc(song[1]).lower()
	
	# construct the lyrics URL
	urlstring = "http://www.azlyrics.com/lyrics/{0}/{1}.html".format(artist, title)
	
	# get the HTML at the proper URL
	try:
		lyrics = urllib.request.urlopen(urlstring)
	except urllib.request.HTTPError:
		print("AZLyrics: No lyrics found...\n")
		return (False, None)

	# Extract lyrics from HTML
	lyrics = lyrics.read().decode(('utf-8')).split('<!-- start of lyrics -->')[1]
	lyrics = lyrics.split('<!-- end of lyrics -->')[0]
	
	# Remove HTML tags
	lyrics = re.sub('<.*?>', '', lyrics)
	
	# Generate a title bar for the lyrics.
	title = generateTitle(song)
	lyrics = title + lyrics

	return (True, lyrics)

def SongLyrics(song):
	"""Fetches lyrics from SongLyrics.com"""
	# Prepare artist and title for lyrics search.
	artist = song[0].replace('The', '').replace(" ", "-").lower()
	title = song[1].replace(" ", "-").lower()
		
	# Construct the lyrics URL
	urlstring = "http://www.songlyrics.com/{0}/{1}-lyrics".format(artist,title)
	
	# get the HTML at the proper URL
	try:
		lyrics = urllib.request.urlopen(urlstring)
	except urllib.request.HTTPError:
		print("SongLyrics: No lyrics found...\n")
		return (False, None)

	# Extract lyrics from HTML
	lyrics = lyrics.read().decode(('utf-8')).split("<p id=\"songLyricsDiv\"  class=\"songLyricsV14 iComment-text\">")[1]
	lyrics = lyrics.split("</div>")[0]
	
	# Remove HTML tags	
	lyrics = re.sub("<.*?>", "", lyrics).replace("&#039;", "'")
	
	# Generate a title bar for the lyrics
	title = generateTitle(song)
	lyrics = title + lyrics
	return (True, lyrics)


def generateTitle(song):
	Artist = song[0]
	Title = song[1]
	
	title = ("{0} by {1}".format(Title, Artist) + '\n')
	for characters in title:
		title = (title + '-')

	return title
def nopunc(s):
    return ''.join(e for e in s if e.isalnum())
