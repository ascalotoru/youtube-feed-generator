# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.String(50), unique=True, nullable=False)
    nombre = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Playlist {self.nombre}>"


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(50), unique=True, nullable=False)
    titulo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    mp3_path = db.Column(db.String(255), nullable=False)
    fecha_publicacion = db.Column(db.DateTime, nullable=False)
    playlist_id = db.Column(db.String(50), db.ForeignKey(
        'playlist.playlist_id'), nullable=False)
    orden = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Video {self.titulo}>"
