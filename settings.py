# thx to https://stackoverflow.com/questions/13034496/using-global-variables-between-files
import threading

def init():

	# used to save thre result of the benchmark
    global resultDict
    resultDict = {}

    global current_num_requests, num_requests
    current_num_requests = 0
    num_requests = 100

    global request_times_concurrency
    request_times_concurrency = True

    # used to stop the threads
    global sendstop
    sendstop = False

    global concurrency, currentConcurrency
    concurrency = [1,5,10]
    currentConcurrency = 0

    global current_num_lock, maxrp
    current_num_lock = threading.Lock()
    maxrp = 1