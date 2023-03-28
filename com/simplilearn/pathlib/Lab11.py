from pathlib import Path
from shutil import copyfile

path=Path('/Users/om/SB013/com/simplilearn/')
print("-------------------------------")

dirs=[ e for e in path.iterdir() if e.is_dir()]
print(dirs)
