import os
import shutil

path='C:/Users/Sakshi/Desktop/python/pro102/images'
listoffiles=os.listdir(path)
for file in listoffiles:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=='':
        continue
  
    if os.path.exists(path+'/'+ext):
         print('Moving'+file+'......')
         shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
        
    else: 
        os.makedirs(path+'/'+ext)
        print('Moving'+file+'......')
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)