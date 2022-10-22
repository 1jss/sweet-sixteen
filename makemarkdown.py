import os
import sys

# Usage:  python makepage.py foldername
# Result: foldername.md

folder = sys.argv[-1]
images = os.listdir(folder)
images.sort()

filename = folder + '.md'
htmltext = ''

for image in images:
	htmltext += '![' + image + '](' + folder + "/" + image + ')\n'

skrivfil = open(filename,'wb')
skrivfil.write(htmltext.encode('utf-8'))
skrivfil.close()
