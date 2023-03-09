from datetime import date, time

from Domain.film import Film
from Domain.rezervare import Rezervare
from Repository.repositoryfilm import RepositoryFilm
from Repository.repositoryrezervare import RepositoryRezervare
from utils import clear_file


def testrezervarerepository():
    filename = 'test_rezervare_repository.json'
    filenamee = 'test_film_repository.json'
    clear_file(filenamee)
    clear_file(filename)
    added = Film('1', 'Filmul test', "2021", "123", 'da')
    film_repository = RepositoryFilm(filenamee)
    film_repository.create(added)
    assert film_repository.read(added.id_film) == added
    addedrez = Rezervare("1", "1", "", date(20, 9, 2020), time(19, 30))
    rezervare_repository = RepositoryRezervare(filename)
    rezervare_repository.add(addedrez)
    assert rezervare_repository.read(addedrez.id_rezervare) == addedrez
    updated = Rezervare("1", "1", "", date(20, 10, 2020), time(20, 30))
    rezervare_repository.update(updated)
    assert rezervare_repository.update(addedrez) == updated
    rezervare_repository.delete(addedrez.id_rezervare)
    assert rezervare_repository.read(addedrez.id_rezervare) != updated
    assert not film_repository.read()
