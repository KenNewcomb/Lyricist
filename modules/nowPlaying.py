import os
import subprocess
import dbus
import re
import sys

def getPID():
	"""Determines if a supported music player is currently running"""
	processes = subprocess.check_output('ps -A', shell=True).decode()
	software_list = ['banshee', 'rhythmbox']
	for software in software_list:
		if software in processes:
			return (True, software)
		else:
			return (False)

def getSong(software):
	"""Calls the proper function to determine currently playing song."""
	if(software[1] == 'banshee'):
		return Banshee()
	elif(software[1] == 'rhythmbox'):
		return Rhythmbox()

### Functions to gather 

def Banshee():
	"""Determines the currently playing song in Banshee."""
	Artist = subprocess.check_output('banshee --query-artist', shell=True).decode().replace('artist: ', '').replace('\n', '')
	Title = subprocess.check_output('banshee --query-title', shell=True).decode().replace('title: ', '').replace('\n', '')
	return (Artist, Title)

def Rhythmbox():
	"""Determines the currently playing song in Rhythmbox."""
	pass
