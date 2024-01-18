# Threads helps in using multiple cores and executing 2 or more tasks simultaneously
from time import sleep
from threading import *

class Hello(Thread):
    
    def run(self):
         for i in range(10):
             print("Hello")
             sleep(1)
             
class Hi(Thread):
    
    def run(self):
         for i in range(10):
             print("Hi")
             sleep(1)   
# We have 3 threads; main thread, thread_1, and thread_2             
thread_1 = Hello()
thread_2 = Hi()

thread_1.start()
sleep(0.2) # Prevent collision of threads
thread_2.start() 

# let main thread to wait for thread_1 and thread_2 to complete and print "bye" at the end using thread_1.join() and thread_2.join()
thread_1.join()
thread_2.join()

print("Bye") 