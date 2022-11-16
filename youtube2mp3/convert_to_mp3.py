from moviepy.editor import *
import os

directory = os.listdir()
lst = []
path = os.getcwd()
print(path)
for element in directory:
    if element[-5:] == ".webm" or element[-4:] == ".mkv":
        lst.append(element)

for element in lst:

    name_split = element.split("-")
    name = name_split[0] + "-" + name_split[1]
    videoClip = VideoFileClip(element)
    audioclip = videoClip.audio
    audioclip.write_audiofile(name + ".mp3")
    audioclip.close()
    videoClip.close()

for element in directory:
    if element[-5:] == ".webm" or element[-4:] == ".mkv":
        os.remove(f"{path}/{element}")