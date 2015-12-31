import sys
import time
import xbmc
import xbmcgui
import xbmcaddon

# Takes in a list of filenames and spits out an XML file
	# They are expected to have .mpg extension
	def generate_xml(files):
		xml = "<dvdauthor>"
		xml += "<vmgm />"
		xml += "<titleset>"
		xml += "<titles>"
	
		for video in files:
			xml += "<pgc>"
			xml += "<vob file=\"" + video + "\" />"
			xml += "</pgc>"
		xml += "</titles>"
		xml += "</titleset>"
		xml += "</dvdauthor>"
		return xml

# Grab file names and prepare to generate data for dvdauthor
if __name__ == '__main__':
	xbmc.executebuiltin("Notification(\"Finalising DVD...\", \"\")")
	f = open('/tmp/dvd_queue.txt','r')
	lines = []
	for line in f:
		lines.append(line) # Need to check if file is MPEG formatted
	f.close()

	if len(lines) == 0:
		__addon__ = xbmcaddon.Addon()
		__addonname__ = __addon__.getAddonInfo('name')
		xbmcgui.Dialog().ok(__addonname__, "DVD burner", 
				"No videos have been added!", "")
		return None
	dvdauthor_xml = generate_xml(lines)
	# Now to hand it to dvdauthor somehow
	# Delete the queue
