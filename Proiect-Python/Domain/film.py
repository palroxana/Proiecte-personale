from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Film(Entity):
    titlu_film: str
    an_aparitie_film: str
    pret_bilet_film: str
    in_program_film: str
