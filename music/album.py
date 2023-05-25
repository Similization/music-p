from dataclasses import dataclass

from music.track import Track
from music.volume import Volume


@dataclass
class Album(Volume):
    track_list: list[Track]
