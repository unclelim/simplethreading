# SimpleThreading.py by UncleLim
from threading import Thread
from Queue import Queue
 
class SimpleThreadingWorker(Thread):
    def __init__(self, jobs):
        Thread.__init__(self)
        self.JOBS = jobs
        self.daemon = True
        self.start()
 
    def run(self):
        while True:
            job_function, data = self.JOBS.get()
            try:
                job_function(*data)
            except Exception, e:
                print e
 
            self.JOBS.task_done()
 
class SimpleThreading:
    NUMBER_OF_WORKERS = 1
 
    def __init__(self):
        self.JOBS = Queue()
 
    def set_number_of_workers(self, number_of_workers):
        self.NUMBER_OF_WORKERS = number_of_workers
 
        for _ in range(number_of_workers):
            SimpleThreadingWorker(self.JOBS)
 
    def map_job(self, job_function, *data):
        self.JOBS.put((job_function, data))
 
    def run(self):
        self.JOBS.join()
