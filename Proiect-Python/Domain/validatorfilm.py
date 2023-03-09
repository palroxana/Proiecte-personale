from Domain.film import Film


class ValidatorFilm:
    def validatorfilm(self, film: Film):
        erori = []
        program = ['da', 'nu']
        if not self.numar(film.pret_bilet_film):
            erori.append("Pretul trebuie sa fie un numar")
        else:
            if float(film.pret_bilet_film) < 0:
                erori.append("Pretul trebuie sa fie pozitiv")
        if not film.an_aparitie_film.isnumeric():
            erori.append("Anul trebuie sa fie format din cifre")
        if film.in_program_film not in program:
            erori.append("Filmul poate sau nu sa fie in program "
                         "cu variantele da/nu")
        if not film.id_entity.isnumeric():
            erori.append("Id-ul trebuie sa contina doar cifre")
        if len(erori) > 0:
            raise KeyError(erori)

    # "numar" verifica
    # daca stringurile contin doar cifre nu si litere pentru floaturi
    def numar(self, pret: str):
        try:
            float(pret)
        except ValueError:
            return False
        return True
