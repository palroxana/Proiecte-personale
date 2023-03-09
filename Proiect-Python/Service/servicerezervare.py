import datetime
from typing import List

from Domain.rezervare import Rezervare
from Domain.validatorrezervare import ValidatorRezervare
from Repository.repository import Repository
from Service.servicecardclient import ServiceCardClient
from ViewModel.toaterezervariledintreore import ToateRezervarile


class ServiceRezervare:
    def __init__(self, rezervarerepository: Repository,
                 rezervarevalidator: ValidatorRezervare,
                 filmrepository: Repository,
                 cardrepository: Repository, cardservice: ServiceCardClient):
        self.rezervarerepository = rezervarerepository
        self.rezervarevalidator = rezervarevalidator
        self.filmrepository = filmrepository
        self.cardrepository = cardrepository
        self.cardservice = cardservice

    def add(self, id_rezervare: str, id_film_rezervare: str,
            id_card_client_rezervare: str, data, ora):
        data_rezervare = data.split(".")
        if len(data_rezervare) > 3:
            print("Data nu e valida")
        data_zi = data_rezervare[0]
        data_luna = data_rezervare[1]
        data_an = data_rezervare[2]
        ora_rezervare = ora.split(".")
        if len(ora_rezervare) > 2:
            print("Ora nu este valida")
        ora_ora = ora_rezervare[0]
        ora_minute = ora_rezervare[1]
        try:
            self.rezervarevalidator.esteint(data_an, data_luna, data_zi)
            self.rezervarevalidator.validareora(ora_ora, ora_minute)
            data_zi = int(data_zi)
            data_luna = int(data_luna)
            data_an = int(data_an)
            ora_ora = int(ora_ora)
            ora_minute = int(ora_minute)
            data = datetime.date(data_an, data_luna, data_zi)
            ora = datetime.time(ora_ora, ora_minute)
            rezervare = Rezervare(id_rezervare, id_film_rezervare,
                                  id_card_client_rezervare, data, ora)
            try:
                self.rezervarerepository.create(rezervare)
                self.rezervarevalidator.validatorrezervare(rezervare)
                if id_card_client_rezervare != "":
                    cardul = self.cardrepository.read(id_card_client_rezervare)
                    filmul = self.filmrepository.read(id_film_rezervare)
                    punctele = str(int(cardul.puncte_card_client) + int(
                        filmul.pret_bilet_film) // 10)
                    datanasteriistring = \
                        cardul.data_nasterii_card_client.strftime('%d.%m.%Y')
                    datainregistrariistring = \
                        cardul.data_inregistrarii_card_client.strftime(
                            '%d.%m.%Y')
                    self.cardservice.update(cardul.id_card_client,
                                            cardul.nume_card_client,
                                            cardul.prenume_card_client,
                                            cardul.cnp_card_client,
                                            datanasteriistring,
                                            datainregistrariistring, punctele)
                    print("Punctele de pe card sunt:")
                    print(punctele)

            except KeyError as ve:
                print(ve)
        except KeyError as e:
            print(e)

    def delete(self, id_rezervare):
        try:
            self.rezervarerepository.delete(id_rezervare)
        except KeyError as e:
            print(e)

    def update(self, id_rezervare: str, id_film_rezervare: str,
               id_card_client_rezervare: str, data, ora):
        data_rezervare = data.split(".")
        if len(data_rezervare) > 3:
            print("Data nu e valida")
        data_zi = data_rezervare[0]
        data_luna = data_rezervare[1]
        data_an = data_rezervare[2]
        ora_rezervare = ora.split(".")
        if len(ora_rezervare) > 2:
            print("Ora nu este valida")
        ora_ora = ora_rezervare[0]
        ora_minute = ora_rezervare[1]
        try:
            self.rezervarevalidator.esteint(data_an, data_luna, data_zi)
            self.rezervarevalidator.validareora(ora_ora, ora_minute)
            data_luna = int(data_luna)
            data_an = int(data_an)
            ora_ora = int(ora_ora)
            ora_minute = int(ora_minute)
            data = datetime.date(data_an, data_luna, data_zi)
            ora = datetime.time(ora_ora, ora_minute)
            rezervare = Rezervare(id_rezervare, id_film_rezervare,
                                  id_card_client_rezervare, data, ora)
            try:
                self.rezervarerepository.create(rezervare)
                self.rezervarevalidator.validatorrezervare(rezervare)
                if id_card_client_rezervare != "":
                    cardul = self.cardrepository.read(id_card_client_rezervare)
                    filmul = self.filmrepository.read(id_film_rezervare)
                    punctele = str(int(cardul.puncte_card_client) + int(
                        filmul.pret_bilet_film) // 10)
                    datanasteriistring = \
                        cardul.data_nasterii_card_client.strftime('%d.%m.%Y')
                    datainregistrariistring = \
                        cardul.data_inregistrarii_card_client.strftime(
                            '%d.%m.%Y')
                    self.cardservice.update(cardul.id_card_client,
                                            cardul.nume_card_client,
                                            cardul.prenume_card_client,
                                            cardul.cnp_card_client,
                                            datanasteriistring,
                                            datainregistrariistring, punctele)
                    print("Punctele de pe card sunt:")
                    print(punctele)

            except KeyError as ve:
                print(ve)
        except KeyError as e:
            print(e)

    def get_all(self) -> List[Rezervare]:
        return self.rezervarerepository.read()

    def get_all_rezervation(self, ora_inceput: str, ora_final: str) -> \
            List[ToateRezervarile]:
        rezervarii = self.get_all()
        lista_rez = []

        def inner(rezervari: List[Rezervare], lista: list):
            if not rezervari:
                return []
            rezervare = rezervari[0]
            txt = ora_inceput.split(".")
            inceput = datetime.time(int(txt[0]), int(txt[1]))
            txt = ora_final.split(".")
            final = datetime.time(int(txt[0]), int(txt[1]))
            if rezervare.ora >= inceput:
                if rezervare.ora <= final:
                    obiect = ToateRezervarile(ora_inceput,
                                              ora_final, rezervare)
                    return lista + [obiect] + inner(rezervari[1:], lista)
            return lista + inner(rezervari[1:], lista)

        listaderezervari = inner(rezervarii, lista_rez)
        return listaderezervari

    def stergere_rezervari(self, zi_inceput: str, zi_final: str) -> None:
        rezervarii = self.get_all()
        lista = []

        def inner(rezervari: List[Rezervare], lista_rezervari: list):
            if not rezervari:
                return []
            rezervarea = rezervari[0]
            txt = zi_inceput.split(".")
            inceput = datetime.date(int(txt[2]), int(txt[1]), int(txt[0]))
            txt = zi_final.split(".")
            final = datetime.date(int(txt[2]), int(txt[1]), int(txt[0]))
            if rezervarea.data >= inceput:
                if rezervarea.data <= final:
                    obiect = rezervarea
                    return lista_rezervari + [obiect] + inner(rezervari[1:],
                                                              lista_rezervari)
            return lista_rezervari + inner(rezervari[1:], lista_rezervari)

        listaderezervari = inner(rezervarii, lista)
        for rezervare in rezervarii:
            if rezervare in listaderezervari:
                self.delete(rezervare.id_entity)
