# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:02:03 2018

@author: Jonathan Tross
"""

from bisect import bisect
from random import seed
from dice import roll

from ancestry.character import Character


faun_ages_breakpoints = [4, 8, 13, 16, 18]
faun_ages = [
    ("You are a child, 11 years old or younger.",'None'),
    ("You are an adolescent, {} years old.", 'roll("1d6+11")'),
    ("You are a young adult, {} years old.", 'roll("1d18+17")'),
    ("You are a middle-aged adult, {} years old.", 'roll("1d20+35")'),
    ("You are an older adult, {} years old.", 'roll("1d20+55")'),
    ("You are a venerable adult, 76 years or older.",'None'),
    ]

def roll_faun_age(dice_roll):
    age, rand = faun_ages[bisect(faun_ages_breakpoints, dice_roll)]
    return age.format(eval(rand))


faun_build_breakpoints = [4, 5, 7, 9, 13, 15, 17, 18]
faun_build = [
    "You are short and scrawny, likely due to the harshness of your upbringing.",
    "You are short and round, obviously well fed.",
    "You are short for your kind, no taller than 3-1/2 feet.",
    "You are slender and wiry.",
    "You have a typical height and weight for a faun",
    "You are heavy, unusually curvaceous or plump.",
    "You stand a full foot taller than other fauns.",
    "You are tall and gaunt.",
    "You tower over other fauns, have large curling ram horns, and a muscled body. Increase your Strength by 2 and reduce your Agility by 2..",
    ]

def roll_faun_build(dice_roll):
    return faun_build[bisect(faun_build_breakpoints, dice_roll)]


faun_appearance_breakpoints = [4, 5, 7, 9, 13, 15, 17, 18]
faun_appearance = [
    "Little trace of your human heritage appears in your features, and your face is strange and angular. Unusual whorls mark your leathery hide. Others might become uncomfortable when they see you.",
    "You are brutish, more like a wild animal than a person. Your eyes are those of a goat, and your posture is hunched, your gait lurching.",
    "Nothing about you is attractive. Human qualities are evident here and there, but your abundant animal traits overshadow them.",
    "Your animal traits are subdued—your horns are mere nubs, and the fur covering your legs is thin.",
    "You look like most other fauns, with small horns on your brow and legs covered in fur down to your cloven feet.",
    "You have an appealing appearance, such as a well-formed body, bright eyes, or warm smile. Your appearance can put others more at ease.",
    "You are quite attractive.",
    "You are so striking to behold that others often want to be around you.",
    "You inherited the very best qualities from your mortal and immortal parents. You have a perfect physique, exotic features, and an air about you that captures the attention of everyone you meet.",
    ]

def roll_faun_appearance(dice_roll):
    return faun_appearance[bisect(faun_appearance_breakpoints, dice_roll)]


faun_background = {
    1: ("Hunters captured you and subjected you to horrific abuse. You escaped after murdering one or more of your captors.",'None'),
    2: ("You were a fool in an elf noble’s court and have known nothing but mockery and disdain your whole life.", 'None'),
    3: ("You spent several years as the prisoner of a wizard who believed your blood contained magical power.",  'None'),
    4: ("You fell in love with a human and had an affair that lasted for a few months before the tryst was exposed and you were chased off.", 'None'),
    5: ("Zealots of the New God descended on your village and slew everyone but you. Your attackers thought the village was full of beastmen.",  'None'),
    6: ("You were the plaything of a nymph for many years.",  'None'),
    7: ("You spent many years living alone in the wilderness.", 'None'),
    8: ("You had a small family in a remote corner of the Empire, but you lost them to disease or a monster attack.",  'None'),
    9: ("Poor treatment at faerie or human hands has left you scarred, mentally or physically, or both.",  'None'),
    10: ("You lived in a human settlement for many years and there learned your profession.",  'None'),
    11: ("A druid raised you from a baby, and you learned much of the Old Faith.",  'None'),
    12: ("You grew up in the house of your human parent, where you were loved.",  'None'),
    13: ("You are a second or third generation faun. You were raised in a remote part of the world, such as a deep forest or a high mountain vale.",  'None'),
    14: ("A troupe of performers took you in as a small child and raised you. You grew up facing the stares of the people who paid a few bits to see you.", 'None'),
    15: ("A wizard or witch found you and cared for you until you came of age.",  'None'),
    16: ("You worked as a spy for an inquisitor, who recently died.",  'None'),
    17: ("A wizard raised you and gave you a formal education. You can read the Common Tongue.",  'None'),
    18: ("You warned a human village of a monstrous threat. You are always welcome there.",  'None'),
    19: ("You befriended a leshy long ago, but you haven’t seen it in years.",  'None'),
    20: ("You found or stole a bag of coins. Add {} copper pennies to your starting equipment.",  "roll('2d6t')"),
}

def roll_faun_background(dice_roll):
    background, rand = faun_background[dice_roll]
    return background.format(eval(rand))


faun_personality_breakpoints = [4, 6, 9, 13, 16, 18]
faun_personality = [
    "You have known nothing but sorrow your whole life. It’s time to repay others for how they have treated you.",
    "The world is a cruel and unforgiving place. You do whatever you must to survive, even if that means stealing, cheating, or killing.",
    "You do and say what you please. You try not to hurt other people, but if it happens, there’s not much you can do about it.",
    "You survive by looking after yourself. You have a hard time trusting others or taking them at their word.",
    "You trust yourself to do what is right, even if others disagree with your tactics.",
    "You put your best foot forward. If you can prove your heart is good, maybe others will give you a chance.",
    "You were born for a reason, to accomplish some great task, to fulfill a great purpose. You hope to find your destiny and do what you were meant to do.",
    ]

def roll_faun_personality(dice_roll):
    return faun_personality[bisect(faun_personality_breakpoints, dice_roll)]


class Faun(Character):
    def __init__(self, s=None):
        super().__init__(s)
        self.ancestry = 'Faun'
        self.age = roll_faun_age(roll('3d6t'))
        self.build = roll_faun_build(roll('3d6t'))
        self.appearance = roll_faun_appearance(roll('3d6t'))
        self.background = roll_faun_background(roll('1d20t'))
        self.personality = roll_faun_personality(roll('3d6t'))

    def __str__(self):
        return (f"Age: {self.age}\nBuild: {self.build}\nAppearance: {self.appearance}\n"
                f"Background: {self.background}\nPersonality: {self.personality}\nFirst profession: "
                f"{self.professions[0]}\nSecond Profession: {self.professions[1]}\nInteresting Thing: "
                f"{self.interesting_thing}\nWealth: {self.wealth}\n\nSeed: {self.seed}")


    def __repr__(self):
        return f'Class: {self.ancestry}'


if __name__ == '__main__':
    pan = Faun('Pan')
    print(pan)
