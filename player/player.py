import os
import random
import pygame
import tkinter as tk
from tkinter import messagebox, Listbox, END

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

        # Interfaz
        self.song_listbox = Listbox(root, width=50, height=15)
        self.song_listbox.pack(pady=10)

        for song in self.playlist:
            self.song_listbox.insert(END, song)

        # Botones
        tk.Button(root, text="Play", command=self.play_song).pack()
        tk.Button(root, text="Pausa", command=self.pause_song).pack()
        tk.Button(root, text="Stop", command=self.stop_song).pack()
        tk.Button(root, text="Aleatorio", command=self.play_random).pack()

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
