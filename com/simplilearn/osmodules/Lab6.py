import os

'''
os.error() function defines the OS level Error .
It raise the OS Error in case of invalid or not accessable file and path
'''
try:
    filename="Python.txt"
    f=open(filename,'r')
    text = f.read()
    print(text)
    f.close()
except:
    print(os.error)
    print("Problem Reading the File ")


