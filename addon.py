import sys
import xbmc
import time

# Grab file name and add it to the queue
if __name__ == '__main__':
	filename = sys.listitem.getInfoLabel("ListItem.FileNameAndPath")
	message = "Clicked on '%s'" % sys.listitem.getLabel()
	xbmc.executebuiltin("Notification(\"%s\", \"Added to DVD queue\")" % message)
	f = open("/tmp/dvd_queue.txt","a")
	f.write(filename)
	f.close()
