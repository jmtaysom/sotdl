from bisect import bisect
from random import seed
from dice import roll

try:
    from .character import Character
except ModuleNotFoundError:
    from character import Character


def orc_children():
    born = roll('3d6t')
    died = roll('3d6t')
    if died > born:
        living = 0
    else:
        living = born - died
    return (born, living)


orc_background = {
    1: ("You butchered helpless people. Gain 2 Corruption.", "(None, None)"),
    2: ("You were briefly possessed by a demon. Gain 1 Corruption.", "(None,  None)"),
    3: ("You spent {} years in the fighting pit, testing your skills against other orcs for the amusement of the "
        "crowds.", "(roll('1d6t'), None)"),
    4: ("You stayed loyal to the Empire and fought against other orcs. You were branded as a traitor and cast out.",
        "(None,  None)"),
    5: ("You caught the rot and lost your nose and ears.", "(None,  None)"),
    6: ("You were chained to the oars in a slave ship for {} years.", "(roll('1d6t'), None)"),
    7: ("You were made a eunuch and stood guard over the emperor’s concubines.", "(None,  None)"),
    8: ("You have scar tissue over half your body from when you were caught in the blast of a spell.", "(None,  None)"),
    9: ("You escaped your slavery and have lived in the wilderness ever since.", "(None,  None)"),
    10: ("You earned a living working in your profession.", "(None,  None)"),
    11: ("You fell in love with a human and were spurned for your affections.", "(None,  None)"),
    12: ("You sired or gave birth to {} children. {} are still alive.", "orc_children()"),
    13: ("You traveled extensively. You speak one additional language.", "(None,  None)"),
    14: ("You received an education. You know how to read the Common Tongue.", "(None,  None)"),
    15: ("You fought bravely for the Emperor and were awarded a medal for your courage.", "(None,  None)"),
    16: ("You saved an important noble from an assassination attempt.", "(None,  None)"),
    17: ("A human broke your chains and freed you to find your fortunes in the world.", "(None,  None)"),
    18: ("You took a sword from the corpse of a warrior you killed.", "(None,  None)"),
    19: ("The Gods of Blood and Iron visit you in your dreams. You start the game with 1 Insanity.", "(None,  None)"),
    20: ("You came into money and start the game with {} cp.", "(roll('2d6t'), None)"),
}


def roll_orc_background(dice_roll):
    background, rand = orc_background[dice_roll]
    return background.format(*eval(rand))


orc_personality_breakpoints = [4, 5, 7, 9, 13, 15, 17, 18]
orc_personalities = [
    "You fight to liberate your people from slavery.",
    "Orcs are more than the killers the emperor made them to be. They are people, with hearts and souls, dreams and "
    "ambitions. You believe you must rise above the savagery and find your place.",
    "The world is going to Hell. You say, let it.",
    "You take care of yourself, take what you want, and do what you want.",
    "Kill!",
    "You never question orders. You always do as you’re commanded.",
    "You want revenge and you’ll kill anyone that gets in your way.",
    "You believe you were made for a reason. Without your chains, you have no purpose.",
    "You believe your people have committed great acts of evil in the Empire’s name. You strive to right the wrongs."
]


def roll_orc_personality(dice_roll):
    return orc_personalities[bisect(orc_personality_breakpoints, dice_roll)]


orc_build_breakpoints = [4, 5, 7, 9, 13, 15, 17, 18]
orc_build = [
    'You are short and wiry.',
    'You are short and muscular.',
    'You are short.',
    'You are thin.',
    'You are of average height and weight.',
    'You are corpulent.',
    'You are tall.',
    'You are tall and gaunt.',
    'You are a giant among orcs.'
]


def roll_orc_build(dice_roll):
    return orc_build[bisect(orc_build_breakpoints, dice_roll)]


orc_appearance_breakpoints = [6, 9, 13, 16, 18]
orc_appearances = [
    'You are grotesque. Your face is a mass of scar tissue. Thick scars crisscross your body, held together with '
    'excrement, blood, and rot. '
    'Swaths of open sores weep streams of pus, and you reek ofcrude, leather stitching.',
    'You are monstrous, with thick, brutish features, weird growths sprouting from your skin, '
    'and nasty scars that cut jagged lines across your thick hide.',
    'You are ugly. You have thick tusks jutting from your broad jaw, a sloping forehead, and tiny eyes set deep in '
    'your skull.',
    'You are an orc of typical appearance, dirty and unkempt.',
    'Your features are somewhat less brutish, though you might have odd skin coloration, extra fur, and thick '
    'features.',
    'You stand out from other orcs. Your body is remarkably free from the scars and injuries '
    'that maim your fellows, and you are in pretty good health.'
]


def roll_orc_appearance(dice_roll):
    return orc_appearances[bisect(orc_appearance_breakpoints, dice_roll)]


orc_ages_breakpoints = [4, 8, 13, 16, 18]
orc_ages = [
    ('You are a child, 8 years old or younger.', 'None'),
    ('You are an adolescent, {} years old.', 'roll("1d5+7")'),
    ('You are a young adult, {} years old.', 'roll("1d6+12")'),
    ('You are a middle-aged adult, {} years old.', 'roll("1d8+18")'),
    ('You are an older adult, {} years old.', 'roll("1d6+26")'),
    ('You are a venerable adult, 33 years old or older.', 'None'),
]


def roll_orc_age(dice_roll):
    age, rand = orc_ages[bisect(orc_ages_breakpoints, dice_roll)]
    return age.format(eval(rand))


class Orc(Character):
    def __init__(self, s=None):
        if s:
            seed(s)
        self.ancestry = 'Orc'
        self.age = roll_orc_age(roll('3d6t'))
        self.build = roll_orc_build(roll('3d6t'))
        self.appearance = roll_orc_appearance(roll('3d6t'))
        self.background = roll_orc_background(roll('1d20t'))
        self.personality = roll_orc_personality(roll('3d6t'))
        super().__init__()

    def __str__(self):
        return (f"Age: {self.age}\nBuild: {self.build}\nAppearance: {self.appearance}\n"
                f"Background: {self.background}\nPersonality: {self.personality}\nFirst profession: "
                f"{self.professions[0]}\nSecond Profession: {self.professions[1]}\nInteresting Thing: "
                f"{self.intersting_thing}\nWealth: {self.wealth}")

    def __repr__(self):
        return f'Class: {self.ancestry}'


if __name__ == '__main__':
    azog = Orc('Azog')
    print(azog)
