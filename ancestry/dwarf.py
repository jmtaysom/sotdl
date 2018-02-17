from bisect import bisect
from dice import roll


age_breakpoints_dwarf = [4, 8, 13, 16, 18]
ages_dwarf = [
    ('You are a child, 20 years old or younger.', 'None'),
    ('You are an adolescent, {} years old.', 'roll("1d11+9")'),
    ('You are a young adult, {} years old.', 'roll("1d20+30")'),
    ('You are a middle-aged adult, {} years old.', 'roll("1d50+50")'),
    ('You are an older adult, {} years old.', 'roll("1d50+100")'),
    ('You are a venerable adult, 151 years old or older.', 'None'),
]


def roll_dwarf_age(dice_roll):
    age, rand = ages_dwarf[bisect(age_breakpoints_dwarf, dice_roll)]
    return age.format(eval(rand))


build_breakpoints_dwarf = [4, 7, 9, 13, 16, 18]
build_dwarf = [
    'You are short and scrawny.',
    'You are short and fat.',
    'You stand a bit shorter than other dwarfs.',
    'You are average in height and build.',
    'You have a magnificent belly.',
    'You are tall.',
    'You are tall and heavy.',
]


def roll_dwarf_build(dice_roll):
    return build_dwarf[bisect(build_breakpoints_dwarf, dice_roll)]


appearance_breakpoints_dwarf = [5, 7, 9, 12, 16]
appearance_dwarf = [
    'You have a monstrous appearance, likely due to hard living and several near misses. Your face is a mass of scar'
    'tissue, probably missing an ear, an eye, or your nose. You also display some unusual habit, such as pounding nails' 
    'into your skull or greasing your body with troll fat.',
    'You have several interesting features that work together to make you one ugly brute. Filth from digging in the  '
    'dirt, mites infesting your hair, skin lashed with healing scars, and a rich aroma of vomit—all these contribute '
    'to your distinctive style.',
    'You look like a typical dwarf, being hairy, portly, and grubby.',
    'You take better care of yourself than most dwarfs and keep your facial hair well groomed.',
    'You take pride in your appearance. You stay clean, oil your facial hair, and perhaps braid it or tie it with '
    'metal rings.',
    'You are quite fetching for a dwarf. You have regal features, good bearing, and a deep voice. You take pride in '
    'your appearance.'
]


def roll_dwarf_appearance(dice_roll):
    return appearance_dwarf[bisect(appearance_breakpoints_dwarf, dice_roll)]


hatred_dwarf = {
    1: 'Ogres',
    2: 'Troglodytes',
    3: 'Beastmen',
    4: 'Orcs',
    5: 'Goblins',
    6: 'Elves',
    7: 'Trolls',
    8: 'Giants',
    9: 'Dragons',
    10: 'Demons'
}


def roll_dwarf_hatred(dice_roll):
    return 'You hate ' + hatred_dwarf[dice_roll].lower()


background_dwarf = {
    1: ('You sold your soul to a devil to gain wealth. The devil betrayed you and left you penniless. You start the '
       'game with 1 Corruption.', 'None'),
    2: ('Your ancestors appeared to you in a vision and sent you to recover a fabled relic.', 'None'),
    3: ('You accidentally killed someone close to you.', 'None'),
    4: ('You stole gold from a rival clan and the theft shames you.', 'None'),
    5: ('You fought against the creatures you hate and lost.', 'None'),
    6: ('You brought shame to yourself and your clan. You live as an exile, searching for redemption, even if that '
        'redemption comes with a glorious death.', 'None'),
    7: ('You were taken prisoner by the creatures you hate. You lived as a slave for {} years.', 'roll("2d6t")'),
    8: ('The creatures you hate overran your home and wiped out your clan.', 'None'),
    9: ('You survived a cave-in and get a bit nervous when underground.', 'None'),
    10: ('You earned a living working in your profession.', 'None'),
    11: ('You are a sworn servant of the Dwarf King.', 'None'),
    12: ('You are a gifted artisan. Add artisan : (any one) to your list of professions.', 'None'),
    13: ('You traveled extensively. You speak one additional language.', 'None'),
    14: ('You inherited a battleaxe or a warhammer from an ancestor.', 'None'),
    15: ('You discovered a vein of gold under your mountain home.', 'None'),
    16: ('You hunted down and helped kill a creature you hate.', 'None'),
    17: ('You performed a great deed, and you are a hero to your clan.', 'None'),
    18: ('You have a key to an ancient treasure vault lost to the dwarfs long ago.', 'None'),
    19: ('You are the rightful heir to a stronghold overrun by the enemies of your people.', 'None'),
    20: ('You came into money and start the game with {} cp.', 'roll("2d6")'),
}


def roll_dwarf_background(dice_roll):
    background, rand = background_dwarf[dice_roll]
    return background.format(eval(rand))


personality_breakpoints_dwarf = [4, 5, 7, 9, 13, 15, 17, 18]
personality_dwarf = [
    'Your hatred is a living thing. It drives you, gives you strength, and helps you triumph over your enemies.',
    'You seek a glorious death killing your enemies.',
    'You love gold more than anything. You love the way it feels, the sound it makes, and the taste of it.',
    'You believe other people covet your wealth. It is your duty to protect what is yours—at any cost.',
    'Your honor is your life. You would never do anything to bring shame to your people.',
    'You surrender to the will of your ancestors, the customs of your people, and the good of all.',
    'You believe your people must rise above their greed and suspicion. In these dark times, you must band together to '
    'overcome the doom that awaits you all.',
    'You don’t trust or like non-dwarfs, but they have their uses.',
    'You have little use for the customs of your people. It’s time to move past the dusty caves and seek out fortunes '
    'elsewhere.'
]


def roll_dwarf_personality(dice_roll):
    return personality_dwarf[bisect(personality_breakpoints_dwarf, dice_roll)]


def roll_dwarf():
    print(roll_dwarf_age(roll('3d6t')))
    print(roll_dwarf_build(roll('3d6t')))
    print(roll_dwarf_appearance(roll('3d6t')))
    print(roll_dwarf_hatred(roll('1d10')))
    print(roll_dwarf_background(roll('1d20')))
    print(roll_dwarf_personality(roll('3d6t')))


if __name__ == '__main__':
    roll_dwarf()
