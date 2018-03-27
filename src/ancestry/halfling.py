# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:31:20 2018

@author: Jonathan Tross
"""


from bisect import bisect
from random import seed
from dice import roll

from ancestry.character import Character

halfling_ages_breakpoints = [4, 8, 13, 16, 18]
halfling_ages = [
    ("You are a child, 11 years old or younger.", 'None'),
    ("You are an adolescent, {} years old.", 'roll("1d6+11")'),
    ("You are a young adult, {} years old.", 'roll("1d18+17")'),
    ("You are a middle-aged adult, {} years old.", 'roll("1d20+35")'),
    ("You are an older adult, {} years old.", 'roll("1d20+55")'),
    ("You are a venerable adult, 76 years or older.", 'None'),
    ]


def roll_halfling_age(dice_roll):
    age, rand = halfling_ages[bisect(halfling_ages_breakpoints, dice_roll)]
    return age.format(eval(rand))


halfling_build_breakpoints = [4, 5, 7, 9, 13, 15, 17, 18]
halfling_build = [
    "You are quite small for a halfling, standing just 2 feet tall and weighing 40 pounds.",
    "You grew horizontally instead of vertically. You have a rounded body and short, stubby limbs.",
    "You are short for a halfling.",
    "You are skinny no matter how much you eat.",
    "You are normal height and weight for a halfling.",
    "Good living has rewarded you with considerable bulk.",
    "You are tall by halfling standards and can pass for a short human.",
    "You are tall and slender, with a willowy body. Your family claims you have faerie blood.",
    "You are enormous for a halfling, standing 5 feet tall and weighing close to 200 pounds. Increase your Size to 1.",
    ]


def roll_halfling_build(dice_roll):
    return halfling_build[bisect(halfling_build_breakpoints, dice_roll)]


halfling_appearance_breakpoints = [4, 5, 7, 9, 13, 15, 17, 18]
halfling_appearance = [
    "Luck saved your life, but you did not escape death unscathed. You bear horrific scars, your appearance a mess "
    "that evokes revulsion in anyone who lays eyes on you.",
    "You are downright ugly. Your features look like they wandered around your head and settled in where they felt "
    "comfortable.",
    "You have an unattractive quality that ruins your otherwise plain appearance.",
    "You have no distinctive physical qualities. People sometimes forget you are there.",
    "You are perfectly average and unremarkable.",
    "Other halflings find you attractive, likely due to your winning personality.",
    "You are attractive.",
    "You are striking, catching the eye of halflings and humans alike.",
    "You are a great beauty, an individual perfect by the standards of your people and others. When you enter a room, "
    "people notice.",
    ]


def roll_halfling_appearance(dice_roll):
    return halfling_appearance[bisect(halfling_appearance_breakpoints, dice_roll)]


halfling_background = {
    1: ("Your curiosity led you to a very dark place, where you witnessed something that unhinged your mind. "
        "You start the game with {} Insanity.",  "roll('1d3+1')"),
    2: ("You discovered a terrible secret. To keep your family safe, you decided to disappear.",  'None'),
    3: ("Hard times forced you to make ends meet by committing crimes. Gain one criminal profession.",  'None'),
    4: ("You stole something of great importance. Someone else took the blame and was executed for the crime.",
        'None'),
    5: ("A nasty plague wiped out your community. You were the sole survivor.",  'None'),
    6: ("An orc captured you and kept you as a prisoner for {} years. The orc believed you were a lucky charm.",
        "roll('1d6t')"),
    7: ("You went spelunking and became lost until a group of gnomes rescued you.",  'None'),
    8: ("You have terrible wanderlust. You can’t stay put for more than a few weeks at a time. Add one language to the "
        "list of the languages you can speak.",  'None'),
    9: ("You worked a series of a terrible jobs in a large city.",  'None'),
    10: ("You earned a living working in your profession.",  'None'),
    11: ("A human fell in love with you, but you rejected the relationship.",  'None'),
    12: ("You have a large immediate family with {} members.",  "roll('2d6+3')"),
    13: ("You befriended a powerful witch or wizard who came to visit your community.",  'None'),
    14: ("You received an education. You know how to read the Common Tongue.",  'None'),
    15: ("When your town came under attack, you led your people to safety.",  'None'),
    16: ("One time, an ogre swallowed you whole. Somehow, you survived and came out the other end, filthy but intact.",
         'None'),
    17: ("You were abducted by faeries, but you managed to escape.",  'None'),
    18: ("You went on a long journey with a band of dwarfs. You plan to write about your experiences one day.",
         'None'),
    19: ("You found an odd treasure in a cave. You start the game with one enchanted object of the GM’s choice.",
         'None'),
    20: ("You came into money and start the game with {} copper pennies.",  "roll('3d6t')"),
    }


def roll_halfling_background(dice_roll):
    background, rand = halfling_background[dice_roll]
    return background.format(eval(rand))


halfling_religion_breakpoints = [5, 7, 9, 13]
halfling_religion = [
    "You belong to the cult of the New God.",
    "You studied a bit of witchcraft.",
    "You follow the tenets of the Old Faith.",
    "You have little use for the gods or religion.",
    "You don’t believe the gods exist.",
    ]


def roll_halfling_religion(dice_roll):
    return halfling_religion[bisect(halfling_religion_breakpoints, dice_roll)]


halfling_personality_breakpoints = [4, 5, 7, 9, 13, 15, 17, 18]
halfling_personality = [
    "Something is wrong with you. You dream about hurting people, cutting them up and making them scream. You worry "
    "that you may one day act out on these fantasies.",
    "You have a hard time paying attention. You are easily distracted and tend to abandon whatever you’re doing to do "
    "something else.",
    "You keep your head down and try not to cause trouble.",
    "You do what you want, when you want. You won’t let anyone get in your way. You can’t soar with the eagles when "
    "you’re scratching with the turkeys.",
    "You try to do right by your friends, provided doing so doesn’t slow you down.",
    "You are a good person who enjoys helping others.",
    "You look after your people, whether they are other halflings or the people you call your friends. You would do "
    "anything for them.",
    "You always do what you think is right, even if doing so gets you into trouble.",
    "You are concerned about what others think of you and alter your behavior to make others like you.",
    ]


def roll_halfling_personality(dice_roll):
    return halfling_personality[bisect(halfling_personality_breakpoints, dice_roll)]


def roll_halfling():
    print("Age:", roll_halfling_age(roll('3d6t')))
    print("Build:", roll_halfling_build(roll('3d6t')))
    print("Appearance:", roll_halfling_appearance(roll('3d6t')))
    print("Background:", roll_halfling_background(roll('1d20t')))
    print("Religion:", roll_halfling_religion(roll('3d6t')))
    print("Personality:", roll_halfling_personality(roll('3d6t')))


class Halfling(Character):
    def __init__(self, s=None):
        super().__init__(s)
        self.ancestry = 'Halfling'
        self.age = roll_halfling_age(roll('3d6t'))
        self.build = roll_halfling_build(roll('3d6t'))
        self.appearance = roll_halfling_appearance(roll('3d6t'))
        self.religion = roll_halfling_religion(roll('1d20t'))
        self.background = roll_halfling_background(roll('1d20t'))
        self.personality = roll_halfling_personality(roll('3d6t'))

    def __str__(self):
        return (f"Age: {self.age}\nBuild: {self.build}\nAppearance: {self.appearance}\nReligion: {self.religion}\n"
                f"Background: {self.background}\nPersonality: {self.personality}\nFirst profession: "
                f"{self.professions[0]}\nSecond Profession: {self.professions[1]}\nInteresting Thing: "
                f"{self.interesting_thing}\nWealth: {self.wealth}\n\nSeed: {self.seed}")

    def __repr__(self):
        return f'Class: {self.ancestry}'


if __name__ == '__main__':
    sam = Halfling('Sam')
    print(sam)
