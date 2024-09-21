from feedgen.feed import FeedGenerator
from flask import url_for
from pytz import UTC
from urllib.parse import quote


def generar_feed_rss(videos):
    fg = FeedGenerator()
    fg.title('Podcast desde YouTube')
    fg.link(href='https://miweb.com/rss')
    fg.description('Podcast generado dinámicamente a partir de YouTube')

    for video in videos:
        fe = fg.add_entry()
        fe.title(video.titulo)
        # fe.link(href=video.url)
        fe.description(video.descripcion)
        mp3_url = url_for(
            'static', filename=f'audio/{quote(video.mp3_path.split("/")[-1])}',
            _external=True)
        fe.enclosure(mp3_url, 0, 'audio/mpeg')
        fe.pubDate(video.fecha_publicacion.replace(tzinfo=UTC))

    return fg.rss_str(pretty=True)
