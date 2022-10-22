import os
import sys

# Usage:  python makepage.py foldername 
# Result: foldername.html

folder = sys.argv[-1]
images = os.listdir(folder)
images.sort()

filename = folder + '.html'
htmltext = '<html><head>' + folder + '</head><body><'
htmltext = '<!DOCTYPE html><html><head><title>' + folder + '</title><meta charset="UTF-8" /><link href="style.css" rel="stylesheet" /></head><body><div id="pagewrap"><div class="box"><h2>' + folder + '</h2><p>'

for image in images:
	htmltext += '<img src=\"' + folder + '/' + image + '\" title=\"' + image + '\"\\>\n'

htmltext += '</p></div></div></body></html>'

skrivfil = open(filename,'wb')
skrivfil.write(htmltext.encode('utf-8'))
skrivfil.close()