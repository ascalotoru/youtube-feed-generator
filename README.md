# YouTube Feed Generator

YouTube Feed Generator es una aplicación en Flask que permite generar un feed RSS en formato podcast desde una playlist de YouTube.

## Instalación

1. Clona este repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Configura tu clave API de YouTube creando un archivo `.env` y añadiendo la variable `YOUTUBE_API_KEY`.

## Uso

Para generar un feed RSS, inicia la aplicación y accede a la URL `/rss/<playlist_id>` donde `playlist_id` es el identificador de la playlist de YouTube.
