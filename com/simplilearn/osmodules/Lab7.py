import os

'''
os.error() function defines the OS level Error .
It raise the OS Error in case of invalid or not accessable file and path
'''
oldfilename="Python.txt"
newfilename="NEW_Python.txt"
os.rename(oldfilename,newfilename)

