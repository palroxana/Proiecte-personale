from Domain.cardclient import CardClient
from dataclasses import dataclass


@dataclass
class CarduriCrescatoare:
    puncte: int
    card: CardClient
