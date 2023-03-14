from actor import Actor
from hero import Hero
from monster import Monster


class ActorBuilder:
    def __init__(self):
        self.x = None
        self.y = None
        self.vitality = None
        self.agility = None
        self.strength = None

    def setX(self, x):
        if x > 100:
            self.x = 100
        elif x < 0:
            self.x = 0
        else:
            self.x = x
        return self

    def setY(self, y):
        if y > 100:
            self.y = 100
        elif y < 0:
            self.y = 0
        else:
            self.y = y
        return self

    def setVitality(self, vitality):
        self.vitality = vitality
        return self

    def setAgility(self, agility):
        self.agility = agility
        return self

    def setStrength(self, strength):
        self.strength = strength
        return self

    def build(self):
        actor = Actor(self.x, self.y, self.vitality,
                      self.agility, self.strength)
        return actor


class HeroBuilder(ActorBuilder):
    def __init__(self):
        super().__init__()
        self.skill = None
        self.level = None
        self.money = None
        self.weapon = None
        self.armour = None
        self.job = None

    def setSkill(self, skill):
        self.skill = skill
        return self

    def setLevel(self, level):
        self.level = level
        return self

    def setMoney(self, money):
        self.money = money
        return self

    def setWeapon(self, weapon):
        self.weapon = weapon
        return self

    def setArmour(self, armour):
        self.armour = armour
        return self

    def setJob(self, job):
        self.job = job
        return self

    def build(self):
        hero = Hero(self.x, self.y, self.vitality, self.agility, self.strength, self.skill,
                    self.level, self.money, self.weapon, self.armour, self.job)
        return hero


class MonsterBuilder(ActorBuilder):
    def __init__(self):
        super().__init__()
        self.residence = None
        self.color = None
        self.itemDropRate = None

    def setResidence(self, residence):
        self.residence = residence
        return self

    def setColor(self, color):
        self.color = color
        return self

    def setItemDropRate(self, itemDropRate):
        self.itemDropRate = itemDropRate
        return self

    def build(self):
        monster = Monster(self.x, self.y, self.vitality, self.agility, self.strength,
                          self.residence, self.color, self.itemDropRate)
        return monster
