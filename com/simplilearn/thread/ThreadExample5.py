from threading import *

print(current_thread().getName()) #MainThread
current_thread().setName("Simplilearn-Cisco Thread")
print(current_thread().getName()) #Simplilearn-Cisco Thread