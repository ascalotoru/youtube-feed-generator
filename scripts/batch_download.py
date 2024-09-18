from googleapiclient.discovery import build
from config import Config
from app.services import descargar_audio
from app.models import db, Video, Playlist
from datetime import datetime


def procesar_playlist(playlist_id):
    api_key = Config.YOUTUBE_API_KEY
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50
    )
    response = request.execute()

    for item in response['items']:
        video_id = item['snippet']['resourceId']['videoId']
        video_title = item['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        fecha_publicacion = item['snippet']['publishedAt']

        # Verificar si el video ya está descargado en la base de datos
        video_existente = Video.query.filter_by(video_id=video_id).first()
        if video_existente:
            continue  # Si ya está descargado, lo ignoramos

        # Descargar el audio como MP3
        try:
            mp3_path = descargar_audio(video_url, video_title)
        except Exception as e:
            print(f"Error al descargar el video {video_id}: {e}")
            continue

        # Guardar en la base de datos el video descargado
        nuevo_video = Video(
            video_id=video_id,
            titulo=video_title,
            descripcion=item['snippet']['description'],
            mp3_path=mp3_path,
            fecha_publicacion=datetime.strptime(
                fecha_publicacion, "%Y-%m-%dT%H:%M:%SZ"),
            playlist_id=playlist_id
        )
        db.session.add(nuevo_video)
        db.session.commit()


def procesar_playlists():
    playlists = Playlist.query.all()
    for playlist in playlists:
        procesar_playlist(playlist.playlist_id)


if __name__ == "__main__":
    # Configura la aplicación y la base de datos
    from app import create_app
    app = create_app()
    with app.app_context():
        procesar_playlists()
