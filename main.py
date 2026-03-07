""""
class SafeStorage:
    __data = None
    def get(self):
        return self.__data
    def put(self, data):
        self.__data = data

safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()
safe.put("Boaorm")
y = safe.get()
print(x, y)"""

class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Rooster(Animal):
    def make_noise(self):
        print("UhhhhhUhhUhhUuuuuuuuuhh!")

class Dog(Animal):
    def make_noise(self):
        print("Voff!")

class Cat(Animal):
    def make_noise(self):
        super().make_noise()
        #print("Mjau!")

class Parrot(Animal):
    def make_noise(self):
        print("Aaaäääou!")

def sound_off(animal):
    animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()
p = Parrot()
sound_off(c)

