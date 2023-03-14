import actor as Actor

class Monster (Actor):
  def _init_(self, x, y, vital, agi, strength, residence, color, itemDropRate):
    super().__init__(x, y, vital, agi, strength)
    self.residence = residence
    self.color = color
    self.itemDropRate = itemDropRate
  def printState(self):
    print (self.residence+"지역에서 몬스터 출용")