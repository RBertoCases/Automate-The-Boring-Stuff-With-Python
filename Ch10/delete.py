#! Python3
import os
from pathlib import Path

for filename in Path.home().glob('*.txt'):

    #os.unlink(filename)

    print(filename)