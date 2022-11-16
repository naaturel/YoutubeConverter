import yt_dlp
import webbrowser

ytdl = yt_dlp.YoutubeDL()
run = True

while run:

    lien = input("Enter a youtube video url: ")

    video = ytdl.extract_info(lien, download=True)

    nav = input("Open brower ? ('enter' : no / any key : yes)")
    if nav != "" :
        webbrowser.open(video['url'])

    end = input("Download again ? ('enter' : no / any key : oui) ?")

    if end != "":
        run = False

#https://www.youtube.com/watch?v=dQw4w9WgXcQ
#https://www.youtube.com/watch?v=5B8Xb87smTE
