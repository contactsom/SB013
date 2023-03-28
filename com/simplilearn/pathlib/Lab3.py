from pathlib import Path
from os import chdir

path=Path('..')
print(f"Current Directory :{Path.cwd()}")
chdir(path)
print(f"Current Directory :{Path.cwd()}")
chdir(path)
print(f"Current Directory :{Path.cwd()}")