from bisect import bisect
from dice import roll

orc_background = {
    1: ("You butchered helpless people. Gain 2 Corruption.", "None"),
    2: ("You were briefly possessed by a demon. Gain 1 Corruption.", "None"),
    3: ("You spent {} years in the fighting pit, testing your skills against other orcs for the amusement of the crowds.", "roll('1d6t')"),
    4: ("You stayed loyal to the Empire and fought against other orcs. You were branded as a traitor and cast out.", "None"),
    5: ("You caught the rot and lost your nose and ears.", "None"),
    6: ("You were chained to the oars in a slave ship for {} years.", "roll('1d6t')"),
    7: ("You were made a eunuch and stood guard over the emperor’s concubines.", "None"),
    8: ("You have scar tissue over half your body from when you were caught in the blast of a spell.", "None"),
    9: ("You escaped your slavery and have lived in the wilderness ever since.", "None"),
    10: ("You earned a living working in your profession.", "None"),
    11: ("You fell in love with a human and were spurned for your affections.", "None"),
    12: ("You sired or gave birth to {} children. {} are still alive.", "max([roll('1d6-2t'), 0])"),
    13: ("You traveled extensively. You speak one additional language.", "None"),
    14: ("You received an education. You know how to read the Common Tongue.", "None"),
    15: ("You fought bravely for the Emperor and were awarded a medal for your courage.", "None"),
    16: ("You saved an important noble from an assassination attempt.", "None"),
    17: ("A human broke your chains and freed you to find your fortunes in the world.", "None"),
    18: ("You took a sword from the corpse of a warrior you killed.", "None"),
    19: ("The Gods of Blood and Iron visit you in your dreams. You start the game with 1 Insanity.", "None"),
    20: ("You came into money and start the game with {} cp.", "roll('2d6t')"),
}


def roll_orc_background(dice_roll):
    background, rand = orc_background[dice_roll]
    return background.format(eval(rand))


orc_personality_breakpoints = [4, 5, 7, 9, 13, 15, 17, 18]
orc_personalities = [
    "You fight to liberate your people from slavery.",
    "Orcs are more than the killers the emperor made them to be. They are people, with hearts and souls, dreams and ambitions. You believe you must rise above the savagery and find your place.",
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
    'You are grotesque. Your face is a mass of scar tissue. Thick scars crisscross your body, held together with excrement, blood, and rot. '
    'Swaths of open sores weep streams of pus, and you reek ofcrude, leather stitching.',
    'You are monstrous, with thick, brutish features, weird growths sprouting from your skin, '
    'and nasty scars that cut jagged lines across your thick hide.',
    'You are ugly. You have thick tusks jutting from your broad jaw, a sloping forehead, and tiny eyes set deep in your skull.',
    'You are an orc of typical appearance, dirty and unkempt.',
    'Your features are somewhat less brutish, though you might have odd skin coloration, extra fur, and thick features.',
    'You stand out from other orcs. Your body is remarkably free from the scars and injuries '
    'that maim your fellows, and you are in pretty good health.'
]


def roll_orc_appearance(dice_roll):
    return orc_appearances[bisect(orc_appearance_breakpoints, dice_roll)]


orc_ages_breakpoints = [4, 8, 13, 16, 18]
orc_ages = [
    'You are a child, 8 years old or younger.',
    'You are an adolescent, 8 to 12 years old.',
    'You are a young adult, 13 to 18 years old.',
    'You are a middle-aged adult, 19 to 26 years old.',
    'You are an older adult, 27 to 32 years old.',
    'You are a venerable adult, 33 years old or older.'
]


def roll_orc_age(dice_roll):
    return orc_age[bisect(orc_age_breakpoints, dice_roll)]


def roll_orc():
    print(roll_orc_background(roll('1d20t')))
    print(roll_orc_personality(roll('3d6t')))
    print(roll_orc_build(roll('3d6t')))
    print(roll_orc_appearance(roll('3d6t')))
    print(roll_orc_age(roll('3d6t')))


if __name__ == '__main__':
    roll_orc()
