from Domain.validatorcardclient import ValidatorCardClient
from Domain.validatorfilm import ValidatorFilm
from Domain.validatorrezervare import ValidatorRezervare
from Service.servicecardclient import ServiceCardClient
from Service.servicefilm import ServiceFilm
from Service.servicerezervare import ServiceRezervare


def showall(objects):
    try:
        for obj in objects:
            print(obj)
    except KeyError as ke:
        print('Eroare de ID: ', ke)
    except ValueError as ve:
        print('Eroare valorica: ', ve)
    except Exception as ee:
        print('Eroare: ', ee)


def meniurezervare():
    print("1.Adauga rezervare")
    print("2.Sterge rezervare")
    print("3.Modifica rezervare")
    print("a.Afisare")
    print("x.Iesire")


def meniucard():
    print("1.Adauga card")
    print("2.Sterge card")
    print("3.Modifica card")
    print("a.Afisare")
    print("x.Iesire")


def meniufilm():
    print("1.Adauga film")
    print("2.Sterge film")
    print("3.Modifica film")
    print("a.Afisare")
    print("x.Iesire")


def meniu():
    print("1.crud film")
    print("2.crud card client")
    print("3.crud rezervare")
    print("4.ordonare filme crescator dupa nr de rezervari")
    print("5.afisarea tuturor rezervarilor dintr-un interval de ore dat")
    print("6.afisarea cardurilor client ordonate descrescator dupa puncte")
    print("7.stergere rezervari")
    print("8.adaugare puncte")
    print("9.")
    print("10.lab 1: n filme generate random")
    print("x.Iesire")


class Consola:
    def __init__(self, filmservice: ServiceFilm, filmvalidator: ValidatorFilm,
                 cardservice: ServiceCardClient,
                 cardvalidator: ValidatorCardClient,
                 rezervareservice: ServiceRezervare,
                 rezervarevalidator: ValidatorRezervare):
        self.filmservice = filmservice
        self.filmvalidator = filmvalidator
        self.cardservice = cardservice
        self.cardvalidator = cardvalidator
        self.rezervareservice = rezervareservice
        self.rezervarevalidator = rezervarevalidator

    def runmeniu(self):
        while True:
            meniu()
            op = input("Dati optiunea: ")
            if op == "1":
                self.crudfilm()
            elif op == "2":
                self.crudcard()
            elif op == "3":
                self.crudrezervare()
            elif op == "4":
                showall(self.filmservice.get_ordered_by_reservation())
            elif op == "5":
                self.rezervariore()
            elif op == "6":
                showall(self.cardservice.cardcrescator())
            elif op == "7":
                self.stergererezervari()
            elif op == "8":
                self.adaugarepuncte()
            elif op == "10":
                self.n_elemente()
            elif op == "x":
                break
            else:
                print("Optiune invalida")

    def crudfilm(self):
        while True:
            meniufilm()
            op = input("Dati op")
            if op == "1":
                try:
                    id_film = input("Dati id-ul")
                    titlu_film = input("Dati titlu")
                    an_aparitie = input("Dati anul aparitiei")
                    pret_bilet = input("Dati pretul biletului")
                    inprogram_film = input("Este filmul in program?(da/nu)")
                    self.filmservice.add(id_film, titlu_film, an_aparitie,
                                         pret_bilet, inprogram_film)
                except KeyError as ke:
                    print('Eroare de ID: ', ke)
                except ValueError as ve:
                    print('Eroare valorica: ', ve)
                except Exception as ee:
                    print('Eroare: ', ee)
            elif op == "2":
                try:
                    id_film = input("Dati id-ul filmului sters")
                    self.filmservice.delete(id_film)
                except KeyError as ke:
                    print('Eroare de ID: ', ke)
                except ValueError as ve:
                    print('Eroare valorica: ', ve)
                except Exception as ee:
                    print('Eroare: ', ee)
            elif op == "3":
                try:
                    id_film = input("Dati id-ul")
                    titlu_film = input("Dati titlu film")
                    an_aparitie = input("Dati anul aparitiei")
                    pret_bilet = input("Dati pretul biletului")
                    inprogram_film = input("Este filmul in program?(da/nu)")
                    self.filmservice.update(id_film, titlu_film, an_aparitie,
                                            pret_bilet, inprogram_film)
                except KeyError as ke:
                    print('Eroare de ID: ', ke)
                except ValueError as ve:
                    print('Eroare valorica: ', ve)
                except Exception as ee:
                    print('Eroare: ', ee)
            elif op == "a":
                try:
                    showall(self.filmservice.get_all())
                except KeyError as ke:
                    print('Eroare de ID: ', ke)
                except ValueError as ve:
                    print('Eroare valorica: ', ve)
                except Exception as ee:
                    print('Eroare: ', ee)
            elif op == "x":
                break
            else:
                print("Optiune invalida")

    def crudcard(self):
        while True:
            meniucard()
            op = input("Dati op")
            if op == "1":
                try:
                    id_card = input("Dati id-ul cardului")
                    nume_card = input("Dati numele clientului")
                    prenume_card = input("Dati prenumele clientului")
                    cnp_card = input("Dati cnp-ul clientului")
                    datanasterii_card = input(
                        "Dati data nasterii clientului "
                        "despartita prin '.'(dd.mm.yyyy):")
                    datainregistrarii_card = input(
                        "Dati data inregistrarii cardului "
                        "despartita prin '.'(dd.mm.yyyy):")
                    punctecard_client = "0"
                    self.cardservice.add(id_card, nume_card, prenume_card,
                                         cnp_card, datanasterii_card,
                                         datainregistrarii_card,
                                         punctecard_client)

                except KeyError as ke:
                    print('Eroare de ID: ', ke)
                except ValueError as ve:
                    print('Eroare valorica: ', ve)
                except Exception as ee:
                    print('Eroare: ', ee)
            elif op == "2":
                try:
                    id_card = input("Dati id-ul cardului sters")
                    self.cardservice.delete(id_card)
                except KeyError as ke:
                    print('Eroare de ID: ', ke)
                except ValueError as ve:
                    print('Eroare valorica: ', ve)
                except Exception as ee:
                    print('Eroare: ', ee)
            elif op == "3":
                try:
                    id_card = input("Dati id-ul cardului")
                    nume_card = input("Dati numele clientului")
                    prenume_card = input("Dati prenumele clientului")
                    cnp_card = input("Dati cnp-ul clientului")
                    datanasterii_card = input(
                        "Dati data nasterii clientului "
                        "despartita prin '.'(dd.mm.yyyy):")
                    datainregistrarii_card = input(
                        "Dati data inregistrarii cardului "
                        "despartita prin '.'(dd.mm.yyyy):")
                    punctecard_client = "0"
                    self.cardservice.update(id_card, nume_card, prenume_card,
                                            cnp_card, datanasterii_card,
                                            datainregistrarii_card,
                                            punctecard_client)
                except KeyError as ke:
                    print('Eroare de ID: ', ke)
                except ValueError as ve:
                    print('Eroare valorica: ', ve)
                except Exception as ee:
                    print('Eroare: ', ee)
            elif op == "a":
                try:
                    showall(self.cardservice.get_all())
                except KeyError as ke:
                    print('Eroare de ID: ', ke)
                except ValueError as ve:
                    print('Eroare valorica: ', ve)
                except Exception as ee:
                    print('Eroare: ', ee)
            elif op == "x":
                break
            else:
                print("Optiune invalida")

    def crudrezervare(self):
        while True:
            meniurezervare()
            op = input("Dati op")
            if op == "1":
                try:
                    id_rezervare = input("Dati id-ul pt rezervare")
                    id_film_rezervare = input(
                        "Dati id-ul filmului pt rezervare")
                    id_card_client = input("Dati id-ul cardului clientului")
                    data = input("Dati data despartita prin'.'(dd.mm.yyyy)")
                    ora = input("Dati ora despartite prin '.'(hh.mm)")
                    self.rezervareservice.add(id_rezervare, id_film_rezervare,
                                              id_card_client, data, ora)
                except KeyError as ke:
                    print('Eroare de ID: ', ke)
                except ValueError as ve:
                    print('Eroare valorica: ', ve)
                except Exception as ee:
                    print('Eroare: ', ee)
            elif op == "2":
                try:
                    id_rezervare = input("Dati id-ul filmului sters")
                    self.rezervareservice.delete(id_rezervare)
                except KeyError as ke:
                    print('Eroare de ID: ', ke)
                except ValueError as ve:
                    print('Eroare valorica: ', ve)
                except Exception as ee:
                    print('Eroare: ', ee)
            elif op == "3":
                try:
                    id_rezervare = input("Dati id-ul pt rezervare")
                    id_film_rezervare = input(
                        "Dati id-ul filmului pt rezervare")
                    id_card_client = input("Dati id-ul cardului clientului")
                    data = input("Dati data despartita prin'.'(dd.mm.yyyy)")
                    ora = input("Dati ora despartite prin '.'(hh.mm)")
                    self.rezervareservice.update(id_rezervare,
                                                 id_film_rezervare,
                                                 id_card_client, data, ora)
                except KeyError as ke:
                    print('Eroare de ID: ', ke)
                except ValueError as ve:
                    print('Eroare valorica: ', ve)
                except Exception as ee:
                    print('Eroare: ', ee)
            elif op == "a":
                try:
                    showall(self.rezervareservice.get_all())
                except KeyError as ke:
                    print('Eroare de ID: ', ke)
                except ValueError as ve:
                    print('Eroare valorica: ', ve)
                except Exception as ee:
                    print('Eroare: ', ee)
            elif op == "x":
                break
            else:
                print("Optiune invalida")

    def rezervariore(self):
        try:
            ora_inceput = input("Dati ora de inceput despartita prin '.': ")
            ora_final = input("Dati ora de final despartita prin '.': ")
            showall(self.rezervareservice.get_all_rezervation(ora_inceput,
                                                              ora_final))
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except ValueError as ve:
            print('Eroare valorica: ', ve)
        except Exception as ee:
            print('Eroare: ', ee)

    def stergererezervari(self):
        try:
            zi_inceput = input("Dati data de inceput despartita prin '.': ")
            zi_final = input("Dati data de final despartita prin '.': ")
            self.rezervareservice.stergere_rezervari(zi_inceput, zi_final)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except ValueError as ve:
            print('Eroare valorica: ', ve)
        except Exception as ee:
            print('Eroare: ', ee)

    def adaugarepuncte(self):
        try:
            zi_inceput = input("Dati data de inceput despartita prin '.': ")
            zi_final = input("Dati data de final despartita prin '.': ")
            puncte = int(input("Dati punctele pe care le adaugati"))
            self.cardservice.adaugare_puncte(puncte, zi_inceput, zi_final)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except ValueError as ve:
            print('Eroare valorica: ', ve)
        except Exception as ee:
            print('Eroare: ', ee)

    def n_elemente(self):
        try:
            n = int(input("Cate elemente trebuie adaugate:"))
            self.filmservice.n_filme(n)
        except KeyError as ke:
            print('Eroare de ID: ', ke)
        except ValueError as ve:
            print('Eroare valorica: ', ve)
        except Exception as ee:
            print('Eroare: ', ee)
