from PIL import Image
import os, sys

path = os.getcwd()
dirs = os.listdir( path )

def resize():
	for item in dirs:
		print(item)
		if item.endswith('.png'):
			im = Image.open(path+'/'+item)
			f, e = os.path.splitext(path+'/'+item)
			imResize = im.resize((480,344), Image.ANTIALIAS)
			imResize.save(f + '_resized.png', 'PNG', quality=90)

resize()