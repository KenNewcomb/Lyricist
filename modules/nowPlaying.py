import os
import subprocess
import dbus
import re
import sys

def getPID():
	"""Determines if a supported music player is currently running"""
	processes = subprocess.check_output('ps','-A')
	software = ['banshee', 'rhythmbox']
	if software in processes:
		getSong(software)
	else:
		return False
def getSong():
	"""Grabs the currently playing song from Banshee"""
	Artist = subprocess.check_output('banshee --query-artist', shell=True).decode().replace('artist: ', '').replace('\n', '')
	Title = subprocess.check_output('banshee --query-title', shell=True).decode().replace('title: ', '').replace('\n', '')
	song = [Artist,Title]
	return song
