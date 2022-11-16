import os

choice = input('''---------------------------------------------\n
These packages will be installed : \n
youtube_dl \n
yt_dlp n
moviepy \n
---------------------------------------------\n
>>>Enter to continue''')

if(choice == ''):
	os.system("py -m pip install youtube_dl")
	os.system("py -m pip install yt_dlp")
	os.system("py -m pip install moviepy")
