from pathlib import Path
from shutil import copyfile

homepath= Path().home()
print(homepath) # /Users/om

newpath=homepath / 'SB013'
print(newpath)


newpath = newpath / 'simplilearn'
print(newpath)



# SB013