import os
for root, dirs, files in os.walk("/home/rafsal/Videos/Songs"):
    if files:
        for file in files:
            if os.path.splitext(file)[1] == '.mkv':
                print(file)
