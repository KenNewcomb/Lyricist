import os
import commands
import dbus
import urllib
import re
import sys
def getSong():
	"""Grabs the currently playing song from Banshee"""
	Artist = os.popen('banshee --query-artist').readline().replace('artist: ', '').replace('\n', '')
	Title = os.popen('banshee --query-title').readline().replace('title: ', '').replace('\n', '')
	song = [Artist,Title]
	return song

