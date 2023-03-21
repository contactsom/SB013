import threading

print("Name of Current Execution Thread ",threading.current_thread().getName()) # MainThread OLD
print("Name of Current Execution Thread ",threading.current_thread()) # <_MainThread(MainThread, started 4345169280)> NEW