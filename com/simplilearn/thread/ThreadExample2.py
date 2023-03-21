from threading import *

def createThread():
    for i in range(1,5):
        print("****Hello****")


t=Thread(target=createThread)
t.start()

for i in range(1, 5):
    print("****main Thread****")
