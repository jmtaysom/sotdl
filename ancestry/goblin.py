from bisect import bisect
from random import seed
from dice import roll

from ancestry.character import Character


goblin_background = {
    1: ("You spent the last {} year(s) in a drunken stupor. you are not proud.", "roll('1d6t')"),
    2: ("The Goblin King turned you into a toad. You escaped that fate after you convinced an Elf maiden to kiss "
        "you. When she did and screamed, you killed her. You start the game with 1 Corruption.", "None"),
    3: ("You accidently got your entire tribe killed.", "None"),
    4: ("You were orphaned and raised by giant rats.", "None"),
    5: ("You accidentally released a demon into the world.", "None"),
    6: ("You spent two days believing you were a fearsome dog. You start the game with 1 Insanity.", "None"),
    7: ("A hag made you her love slave for {} years.", "roll('1d6t')"),
    8: ("Dwarfs almost wiped out your tribe. You are one of {} survivors.", "roll('1d6t')"),
    9: ("You nearly drowned when the sewers flooded.", "None"),
    10: ("You earned a living working in your profession.", "None"),
    11: ("Choose a character. He or she saved your life and you now owe that character a debt.", "None"),
    12: ("You are an unrepentant criminal. Add a random criminal profession to your list of professions.", "None"),
    13: ("You traveled extensively. You speak one additional language.", "None"),
    14: ("You stole a knife from a dashing knight.", "None"),
    15: ("You snuck into Alfheim and stole a lock of hair from the Faerie Queen.", "None"),
    16: ("You killed and ate 100 diseased rats.", "None"),
    17: ("You were a henchman to a powerful wizard.", "None"),
    18: ("You found a signet ring in a sewer.", "None"),
    19: ("You are the seventeenth son or daughter of the Goblin King.", "None"),
    20: ("You came into money and start the game with {} cp.", "roll('2d6t')"),
}


def roll_goblin_background(dice_roll):
    background, rand = goblin_background[dice_roll]
    return background.format(eval(rand))


goblin_personality_breakpoints = [4, 5, 7, 9, 13, 15, 17, 18]
goblin_personalities = [
    "You are a bully and enjoy tormenting things that are weaker than you.",
    "You like violence, especially when it’s random and senseless.",
    "You try to rise above the filth and squalor of your people to do good in the world.",
    "You love playing tricks on other people and find their pain hilarious!",
    "You look out for yourself. To hell with everyone else!",
    "You’re just trying to stay alive!",
    "Your people didn’t deserve exile, but exile you got. You believe you will make places for yourselves and prove "
    "to those stinking elves they were wrong.",
    "You live to serve the strong and mighty.",
    "You hope to redeem your people in the eyes of the Faerie Queen."
]


def roll_goblin_personality(dice_roll):
    return goblin_personalities[bisect(goblin_personality_breakpoints, dice_roll)]


goblin_odd_habit = {
    1: "You save all your secretions in small bottles and give them as gifts to people you like.",
    2: "You never bathe.",
    3: "You punctuate your sentences by spitting.",
    4: "You have tremendous flatulence, yet you seem never to notice when you break wind.",
    5: "You eat only candy.",
    6: "You collect the genitals from creatures you kill and wear them as jewelry.",
    7: "You lick things to claim them as your own.",
    8: "You dress in fancy clothes.",
    9: "You refuse to wear shoes.",
    10: "You keep cockroaches as pets.",
    11: "You always inspect your bowel movements, spreading the mess around with your fingers.",
    12: "You keep a bit of iron on your person at all times.",
    13: "You speak in a singsong voice.",
    14: "You eat a bit of flesh from any living thing you kill.",
    15: "You cry a lot.",
    16: "You tell filthy jokes at inappropriate times.",
    17: "You wear a child’s costume and refuse to take it off.",
    18: "You keep a large collection of spoons.",
    19: "You like to hide.",
    20: "Make something up!",
}


def roll_goblin_odd_habit(dice_roll):
    return goblin_odd_habit[dice_roll]


goblin_appearance = {
    1: ("You have a long, pointed nose.", "None"),
    2: ("You have bright green or orange skin.", "None"),
    3: ("You have the head of a dog.", "None"),
    4: ("You have a reptilian appearance with small horns sprouting from the top of your head.", "None"),
    5: ("You have a wide, leering grin.", "None"),
    6: ("You have a pig’s snout in place of a nose.", "None"),
    7: ("You have long, slender fingers.", "None"),
    8: ("You have a tooth growing out from your forehead.", "None"),
    9: ("You have a tail.", "None"),
    10: ("Fur grows thickly on your arms and legs.", "None"),
    11: ("You are completely hairless.", "None"),
    12: ("You have all the warts.", "None"),
    13: ("A large cyst grows on your back.", "None"),
    14: ("You have an abnormally long and pointed chin.", "None"),
    15: ("A single horn grows out from the side of your head.", "None"),
    16: ("You have one eye.", "None"),
    17: ("You have {} extra fingers, placed on your body wherever you wish.", "roll('1d6t')"),
    18: ("You have enormous ears.", "None"),
    19: ("You have stubby little legs.", "None"),
    20: ("Make something up!", "None"),
}


def roll_goblin_appearance(dice_roll):
    appearance, rand = goblin_appearance[dice_roll]
    return appearance.format(eval(rand))


goblin_ages_breakpoints = [4, 8, 13, 16, 18]
goblin_ages = [
    ('You are a child, 6 years old or younger.', 'None'),
    ('You are an adolescent, {} years old.', 'roll("1d4+6")'),
    ('You are a young adult, {} years old.', 'roll("1d15+10")'),
    ('You are a middle-aged adult, {} years old.', 'roll("1d25+25")'),
    ('You are an older adult, {} years old.', 'roll("1d25+50")'),
    ('You are a venerable adult, 76 years old or older.', 'None')
]


def roll_goblin_age(dice_roll):
    age, rand = goblin_ages[bisect(goblin_ages_breakpoints, dice_roll)]
    return age.format(eval(rand))


goblin_build_breakpoints = [4, 5, 7, 9, 13, 15, 17, 18]
goblin_build = [
    'You are short and spindly.',
    'You are short and round.',
    'You are short.',
    'You are wiry.',
    'You fall within the normal height and weight ranges for goblins.',
    'You are pudgy.',
    'You are tall.',
    'You are tall and lanky.',
    'You are very tall and heavy.',
]


def roll_goblin_build(dice_roll):
    return goblin_build[bisect(goblin_build_breakpoints, dice_roll)]


def roll_goblin():
    print(roll_goblin_background(roll('1d20t')))
    print(roll_goblin_personality(roll('3d6t')))
    print(roll_goblin_odd_habit(roll('1d20t')))
    print(roll_goblin_appearance(roll('1d20t')))
    print(roll_goblin_build(roll('3d6t')))
    print(roll_goblin_age(roll('3d6t')))


class Goblin(Character):
    def __init__(self, s=None):
        if s:
            seed(s)
        self.ancestry = 'Goblin'
        self.age = roll_goblin_age(roll('3d6t'))
        self.build = roll_goblin_build(roll('3d6t'))
        self.appearance = roll_goblin_appearance(roll('3d6t'))
        self.odd_habit = roll_goblin_odd_habit(roll('1d10t'))
        self.background = roll_goblin_background(roll('1d20t'))
        self.personality = roll_goblin_personality(roll('3d6t'))
        super().__init__()

    def __str__(self):
        return (f"Age: {self.age}\nBuild: {self.build}\nAppearance: {self.appearance}\nOdd Habit: {self.odd_habit}\n"
                f"Background: {self.background}\nPersonality: {self.personality}\nFirst profession: "
                f"{self.professions[0]}\nSecond Profession: {self.professions[1]}\nInteresting Thing: "
                f"{self.intersting_thing}\nWealth: {self.wealth}")

    def __repr__(self):
        return f'Class: {self.ancestry}'


if __name__ == '__main__':
    warwick = Goblin('Warwick')
    print(warwick)
