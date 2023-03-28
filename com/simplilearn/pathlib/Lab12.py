from pathlib import Path
from shutil import copyfile

path=Path('/Users/om/SB013/com/simplilearn/')
print("-------------------------------")

pythonfilecount = 0
txtfilecount = 0
for e in path.rglob('*.py'):
    pythonfilecount=pythonfilecount+1
    print(e)
print("Total Python File ",pythonfilecount) # 359

print("-------------------------------")
for e in path.rglob('*.txt'):
    txtfilecount = txtfilecount + 1
    print(e)
print("Total Text File ", txtfilecount)  # 14