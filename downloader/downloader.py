import yt_dlp
import re
import os

def sanitize_filename(title):
    """Limpia el título para que sea un nombre de archivo seguro."""
    # Elimina caracteres que no son alfanuméricos, guiones bajos o puntos
    sanitized_title = re.sub(r'[^\w\s.-]', '', title)
    # Reemplaza espacios con guiones bajos
    sanitized_title = sanitized_title.replace(' ', '_')
    return sanitized_title

def download_song(url, output_path):
    """Descarga la mejor calidad de audio de un video de YouTube y lo convierte a MP3."""
    # Limpiar el URL si tiene parámetros extra
    url = re.sub(r'\?.*$', '', url)  # elimina todo desde el signo de pregunta

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,  # Cambiado a True para no mostrar tanta información en la terminal
        'progress_hooks': [lambda d: print(f"Descargando: {d['filename']}" if d['status'] == 'downloading' else '')], # Ejemplo básico de progreso
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            if info_dict and 'title' in info_dict:
                sanitized_title = sanitize_filename(info_dict['title'])
                ydl_opts['outtmpl'] = f'{output_path}/{sanitized_title}.mp3' # Forzar la extensión a mp3 después de la conversión
            ydl.download([url])
        return True  # Indica que la descarga fue exitosa
    except yt_dlp.DownloadError as e:
        print(f"Error al descargar {url}: {e}")
        return False # Indica que la descarga falló
    except Exception as e:
        print(f"Ocurrió un error inesperado al descargar {url}: {e}")
        return False # Indica que la descarga falló
    except Exception as e:
        print(f"Ocurrió un error inesperado al descargar {url}: {e}")
        print(f"Tipo de error: {type(e)}")
        return False

if __name__ == '__main__':
    # Ejemplo de uso (esto se ejecuta solo si ejecutas downloader.py directamente)
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Un clásico...
    output_directory = "musica_descargada"
    os.makedirs(output_directory, exist_ok=True)
    if download_song(video_url, output_directory):
        print(f"Descarga completada en: {output_directory}")
    else:
        print("La descarga falló.")