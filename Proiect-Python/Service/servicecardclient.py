import datetime
from typing import List

from Domain.cardclient import CardClient
from Domain.validatorcardclient import ValidatorCardClient
from Repository.repository import Repository
from ViewModel.carduricrescatoaredupapct import CarduriCrescatoare


class ServiceCardClient:
    def __init__(self, cardclientrepository: Repository,
                 cardclientvalidator: ValidatorCardClient):
        self.cardclientrepository = cardclientrepository
        self.cardclientvalidator = cardclientvalidator

    def add(self, idcard: str, numecard: str, prenumecard: str, cnpcard: str,
            datanasterii_card: str,
            datainregistrarii_card: str, punctecard: str) -> None:
        datanasterii = datanasterii_card.split(".")
        if len(datanasterii) > 3:
            print("Data nu este valida")
        datainregistrarii = datainregistrarii_card.split(".")
        if len(datainregistrarii) > 3:
            print("Data nu este valida")
        datanasterii_zi = datanasterii[0]
        datanasterii_luna = datanasterii[1]
        datanasterii_an = datanasterii[2]
        datainregistrarii_zi = datainregistrarii[0]
        datainregistrarii_luna = datainregistrarii[1]
        datainregistrarii_an = datainregistrarii[2]
        try:
            self.cardclientvalidator.esteint(datanasterii_an,
                                             datanasterii_luna,
                                             datanasterii_zi)
            self.cardclientvalidator.esteint(datainregistrarii_an,
                                             datainregistrarii_luna,
                                             datainregistrarii_zi)
            datanasterii_an = int(datanasterii_an)
            datanasterii_luna = int(datanasterii_luna)
            datanasterii_zi = int(datanasterii_zi)
            datainregistrarii_an = int(datainregistrarii_an)
            datainregistrarii_luna = int(datainregistrarii_luna)
            datainregistrarii_zi = int(datainregistrarii_zi)
            datanasteriicard = datetime.date(datanasterii_an,
                                             datanasterii_luna,
                                             datanasterii_zi)
            datainregistrariicard = datetime.date(datainregistrarii_an,
                                                  datainregistrarii_luna,
                                                  datainregistrarii_zi)
            cardclient = CardClient(idcard, numecard, prenumecard, cnpcard,
                                    datanasteriicard, datainregistrariicard,
                                    punctecard)
            try:
                self.cardclientvalidator.validatorcardclient(cardclient)
                self.cardclientrepository.create(cardclient)
            except KeyError as e:
                print(e)
        except KeyError as er:
            print(er)

    def delete(self, idcard: str) -> None:
        try:
            self.cardclientrepository.delete(idcard)
        except KeyError as e:
            print(e)

    def update(self, idcard: str, numecard: str, prenumecard: str,
               cnpcard: str, datanasterii_card: str,
               datainregistrarii_card: str, punctecard: str) -> None:
        datanasterii = datanasterii_card.split(".")
        if len(datanasterii) > 3:
            print("Data nu este valida")
        datainregistrarii = datainregistrarii_card.split(".")
        if len(datainregistrarii) > 3:
            print("Data nu este valida")
        datanasterii_zi = datanasterii[0]
        datanasterii_luna = datanasterii[1]
        datanasterii_an = datanasterii[2]
        datainregistrarii_zi = datainregistrarii[0]
        datainregistrarii_luna = datainregistrarii[1]
        datainregistrarii_an = datainregistrarii[2]
        try:
            self.cardclientvalidator.esteint(datanasterii_an,
                                             datanasterii_luna,
                                             datanasterii_zi)
            self.cardclientvalidator.esteint(datainregistrarii_an,
                                             datainregistrarii_luna,
                                             datainregistrarii_zi)
            datanasterii_an = int(datanasterii_an)
            datanasterii_luna = int(datanasterii_luna)
            datanasterii_zi = int(datanasterii_zi)
            datainregistrarii_an = int(datainregistrarii_an)
            datainregistrarii_luna = int(datainregistrarii_luna)
            datainregistrarii_zi = int(datainregistrarii_zi)
            datanasteriicard = datetime.date(datanasterii_an,
                                             datanasterii_luna,
                                             datanasterii_zi)
            datainregistrariicard = datetime.date(datainregistrarii_an,
                                                  datainregistrarii_luna,
                                                  datainregistrarii_zi)
            cardclient = CardClient(idcard, numecard, prenumecard, cnpcard,
                                    datanasteriicard, datainregistrariicard,
                                    punctecard)
            try:
                self.cardclientvalidator.validatorcardclient(cardclient)
                self.cardclientrepository.update(cardclient)
            except KeyError as e:
                print(e)
        except KeyError as er:
            print(er)

    def get_all(self) -> List[CardClient]:
        return self.cardclientrepository.read()

    def cardcrescator(self) -> List[CarduriCrescatoare]:
        cardurii = self.get_all()

        def inner(carduri):
            if not carduri:
                return []
            card = carduri[0]
            puncte = card.puncte_card_client
            return [CarduriCrescatoare(puncte, card)] + inner(carduri[1:])

        listadecarduri = inner(cardurii)
        return sorted(listadecarduri, key=lambda x: x.puncte, reverse=True)

    def adaugare_puncte(self, puncte: int, zi_inceput, zi_final) -> None:
        cardurii = self.get_all()
        lista = []

        def inner(carduri: List[CardClient], lista_rezervari: list):
            if not carduri:
                return []
            cardul = carduri[0]
            txt = zi_inceput.split(".")
            inceput = datetime.date(int(txt[2]), int(txt[1]), int(txt[0]))
            txt = zi_final.split(".")
            final = datetime.date(int(txt[2]), int(txt[1]), int(txt[0]))
            if cardul.data_nasterii_card_client >= inceput:
                if cardul.data_nasterii_card_client <= final:
                    obiect = cardul
                    return lista_rezervari + [obiect] + inner(carduri[1:],
                                                              lista_rezervari)
            return lista_rezervari + inner(carduri[1:], lista_rezervari)

        listadecarduri = inner(cardurii, lista)
        for card in cardurii:
            if card in listadecarduri:
                nastere = card.data_nasterii_card_client.strftime("%d.%m.%Y")
                inregistrare = card.data_inregistrarii_card_client.strftime(
                    "%d.%m.%Y")
                punctelefinale = str(int(card.puncte_card_client) + puncte)
                self.update(card.id_entity, card.nume_card_client,
                            card.prenume_card_client,
                            card.cnp_card_client, nastere,
                            inregistrare, punctelefinale)
