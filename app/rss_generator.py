from feedgen.feed import FeedGenerator


def generar_feed_rss(videos):
    fg = FeedGenerator()
    fg.title('Podcast desde YouTube')
    fg.link(href='https://miweb.com/rss')
    fg.description('Podcast generado dinámicamente a partir de YouTube')

    # Le damos la vuelta a la lista para que el más antiguo salga primero en el feed
    videos.reverse()

    for video in videos:
        fe = fg.add_entry()
        fe.title(video['titulo'])
        fe.link(href=video['url'])
        fe.description(video['descripcion'])
        # Puedes añadir un archivo de audio si decides hacerlo
        fe.enclosure(video['mp3_url'], 0, 'audio/mpeg')
        fe.pubDate(video['fecha_publicacion'])

    return fg.rss_str(pretty=True)
