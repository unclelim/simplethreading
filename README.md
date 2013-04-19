SimpleThreading
===============
SimpleThreading is a simple Python module that gives you the easy way to write your Python codes for processing data concurrently. It uses official Python's threading and Queue modules.

Example Of Usage
================
There are a few important functions in this module:

	.set_number_of_workers(<NUMBER>) - Set the numbers of workers (Threads) to work on your data simultaneously.

	.map_job(<JOB FUNCTION NAME>, <DATA>) - Map a job function with data.

	.run() - Start to execute the jobs

To see how to use this module, please see example.py.
