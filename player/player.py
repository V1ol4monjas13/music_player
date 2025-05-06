import os
import random
import pygame
import tkinter as tk
from tkinter import messagebox, Listbox, END, Entry, Button
from downloader.downloader import download_song
import re

def is_youtube_url(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        r'(youtube|youtu)\.(com|be)/'
        r'(watch\?v=|embed/|v/|)([a-zA-Z0-9\-\_]+)'
    )
    match = re.search(youtube_regex, url)
    return bool(match)

class MusicPlayer:
    def __init__(self, root, music_folder):
        self.root = root
        self.root.title("Reproductor de Música")
        self.music_folder = music_folder
        self.playlist = []
        self.current_song = None
        self.is_paused = False

        pygame.mixer.init()
        self.load_songs()

        # --- Interfaz del Reproductor ---
        self.song_listbox = Listbox(root, width=50, height=15)
        self.song_listbox.pack(pady=10)

        for song in self.playlist:
            self.song_listbox.insert(END, song)

        tk.Button(root, text="Play", command=self.play_song).pack()
        tk.Button(root, text="Pausa", command=self.pause_song).pack()
        tk.Button(root, text="Stop", command=self.stop_song).pack()
        tk.Button(root, text="Aleatorio", command=self.play_random).pack()

        # --- Interfaz de Descarga ---
        tk.Label(root, text="Descargar desde YouTube:").pack(pady=5)
        self.url_entry = Entry(root, width=50)
        self.url_entry.pack()
        download_btn = Button(root, text="Descargar", command=self.download_song_gui)
        download_btn.pack(pady=5)

    def load_songs(self):
        if not os.path.exists(self.music_folder):
            messagebox.showerror("Error", f"No se encontró la carpeta: {self.music_folder}")
            return
        for file in os.listdir(self.music_folder):
            if file.endswith(".mp3"):
                full_path = os.path.join(self.music_folder, file)
                self.playlist.append(full_path)

    def play_song(self):
        try:
            selected_index = self.song_listbox.curselection()
            if not selected_index:
                return
            song_path = self.playlist[selected_index[0]]
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            self.current_song = song_path
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def pause_song(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        self.is_paused = not self.is_paused

    def stop_song(self):
        pygame.mixer.music.stop()

    def play_random(self):
        song_path = random.choice(self.playlist)
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        self.current_song = song_path

    def download_song_gui(self):
        url = self.url_entry.get()
        if url:
            if is_youtube_url(url):
                try:
                    if download_song(url, self.music_folder):
                        messagebox.showinfo("Éxito", "Canción descargada.")
                        self.load_songs()
                        self.song_listbox.delete(0, END)
                        for song in self.playlist:
                            self.song_listbox.insert(END, song)
                    else:
                        messagebox.showerror("Error", "No se pudo descargar la canción. Verifica la URL o tu conexión.")
                except Exception as e:
                    messagebox.showerror("Error", f"Ocurrió un error: {e}")
            else:
                messagebox.showwarning("Advertencia", "Por favor, introduce una URL válida de YouTube.")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una URL.")

if __name__ == '__main__':
    root = tk.Tk()
    music_folder = "musica_reproducccion" # Asegúrate de que esta carpeta exista o ajústala
    player = MusicPlayer(root, music_folder)
    root.mainloop()