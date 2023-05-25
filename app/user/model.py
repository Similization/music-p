import uuid
from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    id: uuid
    nickname: str

    first_name: str | None
    last_name: str | None
    birth_date: date | None

    phone: str | None
    email: str | None
    city: str | None
