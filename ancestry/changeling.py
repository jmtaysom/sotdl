# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 09:45:03 2018

@author: Jonathan Tross
"""

from bisect import bisect
from dice import roll

changeling_true_ages_breakpoints = [4, 8, 13, 16, 18]
changeling_true_ages = [
    ("You are a child, 8 years old or younger.",'None'),
    ("You are an adolescent, {} years old.", 'roll("1d6+8")'),
    ("You are a young adult, {} years old.", 'roll("1d11+14")'),
    ("You are a middle-aged adult, {} years old.", 'roll("1d15+25")'),
    ("You are an older adult, {} years old.", 'roll("1d20+40")'),
    ("You are a venerable adult, 61 years old or older.",'None'),
    ]

def roll_changeling_true_age(dice_roll):
    age, rand = changeling_true_ages[bisect(changeling_true_ages_breakpoints, dice_roll)]
    return age.format(eval(rand))


changeling_appearent_gender_breakpoints = [4]
changeling_appearent_gender = [
    "You appear to be male.",
    "You appear to be female.",
    ]

def roll_changeling_appearent_gender(dice_roll):
    return changeling_appearent_gender[bisect(changeling_appearent_gender_breakpoints, dice_roll)]


changeling_appearent_ancestry_breakpoints = [5, 8, 16, 18]
changeling_appearent_ancestry = [
    "You appear to be a goblin. Go to the Goblin ancestry entry to determine your age, build, and appearance.",
    "You appear to be a dwarf. Go to the Dwarf ancestry entry to determine your age, build, and appearance.",
    "You appear to be a human. Go to the Human ancestry entry to determine your age, build, and appearance.",
    "You appear to be an orc. Go to the Orc ancestry entry to determine your age, build, and appearance.",
    "The GM determines your ancestry, age, build, and appearance.",
    ]

def roll_changeling_appearent_ancestry(dice_roll):
    return changeling_appearent_ancestry[bisect(changeling_appearent_ancestry_breakpoints, dice_roll)]


changeling_background = {
    1: ("You only recently discovered your true nature, and you are having a difficult time adjusting to your new reality. You start the game with 1 Insanity.",'None'),
    2: ("You have no idea that you’re a changeling. You think you are a member of the ancestry whose form you adopted. Add an extra random profession. Until you become incapacitated or touch iron for the first time, you cannot use Steal Identity.", 'None'),
    3: ("You were enslaved by a hag and forced to perform unspeakable acts as she commanded you. You start the game with 1 Corruption.",  'None'),
    4: ("You murdered the person whose identity you stole so you could take over that person’s life. You start the game with 1 Corruption.", 'None'),
    5: ("When your “parents” learned what you were, they cast you out from your home and you were forced to make your own way in the world.",  'None'),
    6: ("You ran away from home when you learned what you were and lived among the faerie for many years.",  'None'),
    7: ("You have earned the enmity of a witch hunter. This foe hunts you and will try to kill you if your paths ever cross.", 'None'),
    8: ("Fearful townsfolk drove you out of your hometown. You have grown to hate them and plot revenge.",  'None'),
    9: ("The first time you stole someone’s identity, you also stole a few of that person’s memories.",  'None'),
    10: ("You earned a living working in your profession.",  'None'),
    11: ("You fell in love, and your lover is not aware of your true identity.",  'None'),
    12: ("After you were exiled from your hometown, a druid or witch took you in and cared for you. You always have a home with this character.",  'None'),
    13: ("You worked as an informant for the Inquisition.",  'None'),
    14: ("You received an education. You know how to read the Common Tongue.", 'None'),
    15: ("You learned a terrible secret while masquerading as someone else. Work out the nature of that secret with your Game Master.",  'None'),
    16: ("Your parents raised you even though they knew what you were. Their love and encouragement gave you the stability you needed to grow into a mature personality.",  'None'),
    17: ("The elf who made you recently found you and befriended you. You can call in one favor from that elf by speaking into a shell he or she gave you. The extent of the favor’s power is subject to the GM’s discretion.",  'None'),
    18: ("You adopted the form of someone famous, powerful, and important.",  'None'),
    19: ("You have ties to a criminal organization after being recruited into it for your magical gifts.",  'None'),
    20: ("You came into a quantity of money and start the game with {} cp.",  "roll('2d6t')"),
}

def roll_changeling_background(dice_roll):
    background, rand = changeling_background[dice_roll]
    return background.format(eval(rand))


changeling_personality_breakpoints = [4, 6, 7, 11, 14, 15, 17, 18]
changeling_personality = [
    "You steal the forms of others so you can do what you want without facing repercussions. You don’t care about how this affects other people.",
    "You enjoy taking on forms that let you work mischief.",
    "You adopt forms that give you power over others. Power ensures your safety.",
    "You take on other forms for profit, usually to gain access to places normally forbidden to you.",
    "You are careful about the forms you take. You try to stay out of trouble and keep your secrets safe.",
    "You strive to do the right thing and use your disguises to help other people, as well as to protect yourself from your enemies.",
    "Your nature is a gift, and you use it to do what you think is right, even if it means upsetting others along the way.",
    "You tend to stick to one form as long as possible; you crave stability and would do anything to be 'normal.'",
    "You use your talents to help others, to make the world a better place, and to right wrongs.",
    ]

def roll_changeling_personality(dice_roll):
    return changeling_personality[bisect(changeling_personality_breakpoints, dice_roll)]


changeling_quirk = {
    1: "You always speak in the third person.",
    2: "Your eyes glow green in the dark.",
    3: "Animals become nervous around you.",
    4: "You can adopt only male forms or only female forms.",
    5: "You are wild and impulsive.",
    6: "You always revert to the first form you adopted.",
    7: "The scent of iron sickens you.",
    8: "You have terrible nightmares.",
    9: "You sometimes hear voices.",
    10: "You tend to lose small, inconsequential things.",
    11: "One night each year, you lose your Steal Identity talent.",
    12: "You can only assume the appearance of dead people.",
    13: "You speak in whispers.",
    14: "You give off an odd, earthy smell.",
    15: "You can never keep your clothes clean.",
    16: "You cannot get drunk.",
    17: "You must always speak the truth as you know it.",
    18: "You find meat repulsive.",
    19: "You laugh at inappropriate times.",
    20: "Forms you adopt have no hair or fingernails.",
}

def roll_changeling_quirk(dice_roll):
    return changeling_quirk[dice_roll]


def roll_changeling():
    print("True Age:", roll_changeling_true_age(roll('3d6t')))
    print("Appearent Gender:", roll_changeling_appearent_gender(roll('1d6t')))
    print("Ancestry:", roll_changeling_appearent_ancestry(roll('3d6t')))
    print("Background:", roll_changeling_background(roll('1d20t')))
    print("Personality:", roll_changeling_personality(roll('3d6t')))
    print("Quirk:", roll_changeling_quirk(roll('1d20t')))    
    
if __name__ == '__main__':
    roll_changeling()