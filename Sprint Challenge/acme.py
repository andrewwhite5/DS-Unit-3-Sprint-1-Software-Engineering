import random


# Product Class
class Product:
    def __init__(self, name, price=10, weight=20,
            flammability=0.5, identifier=random.randint(1000000,9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        worth_ratio = self.price/self.weight
        if worth_ratio < 0.5:
            return 'Not so stealable...'
        if 0.5 <= worth_ratio < 1:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        boom_ratio = self.flammability*self.weight
        if boom_ratio < 10:
            return '...fizzle'
        if 10 <= boom_ratio < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


# Boxing Glove Subclass (Product)
class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10,
            flammability=0.5, identifier=random.randint(1000000,9999999)):
        self.weight = weight
        self.name = name
        super().__init__(price)
        super().__init__(flammability)
        super().__init__(identifier)

    def explode(self):
        return "...it's a glove"

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        if 5 <= self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
