from tkinter import Entry, Button, messagebox
from downloader.downloader import download_song

class MusicPlayer:
    def __init__(self, root, music_folder):
        self.root = root
        self.music_folder = music_folder

        # Cuadro para URL
        self.url_entry = Entry(self.root, width=50)
        self.url_entry.pack()

        # Botón para descargar
        download_btn = Button(self.root, text="Descargar de YouTube", command=self.download_song_gui)
        download_btn.pack()

    def download_song_gui(self):
        url = self.url_entry.get()
        if url:
            try:
                download_song(url, self.music_folder)
                messagebox.showinfo("Éxito", "Canción descargada.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo descargar: {e}")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una URL.")
