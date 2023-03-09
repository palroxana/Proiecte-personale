from dataclasses import dataclass
from time import time

from Domain.rezervare import Rezervare


@dataclass
class ToateRezervarile:
    ora_de_inceput: time
    ora_de_final: time
    rezervare: Rezervare
