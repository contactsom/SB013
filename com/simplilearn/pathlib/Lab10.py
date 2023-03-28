from pathlib import Path
from shutil import copyfile

path=Path('/Users/om/SB013/com/simplilearn/pathlib/Lab1.py')


print(f" The Part is : {path.parts}")
print(f" The Drive is : {path.drive}")
print(f" The Root is : {path.root}")
print("-------------------------------")
print(f" The Name is : {path.name}")
print(f" The Steam is : {path.stem}")
print(f" The anchor is : {path.anchor}")