import yt_dlp
import webbrowser

ytdl = yt_dlp.YoutubeDL()
run = True

while run:

    lien = input("Entrez le lien youtube de la vidéo : ")

    video = ytdl.extract_info(lien, download=True)

    nav = input("Ouvrir le navigateur ('enter' : non / n'importe quelle touche : oui) ?")
    if nav != "" :
        webbrowser.open(video['url'])

    end = input("Télécharger une autre vidéo ('enter' : non / n'importe quelle touche : oui) ?")

    if end != "":
        run = False

#https://www.youtube.com/watch?v=dQw4w9WgXcQ
#https://www.youtube.com/watch?v=5B8Xb87smTE
