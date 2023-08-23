# Business logic core like RUT validator, cession calculator and other.
from itertools import cycle


class AppNameDomain:

    @staticmethod
    def parse_rut(rut: str) -> str:
        """ Parse rut to format 12345678-9 """
        if "-" in rut:
            return rut

        reversed_digits = map(int, reversed(str(rut)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        dv = (-s) % 11
        return f"{rut}-{dv}"
