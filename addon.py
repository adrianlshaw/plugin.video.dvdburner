import sys
import time
import xbmc
import xbmcgui
import xbmcaddon
# Grab file name and add it to the queue
if __name__ == '__main__':
	filename = xbmc.getInfoLabel('ListItem.FileNameAndPath')
	filename = filename.replace(" ", "\ ")
	if filename.startswith('smb://'):
		__addon__ = xbmcaddon.Addon()
		__addonname__ = __addon__.getAddonInfo('name')
		title = "DVD burner"
		xbmcgui.Dialog().ok(__addonname__, "Sorry, this file cannot be burned.",
			"Network shares like SMB and NFS are unsupported.", "")
	else:
		f = open("/tmp/dvd_queue.txt","a")
		f.write(filename + "\n")
		f.close()
		time.sleep(3)
		xbmc.executebuiltin("Notification(\"%s\", \"Added to DVD queue\")" % filename)
