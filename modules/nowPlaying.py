import os
import subprocess
import dbus
import re
import sys

def getPID():
	"""Determines if a supported music player is currently running"""
	processes = subprocess.check_output('ps -A', shell=True).decode()
	software_list = ['banshee', 'rhythmbox']
	process_exists = False
	player = None
	for software in software_list:
		if software in processes:
			process_exists = True
			player = software
	return (process_exists, player)

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
	Artist = subprocess.check_output('rhythmbox-client --no-start --print-playing-format %aa', shell=True).decode()
	Title = subprocess.check_output('rhythmbox-client --no-start --print-playing-format %tt', shell=True).decode()
	return (Artist, Title)
