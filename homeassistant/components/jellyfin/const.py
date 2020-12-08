"""Constants for the jellyfin integration."""

DOMAIN = "jellyfin"

CLIENT_VERSION = "1.0"
USER_APP_NAME = "Home Assistant"
USER_AGENT = "Home-Assistant/%s" % CLIENT_VERSION

DATA_CLIENT = "client"

COLLECTION_TYPE_MOVIES = "movies"
COLLECTION_TYPE_TVSHOWS = "tvshows"
COLLECTION_TYPE_MUSIC = "music"

SUPPORTED_COLLECTION_TYPES = [COLLECTION_TYPE_MOVIES, COLLECTION_TYPE_TVSHOWS]

MAX_STREAMING_BITRATE = "140000000"
