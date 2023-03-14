import actor as Actor

class Hero(Actor):
    def _init_(self, x, y, vital, agi, strength, skill, level, money, weapon, armour, job):
        super().__init__(x, y, vital, agi, strength)
        self.skill = skill
        self. level = level
        self.money = money
        self.weapon = weapon
        self.armour = armour
        self. job = job

    def printState(self):
        print("새로운 "+self.job+"가 태어났습니다.")
        print("착용 중인 아이템은 "+self. weapon + " "+self.armour + " 입니다.")

    def action (self):
        print (self.ski11+"기 손을 사용했습니다. ")
    
    def levelUp(self):
        self.level += 1
        self.vitality += 1 
        self.agility += 1 
        self.strength += 1
