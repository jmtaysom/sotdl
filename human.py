from bisect import bisect
from dice import roll

human_background = {
    1: ("You died and returned to life. You start the game with {} Insanity.", "roll('1d6t')"),
    2: ("You were briefly possessed by a demon. You start the game with 1 Corruption.", "None"),
    3: ("You spent {} years as a prisoner in a dungeon.", "roll('1d6t')"),
    4: ("You murdered someone in cold blood. You start the game with 1 Corruption.", "None"),
    5: ("You caught and recovered from a terrible disease.", "None"),
    6: ("You belonged to a strange cult and saw many strange things. You start the game with 1 Insanity.", "None"),
    7: ("The faerie held you prisoner for {} years.", "roll('1d20t')"),
    8: ("You lost a loved one and their loss haunts you still.", "None"),
    9: ("You lost a finger, a few teeth, or an ear, or you gained a scar.", "None"),
    10: ("You earned a living working in your profession.", "None"),
    11: ("You fell in love and the relationship ended well or is ongoing.", "None"),
    12: ("You have a spouse and {} children.", "max([roll('1d6-2t'), 0])"),
    13: ("You traveled extensively. You speak one additional language.", "None"),
    14: ("You received an education. You know how to read the Common Tongue.", "None"),
    15: ("You saved your town from terrible monsters.", "None"),
    16: ("You foiled a plot to kill someone important or you brought a killer to justice.", "None"),
    17: ("You performed a great deed and are a hero to the people in your hometown.", "None"),
    18: ("You found an old treasure map.", "None"),
    19: ("Someone important and powerful owes you a favor.", "None"),
    20: ("You came into money and start the game with {} cp.", "roll('2d6t')"),
}


def roll_human_background():
    d20 = roll('1d20t')
    background, rand = human_background[d20]
    return background.format(eval(rand))


human_personality_breakpoints = [4, 5, 7, 9, 13, 15, 17, 18]
human_personalities = [
    "You are cruel, wicked, and self-serving. You enjoy  making others suffer.",
    "You are erratic and unpredictable. You have a hard time keeping your word and tend toward capricious behavior.",
    "Might makes right. Obedience to authority is the highest ideal.",
    "You look after yourself first and foremost. You’re not above double-crossing friends.",
    "You put your interests and those of your friends above all else.",
    "You help others because it’s the right thing to do.",
    "You try to do what you think is right, even if it breaks laws and social conventions.",
    "Your honor and duty guide everything you do.",
    "You are committed to good and noble causes, and you never stray from your beliefs even if your insistence would " 
    "cost you your life."
]


def roll_human_personality():
    dice_roll = roll('3d6t')
    return human_personalities[bisect(human_personality_breakpoints, dice_roll)]


human_religion_breakpoints = [4, 5, 7, 11, 16]
human_religions = [
    'You belong to a cult dedicated to a dark power.',
    'You belong to a heretical sect.',
    'You were raised in the teachings of witchcraft.',
    'You follow the tenets of the Old Faith.',
    'You belong to the Cult of the New God.',
    'You have no religion.'
]


def roll_human_religion():
    dice_roll = roll('3d6t')
    return human_religions[bisect(human_religion_breakpoints, dice_roll)]


def human():
    print(roll_human_background())
    print(roll_human_personality())
    print(roll_human_religion())


human()