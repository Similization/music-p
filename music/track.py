from dataclasses import dataclass

from music.album import Album
from music.volume import Volume


@dataclass
class Track(Volume):
    album_list: list[Album]
