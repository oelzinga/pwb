import settings
import time, subprocess, psutil, json, threading
from benchmark import Benchmark

class WebWorker(threading.Thread):

	def run(self, i):
		print("woker statedasdsa")
		while True:
			# if sendstop is True, break the while loop
			if settings.sendstop: break

			# 	if:	counter is not 0 do -1
			#	else: if counter is 0 (workers could be done and waiting for the programm to stop) set conq to 0s
			if settings.current_num_requests != 0: 
				# with lock (current_num_lock) lower current_num_requests by -1
				# if lock is not used the application can do more request then wanted 
				# since multiple wokers al lowering the counter at the same time
				with settings.current_num_lock:
					# check (with the lock) if current_num_requests is not 0 in the mean time
					# to make sure no mistakes are made
					if settings.current_num_requests > 0: 
						settings.current_num_requests-=1
						conq = settings.current_num_requests
					else:
						conq = 0						
			else:
				conq = 0

			# if the worker is not idle: to something
			if conq > 0: 
				##
				## INSERT code here
				##
				####################
				result = Benchmark.ergosleep()
				####################
				settings.resultDict[str(settings.currentConcurrency)].append(result)
			else:
				time.sleep(1)

