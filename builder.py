import actor as Actor
class ActorBuilder:
    def __init__(self):
        self.x = None
        self.y =None
        self.vitality = None
        self.agility = None
        self. strength = None

    def setX(self, x):
        if x > 100 : 
          self. x = 100
        elif x < 0:
          self. x = 0
        return self
    
    def setY(self, y):
        if y > 100 : 
          self. y = 100
        elif y < 0:
          self. y = 0
        return self

    def setVitality(self, vitality):
      self.vitality = vitality
      return self

    def setAgility(self, agility):
      self.agility = agility
      return self

    def setStrengh(self, strength):
      self.strength = strength
      return self

    def Build(self):
      actor = Actor(self.x, self.y, self.vitality, self.agility, self.strength)
      return actor
