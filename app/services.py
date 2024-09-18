from config import Config
import os
import yt_dlp


def descargar_audio(video_url, video_title):
    try:

        # Utilizar el directorio desde la configuración
        audio_dir = Config.AUDIO_DIR

        # Asegúrate de que el directorio de audios exista
        if not os.path.exists(audio_dir):
            os.makedirs(audio_dir)

        # Opciones para yt-dlp para descargar solo el audio en formato MP3
        ydl_opts = {
            'format': 'bestaudio/best',
            # Añade mp3 automaticamente
            'outtmpl': os.path.join(audio_dir, f'{video_title}'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '128',
            }],
            'postprocessor_args': [
                '-ar', '44100',  # Frecuencia de muestreo
                '-ac', '2',      # Estéreo
            ],
            'prefer_ffmpeg': True,
            'noplaylist': True,
        }

        # Descargar el audio del video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        # Retornar la ruta del archivo descargado
        return os.path.join(audio_dir, f'{video_title}.mp3')
    except Exception as e:
        print(f"Error al descargar el audio: {e}")
        raise


def procesar_videos(video_urls_titles):
    # video_urls_titles es una lista de tuplas (video_url, video_title)
    # Ajusta max_workers según el número de hilos que desees
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_video = {executor.submit(descargar_audio, url, title): (
            url, title) for url, title in video_urls_titles}
        for future in as_completed(future_to_video):
            url, title = future_to_video[future]
            try:
                mp3_path = future.result()
                if mp3_path:
                    print(f"Descargado y convertido {url} a {mp3_path}")
            except Exception as e:
                print(f"Error con {url}: {e}")
