
import os
from pygame import mixer

#initialising the directory path to the spacific location
dir_name = os.getcwd()
files=os.listdir(dir_name)
files_mp3=[i for i in files if i.endswith('.mp3')]
for x in file:
temp=dir_name + '/' + x
    mixer.init()
    mixer.music.load(temp)
    mixer.music.play()
