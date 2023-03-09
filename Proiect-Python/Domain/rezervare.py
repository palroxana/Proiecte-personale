from dataclasses import dataclass
import datetime

from Domain.entity import Entity


@dataclass
class Rezervare(Entity):
    id_film_rezervare: str
    id_card_client_rezervare: str
    data: datetime.date
    ora: datetime.time
