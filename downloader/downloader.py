import yt_dlp
import re

def download_song(url, output_path):
    # 🔽 Limpiar el URL si tiene parámetros extra
    url = re.sub(r'\?.*$', '', url)  # elimina todo desde el signo de pregunta

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
