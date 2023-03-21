from threading import *
''' 
Create the Thread Using without extending Thread Class
'''
class ThreadExample4:
    def display(self):
        for i in range(1, 5):
            print("****Hello****")



t=ThreadExample4() # Object Creation
thread=Thread(target=t.display())
thread.start()