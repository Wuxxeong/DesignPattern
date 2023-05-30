from builder import MonsterBuilder
from random import randrange


class Director:
    def makeMonster(builder: MonsterBuilder):
        builder.setX(randrange(100))
        builder.setY(randrange(100))

        builder.setVitality(randrange(50, 100))
        builder.setAgility(randrange(50, 100))
        builder.setStrength(randrange(50, 100))

        return builder.build()
