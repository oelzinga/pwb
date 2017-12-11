import sys, os, json, time
import settings
import threading
from flask import Flask
from flask import request
from webworker import WebWorker

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
		settings.resultDict[str(settings.currentConcurrency)] = []

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


		print("benchmark is finished, in total there are "+str(len(settings.resultDict[str(settings.currentConcurrency)]))+" result collected ")



# dict to put all thread objects in
threadDict = {}

# load shared variables
settings.init()

# run the benchmarks
runBenchmarks()

print("Program is closing...")

# send stop to the workers
settings.sendstop = True

# wait brief second before threads are stopped
time.sleep(0.1)

# Close threads, stop program
stopThreads()

# exit script
sys.exit(0)