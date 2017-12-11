import numpy as np
import csv
import settings
from matplotlib import pyplot as plt


class Plot(object):

	def boxplot(data):
		
		# Create a figure instance
		fig = plt.figure(1, figsize=(9, 4))

		x = data
		########## voor boxplot
		# Create an axes instance
		ax = fig.add_subplot(111)
		bp = ax.boxplot(x)
		plt.grid(zorder=3, linewidth=1.2)
		labelfontsize=16
		plt.yticks(fontsize=14)

		# concurrency = [1,5,10]
		arr=[]

		i=1
		for xy in settings.concurrency:
			arr.append(i)
			print(xy)
			i+=1

		plt.xticks(arr,settings.concurrency, fontsize=10)


		plt.ylabel('Latency (sec)', fontsize=labelfontsize)
		plt.xlabel('Number of Workers', fontsize=labelfontsize)


		# Show the window
		fig.subplots_adjust(bottom=0.2)
		# plt.show()
		plt.savefig('foo.png')
