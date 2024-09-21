from flask import Blueprint, jsonify, request, redirect, url_for, render_template
from app.models import db, Playlist, Video
from .rss_generator import generar_feed_rss

main = Blueprint('main', __name__)


@main.route('/add_playlist', methods=['GET', 'POST'])
def add_playlist():
    if request.method == 'POST':
        playlist_id = request.form.get('playlist_id')
        nombre = request.form.get('nombre')

        if playlist_id:
            # Verificar si la playlist ya existe
            playlist_existente = Playlist.query.filter_by(
                playlist_id=playlist_id).first()
            if not playlist_existente:
                # Crear y agregar la nueva playlist a la base de datos
                nueva_playlist = Playlist(
                    playlist_id=playlist_id, nombre=nombre)
                db.session.add(nueva_playlist)
                db.session.commit()
                return redirect(url_for('main.listar_playlists'))

    return render_template('add_playlist.html')


@main.route('/playlists')
def listar_playlists():
    playlists = Playlist.query.all()
    return render_template('playlists.html', playlists=playlists)


@main.route('/rss/<playlist_id>')
def generar_rss(playlist_id):
    videos = Video.query.filter_by(
        playlist_id=playlist_id).order_by(Video.fecha_publicacion).all()
    feed_xml = generar_feed_rss(videos)
    return feed_xml, 200, {'Content-Type': 'application/xml'}
