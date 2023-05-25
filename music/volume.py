from dataclasses import dataclass
from datetime import date

from music.artist import Artist
from music.group import Group


@dataclass
class Volume:
    title: str

    creation_date: date
    deletion_date: date

    author_list: list[Artist | Group] | None
