import imageio
import os

folder = 'pics' 
files = [f"{folder}/{file}" for file in os.listdir(folder)]
files.sort()

images = [imageio.imread(file) for file in files]
imageio.mimwrite('movie.gif', images, fps=1)