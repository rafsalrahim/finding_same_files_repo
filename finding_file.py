import os

#initialising the directory path to the spacific location
dir_name = os.getcwd()

for root, dirs, files in os.walk(dir_name):
    if files:
        for file in files:
            if os.path.splitext(file)[1] == '.mkv':
                print(file)
