from Domain.cardclient import CardClient


class ValidatorCardClient:
    def validatorcardclient(self, cardclient: CardClient):
        erori = []
        if not cardclient.cnp_card_client.isnumeric():
            erori.append("CNP-ul trebuie sa aiba numai cifre")
        if not cardclient.id_entity.isnumeric():
            erori.append("id-ul trebuie sa aiba numai cifre")
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
                        erori.append("Ziua trebuie "
                                     "in aceasta luna "
                                     "sa fie cuprinsa intre 1 si 30")
                if int(luna) in luna31:
                    if int(zi) > 31:
                        erori.append("Ziua trebuie "
                                     "in aceasta luna "
                                     "sa fie cuprinsa intre 1 si 31")
                if int(luna) == 2:
                    if int(an) % 4 == 0:
                        if int(zi) > 29:
                            erori.append("Ziua trebuie "
                                         "in aceasta luna si in acest an "
                                         "sa fie cuprinsa intre 1 si 29")
                    else:
                        if int(zi) > 28:
                            erori.append("Ziua trebuie "
                                         "in aceasta luna si in acest an "
                                         "sa fie cuprinsa intre 1 si 28")
        if len(erori) > 0:
            raise KeyError(erori)
