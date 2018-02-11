import dice
import attr


@attr.s
class ancestry(object):
    strength = attr.ib()
    agility = attr.ib()
    intellect = attr.ib()
    will = attr.ib()
    perception = attr.ib()
    defense = attr.ib()
    health = attr.ib()
    healing_rate = attr.ib()
    size = attr.ib()
    speed = attr.ib()
    power = attr.ib()
    damage = attr.ib()
    insanity = attr.ib()
    corruption = attr.ib()
    languages = attr.ib()
    professions = attr.ib()

@attr.s
class human(object):

    strength = attr.ib(default=10)
    agility = attr.ib(default=10)
    intellect = attr.ib(default=10)
    will = attr.ib(default=10)
    perception = self.intellect
    defense = attr.ib()
    health = attr.ib()
    healing_rate = attr.ib()
    size = attr.ib()
    speed = attr.ib()
    power = attr.ib()
    damage = attr.ib()
    insanity = attr.ib()
    corruption = attr.ib()
    languages = attr.ib()
    professions = attr.ib()


def create_human():
    human_background[roll('1d20t')]
    print(human_background)

create_human()
