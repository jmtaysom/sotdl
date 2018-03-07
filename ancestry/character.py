import random
from sys import maxsize
from bisect import bisect

from dice import roll

from ancestry.interesting_things import roll_interesting_thing


def get_seed():
    return random.randrange(maxsize)


common_professions = {
    1: 'Animal trainer',
    2: 'Apothecary or healer',
    3: 'Artisan. Choose a manufacturing trade. Examples include baker, blacksmith, bookbinder, brewer, carpenter, '
       'chandler, cobbler, dyer, glassblower, jeweler, leatherworker, mason, potter, printer, and tailor.',
    4: 'Artist. Choose a medium. Examples include painter, poet, sculptor, and writer. If you choose poet or writer, '
       'you can read and write one language you know.',
    5: 'Boatman or ferryman',
    6: 'Butcher',
    7: 'Cook',
    8: 'Drover or herder',
    9: 'Entertainer. Choose a style. Examples include actor, athlete, comedian, courtesan, dancer, orator, puppeteer, '
       'singer, and storyteller.',
    10: 'Farmer',
    11: 'Fisher or whaler',
    12: 'Groom',
    13: 'Laborer. Choose a labor. Examples include chimneysweep, gravedigger, porter, stevedore, and street-sweeper.',
    14: 'Merchant. Choose a good. Options include arms, grains, livestock, slaves, spices, and textiles.',
    15: 'Miner',
    16: 'Musician. Choose an instrument. Examples include percussion, string, and wind.',
    17: 'Sailor',
    18: 'Servant or valet',
    19: 'Shopkeeper',
    20: 'Teamster'
}


def roll_commmon_profession(dice_roll):
    return f'You are a {common_professions[dice_roll]}'


academic_professions = {
    1: 'Architecture',
    2: 'Astrology',
    3: 'Engineering',
    4: 'Etiquette & customs',
    5: 'Folklore',
    6: 'Geography',
    7: 'Heraldry',
    8: 'History',
    9: 'Law',
    10: 'Literature',
    11: 'Magic',
    12: 'Medicine',
    13: 'Navigation',
    14: 'Occult',
    15: 'Philosophy',
    16: 'Politics',
    17: 'Nature',
    18: 'Religion',
    19: 'Science',
    20: 'War'
}


def roll_academic_profession(dice_roll):
    return f'You are an academic of {academic_professions[dice_roll]}'


criminal_professions = {
    1: 'Agitator',
    2: 'Beggar',
    3: 'Burglar',
    4: 'Carouser or rake',
    5: 'Charlatan or confidence artist',
    6: 'Cultist',
    7: 'Fence',
    8: 'Forger',
    9: 'Gambler',
    10: 'Grave robber',
    11: 'Informant',
    12: 'Murderer',
    13: 'Pickpocket',
    14: 'Pirate',
    15: 'Prostitute',
    16: 'Rebel or terrorist',
    17: 'Saboteur',
    18: 'Spy',
    19: 'Thug',
    20: 'Urchin'
}


def roll_criminal_profession(dice_roll):
    return f'You are a {criminal_professions[dice_roll]}'


martial_profession_breakpoints = [2, 3, 5, 6, 7, 8, 9, 11, 13, 16, 17, 19, 20]
martial_professions = [
    'Constable',
    'Detective',
    'Guard',
    'Jailer',
    'Officer',
    'Marine',
    'Mercenary',
    'Militia member',
    'Patroller',
    'Peasant conscript',
    'Slave',
    'Soldier',
    'Squire',
    'Torturer',
]


def roll_martial_profession(dice_roll):
    return f'You are a {martial_professions[bisect(martial_profession_breakpoints, dice_roll)]}'


wilderness_profession_breakpoints = [2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20]
wilderness_professions = [
    'Bandit, brigand, or highway robber',
    'Barbarian',
    'Exile',
    'Gatherer',
    'Guide',
    'Hermit',
    'Hunter',
    'Nomad or vagabond',
    'Pioneer',
    'Poacher or rustler',
    'Prospector',
    'Outlaw',
    'Refugee',
    'Spelunker',
    'Tracker',
    'Trapper',
    'Woodcutter',
]


def roll_wilderness_profession(dice_roll):
    return f'You are a {wilderness_professions[bisect(wilderness_profession_breakpoints, dice_roll)]}'


religious_profession_breakpoints = [3, 5, 6, 7, 9, 11, 13, 14, 17, 19]
religious_professions = [
    'Devotee. You are a strong believer and follower of your faith’s tenets. You can read and write one language you '
    'know.',
    'Evangelist. You travel from place to place, preaching your faith to any who will listen and rely on the charity '
    'of believers. You can read and write one language you know.',
    'Fanatic. You cloak yourself in deprivation to bring you closer to your gods. You might scourge yourself, deprive '
    'yourself of food and drink, or find other, creative ways to make yourself suffer.',
    'Heretic. You hold religious beliefs deemed dangerous and heretical by the leaders of your faith.',
    'Initiate of the Old Faith. You have been initiated into the Old Faith.',
    'Minister. You are a religious leader in your community. You know how to read and write one language you know.',
    'Acolyte of the New God. You study to become a priest in the Cult of the New God. You know how to read and write '
    'one language you know.',
    'Inquisitor’s Henchman. You serve an inquisitor or witch hunter.',
    'Pilgrim. You travel to sites deemed holy to members of your religion.',
    'Street Preacher. You preach on street corners, beseeching people to seek redemption as the end is near.',
    'Temple Ward. You were raised in a temple. You were likely an orphan and brought up by the clergy.'
]


def roll_religious_profession(dice_roll):
    return f'You are a {religious_professions[bisect(religious_profession_breakpoints, dice_roll)]}'


def roll_profession(dice_roll_1, dice_roll_2):
    return {
        1: roll_commmon_profession(dice_roll_2),
        2: roll_academic_profession(dice_roll_2),
        3: roll_criminal_profession(dice_roll_2),
        4: roll_martial_profession(dice_roll_2),
        5: roll_wilderness_profession(dice_roll_2),
        6: roll_religious_profession(dice_roll_2)
    }.get(dice_roll_1)


wealth_breakpoints = [5, 9, 14, 17, 18]
wealth = [
    'Destitute. You are penniless and live on the streets.',
    'Poor. You live in squalid conditions and you’re never sure where you’re going to get your next meal.',
    'Getting By. You earn enough to meet all your expenses.',
    'Comfortable. You live well and make enough that you can save a little.',
    'Wealthy. You live very well. You have nice clothes and fine accommodations, and you have probably not gone without'
    ' for a long time.',
    'Rich. You want for nothing. You likely come from a noble family, and you have servants and an estate, castle, or '
    'house in the best part of town. Your fortunes earn you many friends and many enemies.'
]


def roll_wealth(dice_roll):
    return wealth[bisect(wealth_breakpoints, dice_roll)]


class Character:
    def __init__(self):
        self.professions = [roll_profession(roll('1d6t'), roll('1d20t')), roll_profession(roll('1d6t'), roll('1d20t'))]
        self.intersting_thing = roll_interesting_thing(roll('1d6t'), roll('1d20t'))
        self.wealth = roll_wealth(roll('3d6t'))

    def __repr__(self):
        return f'{self.professions[0]}\n{self.professions[1]}\n{self.intersting_thing}\n{self.wealth}'


if __name__ == '__main__':
    npc = Character()
    print(npc)
