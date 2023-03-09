import datetime
from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class CardClient(Entity):
    nume_card_client: str
    prenume_card_client: str
    cnp_card_client: str
    data_nasterii_card_client: datetime.date
    data_inregistrarii_card_client: datetime.date
    puncte_card_client: str
