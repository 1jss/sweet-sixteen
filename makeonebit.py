# Script that goes through a folder and converts all images to 1-bit png using PIL (PILLOW). Output is saved in a new folder.
# Usage:  python makeonebit.py foldername

# Import libraries
import os
import sys
from PIL import Image

# Read folder name from command line
folder = sys.argv[-1]

# Create new folder for output images
newfolder = folder + '_solid'
if not os.path.exists(newfolder):
	os.makedirs(newfolder)

# Get list of images in folder
images = os.listdir(folder)

# Loop through images and convert to 1-bit and save as .png in new folder
for image in images:
	print('Converting ' + image + ' to 1-bit')
	im = Image.open(folder + '/' + image)
	im = im.convert('RGBA')
	# Manually loop through pixels and convert to black or white
	for x in range(im.size[0]):
		for y in range(im.size[1]):
			# If pixel is transparent, convert to white
			alpha = im.getpixel((x,y))[3]
			if alpha < 128:
				im.putpixel((x,y), (255, 255, 255, 255))
			# If pixel is dark, convert to pure black
			elif im.getpixel((x,y))[0] < 128:
				im.putpixel((x,y), (0, 0, 0, 255))
			# If pixel is light, convert to pure white
			else:
				im.putpixel((x,y), (255, 255, 255, 255))
	im = im.convert('1', dither=Image.NONE)
	im.save(newfolder + '/' + image.split('.')[0] + ".png")

# Print confirmation
print('All images converted to 1-bit and saved in folder ' + newfolder)
