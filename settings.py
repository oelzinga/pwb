# thx to https://stackoverflow.com/questions/13034496/using-global-variables-between-files
import threading

def init():

	# used to save thre result of the benchmark
    global resultDict
    resultDict = {}

    global current_num_requests, num_requests
    current_num_requests = 0
    num_requests = 10

    global request_times_concurrency
    request_times_concurrency = True

    # used to stop the threads
    global sendstop
    sendstop = False

    global concurrency, currentConcurrency
    concurrency = [1]
    # concurrency = [25,30]
    currentConcurrency = 0

    global current_num_lock, maxrp
    current_num_lock = threading.Lock()
    maxrp = 1

    global plotID
    plotID = 1

    global testName
    testName = "test1"

    global contentDir
    contentDir="./content"
  

    global resultBuildUp
    resultBuildUp = {"2":"request 1","1":"request 2","0":"both requests"}
