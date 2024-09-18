import os


class Config:
    YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
    AUDIO_DIR = os.getenv('AUDIO_DIR', 'static/audio')
    FEED_TITLE = os.getenv('FEED_TITLE', 'Mi Feed de Podcast')
    FEED_DESCRIPTION = os.getenv(
        'FEED_DESCRIPTION', 'Un feed RSS de mi playlist de YouTube en formato podcast')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///youtube_feed.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
