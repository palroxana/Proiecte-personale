from Domain.validatorcardclient import ValidatorCardClient
from Domain.validatorfilm import ValidatorFilm
from Domain.validatorrezervare import ValidatorRezervare
from Repository.json_repository import JsonRepository

from Service.servicecardclient import ServiceCardClient
from Service.servicefilm import ServiceFilm
from Service.servicerezervare import ServiceRezervare
from UI.consola import Consola


def main():
    filmrepository = JsonRepository('film.json')
    filmvalidator = ValidatorFilm()
    cardrepository = JsonRepository('card.json')
    cardvalidator = ValidatorCardClient()
    cardservice = ServiceCardClient(cardrepository, cardvalidator)
    rezervarerepository = JsonRepository('rezervare.json')
    rezervarevalidator = ValidatorRezervare(filmrepository, cardrepository)
    rezervareservice = ServiceRezervare(rezervarerepository,
                                        rezervarevalidator,
                                        filmrepository,
                                        cardrepository,
                                        cardservice)
    filmservice = ServiceFilm(filmrepository, filmvalidator, rezervareservice)
    console = Consola(filmservice,
                      filmvalidator,
                      cardservice,
                      cardvalidator,
                      rezervareservice,
                      rezervarevalidator)
    console.runmeniu()


if __name__ == '__main__':
    main()
