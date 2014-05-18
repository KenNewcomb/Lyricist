import os
import commands
import dbus

def getSong():
	"""Grabs the currently playing song from Banshee"""
	Artist = os.popen('banshee --query-artist').readline().replace('artist: ', '').replace('\n', '')
	Title = os.popen('banshee --query-title').readline().replace('title: ', '').replace('\n', '')
	song = "%s - %s" % (artist, title)
	return song

def getLyrics():
	song = getSong()
	
	Artist =
	artist = nopunc(Artist.replace('The', '')).lower()
	title = nopunc(Title).lower()

	# construct the lyrics URL
	urlstring = "http://www.azlyrics.com/lyrics/{0}/{1}.html".format(artist, title)
	# get the HTML at the proper URL
	lyricsf = urllib.urlopen(urlstring)

	# clean up the HTML file
	try:
		lyrics = lyricsf.read().split('<!-- start of lyrics -->')[1]
	except IndexError:
		print "Sorry, no lyrics were found."
		return
        
	lyrics = lyrics.split('<!-- end of lyrics -->')[0]
	# remove HTML tags
	lyrics = re.sub('<.*?>', '', lyrics)

	print "{0} by {1}".format(Title, Artist)
	print lyrics


getLyrics()
