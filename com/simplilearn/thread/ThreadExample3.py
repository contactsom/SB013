from threading import *
''' 
Create the Thread Using Thread Class
'''
class ThreadExample3(Thread):

    def run(self) :
        for i in range(1,5):
            print("Child Thread")

t = ThreadExample3()
t.start()