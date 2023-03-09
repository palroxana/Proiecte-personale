from Domain.film import Film
from Repository.repositoryfilm import RepositoryFilm
from utils import clear_file


def testfilmrepository():
    filename = 'test_film_repository.json'
    clear_file(filename)
    added = Film('1', 'Film', '2021', '12', 'da')
    film_repository = RepositoryFilm(filename)
    film_repository.create(added)
    assert film_repository.read(added.id_film) == added
    film_repository.delete(added.id_film)
    assert film_repository.read(added.id_film) != added
    assert not film_repository.read()
    film_repository.create(added)
    updated = Film('1', 'Filmul', '2020', '124.12', 'nu')
    film_repository.update(updated)
    assert film_repository.read(added.id_film) == updated
    assert film_repository.read(added.id_film) != added
