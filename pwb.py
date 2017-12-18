import sys, os, json, time
import settings
import threading
import numpy
from flask import Flask
from flask import request
from webworker import WebWorker
from excel import excel
from latexOutput import latexOutput


def createThreadObject():
	# create thread objects for the current benchmark
	i = 0
	print(settings.currentConcurrency)
	while i < settings.currentConcurrency:
		# 	see if: thread object (key) already excists
		#	if not: create new thread object
		if str(i) in threadDict:
			i+=1
			print("thread already excists")
			# time.sleep(1)
		else:
			threadDict[str(i)] = threading.Thread(name=i,target=WebWorker().run,args=(i,))
			i+=1
			print('starting thread: '+str(i))
			# time.sleep(1)


def startThreads():
	# 	for each thread object
	# 	see if: thread is alive (already started)
	#	if not: start the thread
	for threads, value in threadDict.items():
		if threadDict[threads].isAlive():
			print("threads is running")
		else:
			threadDict[threads].start()
			print('thread should be started')


def stopThreads():
	for threads, value in threadDict.items():
		threadDict[threads].join()

def runBenchmarks():
	for conq in settings.concurrency:
		
		settings.currentConcurrency = conq
		# create dict for current test
		settings.resultDict[str(settings.currentConcurrency)] = {}
		# create array for raw data
		settings.resultDict[str(settings.currentConcurrency)]["raw"] = []

		# 1: create thread objects
		createThreadObject()

		# 2: start threads for current benchmark
		startThreads()

		# 	3: 	refresh the request counter
		# 		after the request counter is set, the workers can start sending requests
		if settings.request_times_concurrency == True:
			settings.current_num_requests = settings.num_requests * settings.currentConcurrency + 1
		else:
			settings.current_num_requests = settings.num_requests + 1


		# 	4: 	wait for workers to finish
		while settings.current_num_requests > 0:
			time.sleep(2)
			print("conq is running")


		print("benchmark is finished, in total there are "+str(len(settings.resultDict[str(settings.currentConcurrency)]["raw"]))+" result collected ")


def createDIRS():
	
	if not os.path.isdir(str(settings.contentDir)):
		os.makedirs(str(settings.contentDir))
	
	# Make sure dir exists
	if os.path.isdir(str(settings.contentDir)):
		pass
	else:
		print(str(settings.contentDir)+" was not created successfully")
		sys.exit(str(settings.contentDir)+" was not created successfully")


	# IF:	test is already been done, exit
	# ELSE:	creat dir
	if os.path.isdir(str(settings.contentDir)+"/"+str(settings.testName)):
		# print(str(settings.contentDir)+"/"+str(settings.contentDir)+" test ID already exists")
		sys.exit(str(settings.contentDir)+"/"+str(settings.contentDir)+" test ID already exists")
	else:	
		os.path.isdir(str(settings.contentDir)+"/"+str(settings.testName))
		os.makedirs(str(settings.contentDir)+"/"+str(settings.testName))

	# Make sure dir exists
	if os.path.isdir(str(settings.contentDir)+"/"+str(settings.testName)):
		pass
	else:
		print(str(settings.contentDir)+"/"+str(settings.testName)+" was not created successfully")
		sys.exit(str(settings.contentDir)+"/"+str(settings.testName)+" was not created successfully")

def calcStatistics():
	for key in settings.concurrency:
	    settings.resultDict[str(key)]["avg"] = numpy.mean(settings.resultDict[str(key)]["raw"])
	    settings.resultDict[str(key)]["std"] = numpy.std(settings.resultDict[str(key)]["raw"])
	    settings.resultDict[str(key)]["median"] = numpy.median(settings.resultDict[str(key)]["raw"])
	    settings.resultDict[str(key)]["min"] = min(settings.resultDict[str(key)]["raw"])
	    settings.resultDict[str(key)]["max"] = max(settings.resultDict[str(key)]["raw"])




# dict to put all thread objects in
threadDict = {}

# load shared variables
settings.init()

# create dirs stop if
createDIRS()

# run the benchmarks
runBenchmarks()

print("Program is closing...")

# send stop to the workers
settings.sendstop = True

# wait brief second before threads are stopped
time.sleep(0.1)

# Close threads, stop program
stopThreads()



result=[]

# print(settings.resultDict)

calcStatistics()
print("calc is done")
excel.printXLSX()
print("excel is done")


from plot import Plot
for key in settings.concurrency:
	# print(key)
	# print(settings.resultDict[str(key)])
	Plot.lineGraph(settings.resultDict[str(key)]["raw"],str(settings.testName)+"-lineGraph-"+str(key))
	result.append(settings.resultDict[str(key)]["raw"])

# process data
Plot.boxplot(result,str(settings.testName)+"-boxplot")

latexOutput.save()

print(settings.resultDict)

# exit script
sys.exit(0)