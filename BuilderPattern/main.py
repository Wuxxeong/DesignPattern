from builder import HeroBuilder
from builder import MonsterBuilder
from director import Director

hero = HeroBuilder().setX(10).setY(20).setVitality(50).setAgility(60).setStrength(30)\
                    .setSkill("점프").setLevel(1).setMoney(1000).setWeapon("권총")\
                    .setArmour("갑옷").setJob("전사").build()

builderMonster = MonsterBuilder()
Director.makeMonster(builderMonster)
monster = builderMonster.setResidence("대구").setColor(
    "BlackPink").setItemDropRate(10).build()

monster.printState()
hero.printState()
hero.action()
hero.levelUp()
