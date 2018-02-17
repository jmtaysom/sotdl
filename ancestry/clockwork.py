# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 20:05:40 2018

@author: Jonathan Tross
"""

from bisect import bisect
from dice import roll

clockwork_ages_breakpoints = [9, 13, 16, 18]
clockwork_ages = [
    ("You are new, 5 years old or younger.",'None'),
    ("You are experienced, {} years old.", 'roll("1d5+5")'),
    ("You are old, {} years old.", 'roll("1d40+10")'),
    ("You are very old, {} years old.", 'roll("1d100+50")'),
    ("You are ancient, more than 150 years old.", 'None'),
    ]

def roll_clockwork_age(dice_roll):
    age, rand = clockwork_ages[bisect(clockwork_ages_breakpoints, dice_roll)]
    return age.format(eval(rand))

clockwork_purpose_breakpoints = [5, 9, 13, 17]
clockwork_purpose = [
    "You were built for war. Increase your Strength or Agility by 2.",
    "You were built to work. Increase your Strength by 2.",
    "You were built to use magic. Increase your Intellect or Will by 2.",
    "You were built to gather intelligence about or assassinate targets. Increase your Agility or Intellect by 2.",
    "You were built for an inexplicable purpose. Increase one attribute of your choice by 2.",
    ]

def roll_clockwork_purpose(dice_roll):
    return clockwork_purpose[bisect(clockwork_purpose_breakpoints, dice_roll)]


clockwork_form_breakpoints = [4, 6, 10, 16, 18]
clockwork_form = [
    "You are a small winged clockwork. Reduce your Health by 5 and your Size to 1/2. You can fly, but you must land at the end of your movement or fall. You are 3 feet tall and weigh 50 pounds.",
    "You are a small spider-like clockwork with functional hands. Reduce your Size to 1/2. You ignore the effects of difficult terrain when you climb. You are 3 feet tall and weigh 50 pounds.",
    "You are a small humanoid clockwork. Reduce your Size to 1/2. You are 4 feet tall and weigh 75 pounds.",
    "You are a humanoid clockwork. You are 6 feet tall and weigh 300 pounds.",
    "You are a large humanoid clockwork. Increase your Size to 2, but reduce your Speed and your Defense by 2. You are 10 feet tall and weigh 750 pounds.",
    "You are a large clockwork with the lower body of a horse. Increase your Size to 2 and your Speed by 2. Reduce your Defense by 3. You are 6 feet long, 6 feet tall, and weigh 750 pounds.",
    ]

def roll_clockwork_form(dice_roll):
    return clockwork_form[bisect(clockwork_form_breakpoints, dice_roll)]


clockwork_appearance_breakpoints = [4, 5, 7, 9, 13, 15, 17, 18] 
clockwork_appearance = [
    ("You have a strange and unsettling appearance.",'None'),
    ("You appear crude and ill-formed.",'None'),
    ("You appear battered, broken, and in poor repair.",'None'),
    ("You have no facial features or distinguishing markings.",'None'),
    ("You have a mere suggestion of facial features.",'None'),
    ("You appear well made and in good working condition.",'None'),
    ("You have a stylized and ornate body.",'None'),
    ("You have an ornate body festooned with etchings and ornamental jewels.",'None'),
    ("You have an exquisite body festooned with elaborate etchings and ornamental jewels, and trimmed in precious metals. If you are dismantled, your body parts are worth {} gc.", 'roll("1d6t")'),
    ]

def roll_clockwork_appearance(dice_roll):
    appearance, rand = clockwork_appearance[bisect(clockwork_appearance_breakpoints, dice_roll)]
    return appearance.format(eval(rand))


clockwork_background = {
    1: ("Your soul came from Hell. Start the game with {} Corruption.", "roll('1d3t')"),
    2: ("Your soul was plucked from the Underworld before it could forget its former life. Start the game with {} Insanity and add an extra profession.", "roll('1d6t')"),
    3: ("You spent {} years in a dormant state.", "roll('1d20t')"),
    4: ("Your maker treated you poorly. You escaped and now fear your maker will find you.", 'None'),
    5: ("Fire, plague, or monsters destroyed your home and you are the sole survivor.",  'None'),
    6: ("You were stolen from the workshop where you were made and lived as a slave for {} years.",  "roll('1d6t')"),
    7: ("Goblins captured you and almost took you apart for scrap materials. You have replaced your missing components with bits of wood, old weapons, and other rubbish.", 'None'),
    8: ("You were left to find your own way in the world when your maker died.",  'None'),
    9: ("You fell off a boat and spent 2 years walking to shore.",  'None'),
    10: ("You worked to fulfill your purpose for {} years.",  "roll('1d6t')"),
    11: ("Choose a member of the group. That character found you and turned your key. You owe that character a debt.",  'None'),
    12: ("You were one of {} other clockworks made at the same time. You hope to find them one day.",  "roll('1d6t')"),
    13: ("You were made to be a translator. You can speak one additional language.",  'None'),
    14: ("You were made to be a scribe. You know how to read and write the Common Tongue.", 'None'),
    15: ("Your maker set you free to find your destiny.",  'None'),
    16: ("You can’t remember your past. You don’t know where you came from or how you came to be where you are.",  'None'),
    17: ("You built a lasting monument in your community.",  'None'),
    18: ("You found a cryptic message inside your body. You have not yet deciphered its meaning.",  'None'),
    19: ("You have a sword grafted to one of your arms.",  'None'),
    20: ("You came into money and start the game with {} cp.",  "roll('2d6t')"),
}


def roll_clockwork_background(dice_roll):
    background, rand = clockwork_background[dice_roll]
    return background.format(eval(rand))


clockwork_personality_breakpoints = [4, 5, 8, 9, 14, 15, 16, 18]
clockwork_personality = [
    "You hate living things and take pleasure in pulling them apart.",
    "You are terrified of becoming dormant.",
    "Your body gives you power and strength. You use it to enforce your will on others.",
    "You didn’t ask for this existence, but you make the most of it while you have it.",
    "You search for meaning in a world in which you have no place.",
    "You were made to serve. You commit your existence to aiding others.",
    "You don’t know how you fit into this world, but you will spend your life trying to find out.",
    "You obey the instructions of anyone you deem to be an authority.",
    "Your maker gave you three commandments and you must obey them.",
    ]

def roll_clockwork_personality(dice_roll):
    return clockwork_personality[bisect(clockwork_personality_breakpoints, dice_roll)]


def roll_clockwork():
    print(roll_clockwork_background(roll('1d20t')))
    print(roll_clockwork_purpose(roll('1d20t')))
    print(roll_clockwork_form(roll('3d6t')))
    print(roll_clockwork_appearance(roll('3d6t')))
    print(roll_clockwork_age(roll('3d6t')))
    print(roll_clockwork_personality(roll('3d6t')))
    
    
if __name__ == '__main__':
    roll_clockwork()


