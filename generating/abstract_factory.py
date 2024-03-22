class AbstractFactory(object):
    def create_bottle(self):
        raise NotImplementedError()

    def create_water(self):
        raise NotImplementedError()


class Bottle(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Water(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class CocaColaFactory(AbstractFactory):
    def create_bottle(self):
        return Bottle("Coca-cola bottle")

    def create_water(self):
        return Water("Coca-cola water")


class PepsiColaFactory(AbstractFactory):
    def create_bottle(self):
        return Bottle("Pepsi-cola bottle")

    def create_water(self):
        return Water("Pepsi-cola water")


def get_factory(ident):
    if ident == 0:
        return CocaColaFactory()
    elif ident == 1:
        return PepsiColaFactory()


factory = get_factory(1)
print(factory.create_bottle())  # Pepsi
print(factory.create_water())  # Pepsi
