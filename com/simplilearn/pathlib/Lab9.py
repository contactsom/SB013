from pathlib import Path
from shutil import copyfile

path=Path('/Users/om/SB013/com/simplilearn/pathlib/Lab1.py')

home=path.home()
print(home)

relativepath=path.relative_to(home)
print(relativepath)