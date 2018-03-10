from bisect import bisect
from random import seed
from dice import roll

from ancestry.character import Character

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


def roll_human_background(dice_roll):
    background, rand = human_background[dice_roll]
    return background.format(eval(rand))


human_build_breakpoints = [4, 5, 7, 9, 13, 15, 17, 18]
human_build = [
    'You are short and thin.',
    'You are short and heavy.',
    'You are short.',
    'You are slender.',
    'You are average in height and weight.',
    'You are a bit overweight.',
    'You are tall.',
    'You are tall and thin.',
    'You are very tall and heavy.',
]


def roll_human_build(dice_roll):
    return human_build[bisect(human_build_breakpoints, dice_roll)]


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


def roll_human_personality(dice_roll):
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


def roll_human_religion(dice_roll):
    return human_religions[bisect(human_religion_breakpoints, dice_roll)]


human_appearance_breakpoints = [4, 5, 7, 9, 13, 15, 17, 18]
human_appearances = [
    'You are hideous. You look like a monster. Children cry when they encounter you, the weak of heart faint when they '
    'see you, and one person vomited after getting a good look at your face.',
    'You are ugly, and people find your visage unpleasant thanks to a scar, wen, beetling brows, boils, piles, a '
    'wandering or weeping eye, or something else of a similar magnitude.',
    'Most consider you homely: not quite ugly, but a bit worse than plain.',
    'You are plain and uninteresting to look upon. People notice you, but your appearance fails to make an impression.',
    'You are perfectly average in appearance. You look like everyone else.',
    'You have a physical quality that makes you attractive to others. You might have pretty eyes, lips, hair, shape, '
    'or something else.',
    'You have several attractive physical qualities that make you quite comely.',
    'You are one of the great beauties in the land, an individual of almost unsurpassed form and appearance. People '
    'notice you.',
    'You put beautiful people to shame. You are so striking, heads turn to follow you wherever you go. People become '
    'infatuated with you, stumbling over their words and feeling flustered when you show them attention. There’s a fine'
    ' line between love and hate. Should you spurn the attentions of people you enamor, their affection might sour to '
    'resentment and even hatred.',
]


def roll_human_appearance(dice_roll):
    return human_appearances[bisect(human_appearance_breakpoints, dice_roll)]


human_ages_breakpoints = [4, 8, 13, 16, 18]
human_ages = [
    ('You are a child, 11 years old or younger.', 'None'),
    ('You are an adolescent, {} years old.', 'roll("1d6+11")'),
    ('You are a young adult, {} years old.', 'roll("1d18+17")'),
    ('You are a middle-aged adult, {} years old.', 'roll("1d20+35")'),
    ('You are an older adult, {} years old.', 'roll("1d20+55")'),
    ('You are a venerable adult, 76 years old or older.', 'None') 
]


def roll_human_age(dice_roll):
    age, rand = human_ages[bisect(human_ages_breakpoints, dice_roll)]
    return age.format(eval(rand))


def roll_human():
    print(roll_human_background(roll('1d20t')))
    print(roll_human_personality(roll('3d6t')))
    print(roll_human_religion(roll('3d6t')))
    print(roll_human_appearance(roll('3d6t')))
    print(roll_human_age(roll('3d6t')))


class Human(Character):
    def __init__(self, s=None):
        if s:
            seed(s)
        self.ancestry = 'Human'
        self.age = roll_human_age(roll('3d6t'))
        self.appearance = roll_human_appearance(roll('3d6t'))
        self.religion = roll_human_religion(roll('3d6t'))
        self.background = roll_human_background(roll('1d20t'))
        self.personality = roll_human_personality(roll('3d6t'))
        self.build = roll_human_build(roll('3d6t'))
        super().__init__()

    def __str__(self):
        return (f"Age: {self.age}\nBuild: {self.build}\nAppearance: {self.appearance}\nReligion: {self.religion}\n"
                f"Background: {self.background}\nPersonality: {self.personality}\nFirst profession: "
                f"{self.professions[0]}\nSecond Profession: {self.professions[1]}\nInteresting Thing: "
                f"{self.intersting_thing}\nWealth: {self.wealth}")


    def __repr__(self):
        return f'Class: {self.ancestry}'


if __name__ == '__main__':
    john = Human('John')
    print(john)
