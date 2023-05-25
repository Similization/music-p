from dataclasses import dataclass
from datetime import date

from music.album import Album
from music.group import Group
from music.track import Track


@dataclass
class Artist:
    name: str
    lastname: str

    date_of_birth: date
    date_of_death: date

    group_list: list[Group]
    track_list: list[Track]
    album_list: list[Album]
