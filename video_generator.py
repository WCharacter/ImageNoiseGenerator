import cv2
from os import listdir
from os import path
from config import dest, video_name, framerate

path = f'{path.curdir}\\{dest}' # if your images are not in current directory, change this

img_array = [f'{dest}\\{f}' for f in listdir(path)]

if(len(img_array)):
    size = cv2.imread(img_array[0]).shape[1::-1] # automatically detect video resolution
    print(size) 
    out = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), framerate, size)
    for i in img_array:
        if(i.endswith('.jpg') or i.endswith('.png')):
            out.write(cv2.imread(i))
    out.release()