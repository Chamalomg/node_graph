class Champ:
    all_traits = [
        'Boss', 'Cultist', 'Divine', 'Duelist', 'Emperor', 'Fortune', 'Keeper', 'Set4_Adept', 'Set4_Assassin',
        'Set4_Blacksmith', 'Set4_Brawler', 'Set4_Daredevil', 'Set4_Dragonsoul', 'Set4_Elderwood',
        'Set4_Enlightened', 'Set4_Executioner', 'Set4_Exile', 'Set4_Fabled', 'Set4_Mage', 'Set4_Mystic',
        'Set4_Ninja', 'Set4_Slayer', 'Set4_Spirit', 'Set4_Syphoner', 'Set4_Vanguard', 'Sharpshooter',
        'Warlord'
    ]

    traits_color = {key: i / 27 for i, key in enumerate(all_traits)}

    def __init__(self, name, cost, traits):
        self.name = name
        self.cost = cost
        self.traits = traits
        self.color = self.traits_color[traits[0]]

    def __str__(self):
        return '{}'.format(self.name)
