from dataclasses import dataclass
from datetime import date

from music.album import Album
from music.group import Group
from music.track import Track


@dataclass
class Artist:
    def __init__(self):
        self.name: str
        self.lastname: str

        self.date_of_birth: date
        self.date_of_death: date

        self.group_list: list[Group]
        self.track_list: list[Track]
        self.album_list: list[Album]

