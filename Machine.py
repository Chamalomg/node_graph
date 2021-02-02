class Machine:
    name = 'toto'
    reseau = 'Monréseau'

    def __init__(self, name=name, reseau=reseau):
        self.name = name
        self.reseau = reseau

    def __str__(self):
        return '{}\n{}'.format(self.name, self.reseau)


