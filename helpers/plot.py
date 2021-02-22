import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import json, os

# https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html
def plot_coords(x,y, sessionid, task):
	plt.title(str(task).upper()+' TASK - X and Y coordinates')
	plt.plot(x, y)
	plt.savefig(task+'.png')
	plt.xlabel('X coordinate')
	plt.ylabel('Y coordinate')
	plt.close()
	
os.chdir('/Users/jim/desktop/vibe/upload/test')
listdir=os.listdir()
jsonfiles=list()
for i in range(len(listdir)):
	if listdir[i].endswith('.json'):
		jsonfiles.append(listdir[i])

for i in range(len(jsonfiles)):
	data=json.load(open(jsonfiles[i]))
	xy=data['data']
	sessionid=data['sessionId']
	task=jsonfiles[i].replace('.json','')

	x=list()
	y=list()
	for j in range(len(xy)):
		x.append(xy[j][0])
		y.append(xy[j][1])
	plot_coords(x,y, sessionid, task)


