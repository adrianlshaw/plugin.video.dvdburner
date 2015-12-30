import sys
import xbmc

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

if __name__ == '__main__':
    message = "Clicked on '%s'" % sys.listitem.getLabel()
    xbmc.executebuiltin("Notification(\"This is a test!\", \"%s\")" % message)
