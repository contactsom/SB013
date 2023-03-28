from pathlib import Path
from shutil import copyfile

path=Path('/Users/om/SB013/com/simplilearn/pathlib/Lab1.py')

print(path)
print(path.as_uri())
print(path.as_posix())