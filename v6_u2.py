class Country:

    def __init__(self, name, pop, lang, area=None):
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__languages = [lang]

    def print_info(self):
        if self.__area is None:
            print(f"I {self.__name} bor det ca. {self.__population} miljoner invånare och landets officiella språk är {", ".join(self.__languages)}")
        else:
            print(f"I {self.__name} bor det ca. {self.__population} miljoner invånare, "
                  f"landets officiella språk är {", ".join(self.__languages)} och arean är {self.__area}")

    def add_language(self, language):
        self.__languages.append(language)


"""def p_info(country):
    country.print_info()"""

se = Country("Sverige", 10.5, "Svenska", 8778876)
no = Country("Norge", 5.5, "Norska")
isl = Country("Island", 0.4, "Isländska", 747998)
den = Country("Danmark", 6.0, "Danska")
den.add_language("och Skånska")
fin = Country("Finland", 5.7, "Finländska")
fin.add_language("Svenska")
fin.add_language("Ryska")
fin.add_language("och Samiska")

se.print_info()
no.print_info()
isl.print_info()
den.print_info()
fin.print_info()

print("-"*40)

#p_info(se)



