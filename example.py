# example.py
# This example shows you how to use SimpleThreading module to process a list of URLs.
#

from SimpleThreading import SimpleThreading
import httplib2
import time

def print_this(url):
    print url
    time.sleep(1)

urls = ['http://www.google.com', 'http://www.bing.com', 'http://www.yahoo.com']

s = SimpleThreading()
s.set_number_of_workers(2)

for url in urls:
    s.map_job(print_this, url)

s.run()
