from typing import List
import string
import random

from Domain.film import Film
from Domain.validatorfilm import ValidatorFilm
from Repository.repository import Repository
from Service.servicerezervare import ServiceRezervare
from ViewModel.filmecrescatordupanr_rezervari import FilmeCrescatoare


class ServiceFilm:
    def __init__(self, filmrepository: Repository,
                 filmvalidator: ValidatorFilm,
                 servicerezervare: ServiceRezervare):
        self.filmrepository = filmrepository
        self.filmvalidator = filmvalidator
        self.servicerezervare = servicerezervare

    def add(self, id_film: str, titlu_film: str, an_aparitie_film: str,
            pret_bilet_film: str,
            in_program_film: str) -> None:
        film = Film(id_film, titlu_film, an_aparitie_film, pret_bilet_film,
                    in_program_film)
        try:
            self.filmvalidator.validatorfilm(film)
            self.filmrepository.create(film)
        except KeyError as e:
            print(e)

    def delete(self, id_film: str) -> None:
        try:
            self.filmrepository.delete(id_film)
        except KeyError as e:
            print(e)

    def update(self, id_film: str, titlu_film: str, an_aparitie_film: str,
               pret_bilet_film: str,
               in_program_film: str) -> None:
        film = Film(id_film, titlu_film, an_aparitie_film, pret_bilet_film,
                    in_program_film)
        try:
            self.filmvalidator.validatorfilm(film)
            self.filmrepository.update(film)
        except KeyError as e:
            print(e)

    def get_all(self) -> List[Film]:
        return self.filmrepository.read()

    def get_ordered_by_reservation(self) -> List[FilmeCrescatoare]:
        filme = self.get_all()
        rezervarii = self.servicerezervare.get_all()

        def inner(filmee, rezervari):
            if not filmee:
                return []
            filmul = filmee[0]
            idul = filmul.id_film
            numarul_rezervarilor = 0
            for rezervarea in rezervari:
                if rezervarea.id_film_rezervare == idul:
                    numarul_rezervarilor = numarul_rezervarilor + 1
            return [FilmeCrescatoare(filmul.titlu_film,
                                     numarul_rezervarilor)] + inner(filmee[1:],
                                                                    rezervari)

        listadefilme = inner(filme, rezervarii)
        return sorted(listadefilme, key=lambda x: x.nrrezervare, reverse=False)

    def n_filme(self, nr_filme: int) -> None:
        for i in range(nr_filme):
            lungime = random.randint(1, 10)
            lista = ["da", "nu"]
            while True:
                idul = str(random.randint(1, 100))
                if self.filmrepository.read(idul) is None:
                    break
            titlul_film = ''.join((random.choice(string.ascii_lowercase) for _
                                   in range(lungime)))
            an_aparitie = str(random.randint(1, 2021))
            pret = str(random.randint(10, 70))
            program = random.choice(lista)
            self.add(idul, titlul_film, an_aparitie, pret, program)
