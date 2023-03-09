from datetime import date

from Domain.cardclient import CardClient
from Repository.repositorycardclient import RepositoryCardClient
from utils import clear_file


def testcardrepository():
    filename = 'test_card_repository'
    clear_file(filename)
    zi = 20
    luna = 9
    an = 2020
    data_nastere = date(zi, luna, an)
    added = CardClient("1", "ana", "andra", "30", data_nastere, date(21, 9, 2020), "0")
    card_repository = RepositoryCardClient(filename)
    card_repository.create(added)
    assert card_repository.read(added.id_card_client) == added
    card_repository.delete(added.id_card_client)
    assert not card_repository.read(added.id_card_client) != added
    assert not card_repository.read()
    card_repository.create(added)
    updated = CardClient("1", "popa", "andrei", "20", date(20, 9, 2020), date(21, 9, 2020), "20")
    card_repository.update(updated)
    assert card_repository.read(added.id_card_client) == updated
