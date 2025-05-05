from tkinter import Tk
from player import MusicPlayer  # si está en __init__.py

music_folder = "C:\\Users\\gavil\\Desktop\\piton\\proyecto_BOTpy\\musica_reproducccion"

root = Tk()
app = MusicPlayer(root, music_folder)
root.mainloop()



# from downloader.downloader import download_song
# url = input("URL: ")

# url = "https://youtu.be/MqsQI2Di2xY"  # ✅ Esto debe estar definido
# output_path = "C:\\Users\\gavil\\Desktop\\piton\\proyecto_BOTpy\\musica_reproducccion"

# download_song(url, output_path)
