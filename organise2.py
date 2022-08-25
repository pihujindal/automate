import os
import shutil
path='"C:/Users/Sakshi/Desktop/python/pro102/organiser.py"'
root,ext=os.path.splitext(path)
source='C:/Users/Sakshi/Desktop/python/pro102/test/text.txt'
destination='C:/Users/Sakshi/Desktop/python/pro102/move'
shutil.move(source,destination)