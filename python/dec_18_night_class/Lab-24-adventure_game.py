class Creature:
    def __init__(self, location, health):
        self.location = location
        self.health = health
        self.weapon = Weapon(location, 55)


class Weapon:
    def __init__(self, location, damage):
        self.location = location
        self.damage = damage

    def test(self):
        print('You have a {}% of damage.'.format(self.damage))


class Potion:
    def __init__(self, location, health_restored):
        self.location = location
        self.health_restored = health_restored


chris = Creature('se', 100)
b = Weapon('se', 2)
alex = Potion('se', '35')
b.test()
chris.weapon.test()
chris.weapon = b
chris.weapon.test()

