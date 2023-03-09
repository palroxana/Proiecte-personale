from Domain.rezervare import Rezervare
from Repository.repository import Repository


class ValidatorRezervare:
    def __init__(self, filmrepository: Repository, cardrepository: Repository):
        self.filmrepository = filmrepository
        self.cardrepository = cardrepository

    def validatorrezervare(self, rezervare: Rezervare):
        erori = []
        if self.filmrepository.read(rezervare.id_film_rezervare) is None:
            erori.append("Nu exista un film cu id-ul dat")
        if rezervare.id_card_client_rezervare != "":
            if self.cardrepository.read(
                    rezervare.id_card_client_rezervare) is None:
                print("Nu exista un card cu id-ul dat")
        if self.filmrepository.read(
                rezervare.id_film_rezervare).in_program_film == "nu":
            erori.append("Filmul nu este n program")
        if len(erori) > 0:
            raise KeyError(erori)

    def esteint(self, an, luna, zi):
        erori = []
        luna30 = [4, 6, 9, 11]
        luna31 = [1, 3, 5, 7, 8, 10, 12]
        if not an.isnumeric():
            erori.append("Anul trebuie sa aibe cifre si sa fie numar intreg")
        okluna = 0
        if not luna.isnumeric():
            okluna = okluna + 1
            erori.append("Luna trebuie sa aiba cifre si sa fie numar intreg")
        else:
            if int(luna) > 12:
                okluna = okluna + 1
                erori.append("Luna trebuie sa fie cuprinsa intre 1 ai 12")
            if int(luna) < 1:
                okluna = okluna + 1
                erori.append("Luna trebuie sa fie cuprinsa intre 1 ai 12")
        if not zi.isnumeric():
            erori.append("Ziua trebuie sa aiba cifre si a fie numar intreg")
        elif okluna == 0:
            if int(zi) < 1:
                erori.append("Ziua trebuie sa fie mai mare decat 1")
            else:
                if int(luna) in luna30:
                    if int(zi) > 30:
                        erori.append(
                            "Ziua trebuie "
                            "in aceasta luna sa fie cuprinsa intre 1 si 30")
                if int(luna) in luna31:
                    if int(zi) > 31:
                        erori.append(
                            "Ziua trebuie "
                            "in aceasta luna sa fie cuprinsa intre 1 si 31")
                if int(luna) == 2:
                    if int(an) % 4 == 0:
                        if int(zi) > 29:
                            erori.append(
                                "Ziua trebuie "
                                "in aceasta luna si in acest an "
                                "sa fie cuprinsa intre 1 si 29")
                    else:
                        if int(zi) > 28:
                            erori.append(
                                "Ziua trebuie in aceasta "
                                "luna si in acest an "
                                "sa fie cuprinsa intre 1 si 28")
        if len(erori) > 0:
            raise KeyError(erori)

    def validareora(self, ora, minute):
        erori = []
        if not ora.isnumeric():
            erori.append("Ora trebuie sa aiba cifre")
        else:
            if int(ora) > 23:
                erori.append("Ora trebuie sa fie cuprinsa intre 0 si 23")
            if int(ora) < 0:
                erori.append("Ora trebuie sa fie cuprinsa intre 0 si 23")
        if not minute.isnumeric():
            erori.append("Minutele trebuie sa aiba cifre")
        else:
            if int(minute) > 59:
                erori.append("Minutele sunt de la 0 la 59")
            if int(minute) < 0:
                erori.append("Minutele sunt de la 0 la 59")
        if len(erori) > 0:
            raise KeyError(erori)
