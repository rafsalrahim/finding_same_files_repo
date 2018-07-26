import os

#initialising the directory path to the spacific location
dir_name = os.getcwd()

'''for root, dirs, files in os.walk(dir_name):
    if files:
        for file in files:
            if os.path.splitext(file)[1] == '.mkv':
                print(file)'''

#alternative : faster
files=os.listdir(cwd)
files_mkv=[i for i in files if i.endswith('.mkv')]
print (files_mkv)
