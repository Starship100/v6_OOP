class Country:
    def __init__(self, name, pop):
        self._name = name
        self.population = pop

    def print_info(self):
        print(f"I  {self._name} bor det {self.population} miljoner invånare")


se = Country("Sverige", 10.5)
no = Country("Norge", 5.5)
isl = Country("Island", 0.4)
den = Country("Danmark", 6.0)

se.print_info()
no.print_info()
isl.print_info()
den.print_info()





