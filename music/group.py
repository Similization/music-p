from dataclasses import dataclass
from datetime import date

from music.album import Album
from music.artist import Artist
from music.track import Track


@dataclass
class Group:
    title: str

    creation_date: date
    breakup_date: date

    track_list: list[Track]
    album_list: list[Album]
    artist_list: list[Artist]
