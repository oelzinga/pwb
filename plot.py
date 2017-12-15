import settings
import numpy as np
from matplotlib import pyplot as plt


class Plot(object):

	def boxplot(data, name):
		plt.close('all')
		# Create a figure instance
		fig = plt.figure(1, figsize=(9, 4))

		x = data
		########## voor boxplot
		# Create an axes instance
		ax = fig.add_subplot(111)
		settings.plotID+=1
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
		print(str(settings.contentDir)+"/"+str(settings.testName)+"/"+str(name)+".png")
		plt.savefig(str(settings.contentDir)+"/"+str(settings.testName)+"/"+str(name)+".png")


	def lineGraph(data, name):
		plt.close('all')
		x = []
		print("=====")
		print(len(x))
		x.append(data)
		print(len(x))
		try:
			print(len(x[0]))
		except:
			pass
		# Create a figure instance
		print("+===+")
		fig = plt.figure(1, figsize=(9, 4))

		# Create an axes instance
		ax = fig.add_subplot(111)
		settings.plotID+=1
		# bp = ax.boxplot(x)

		########## for line graphphs
		# https://stackoverflow.com/questions/8409095/matplotlib-set-markers-for-individual-points-on-a-line
		i=0


		linestyle= ['-','-','-','-','-','-']
		# marker = ['p','o','s','3','D','+']
		color = ['green','black','orange','cyan','blue','red']
		marker = ['p','o','s','3','D','*']
		for y in x:
		    # plt.plot(y, [linestyle[i], color[i], marker[i]])
		    # plt.plot(y, linestyle=linestyle[i], marker=marker[i], color=color[i])
		    plt.plot(y, linestyle=linestyle[i], color=color[i])
		    i+=1


		plt.grid(zorder=3, linewidth=1.2)


		labelfontsize=16
		plt.yticks(fontsize=14)

		plt.ylabel('Latency (sec)', fontsize=labelfontsize)
		# plt.ylabel('Memory usage (KB)', fontsize=labelfontsize)
		plt.xlabel('Number of measurements', fontsize=labelfontsize)

		plt.xlim(0, len(data)) # iozone read



		# Show the window
		fig.subplots_adjust(bottom=0.2)
		plt.savefig(str(settings.contentDir)+"/"+str(settings.testName)+"/"+str(name)+".png")