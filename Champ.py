class Champ:

    def __init__(self, name, cost, traits):
        self.name = name
        self.cost = cost
        self.traits = traits

    def __str__(self):
        return '{}'.format(self.name)


