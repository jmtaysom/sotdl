# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 03:52:46 2018

@author: Jonathan Tross
"""

from bisect import bisect
from dice import roll


interesting_things_table1 = {
    1: ("A tiny metal box with no opening that makes a faint ticking noise.",  'None'),
    2: ("A skull made from clear crystal.",  'None'),
    3: ("A glass ball filled with water in which swims a tiny living goldfish.",  'None'),
    4: ("A curious odor, a pungent stench, or a skin condition that never quite heals.",  'None'),
    5: ("A bottle filled with a maiden’s tears.",  'None'),
    6: ("A flower that never withers.",  'None'),
    7: ("A small magnet or silver mirror.",  'None'),
    8: ("An invitation to a party or a masquerade mask.",  'None'),
    9: ("A monogrammed handkerchief that always stays clean.",  'None'),
    10: ("A folding knife that always stays sharp.",  'None'),
    11: ("A pair of dancing shoes.",  'None'),
    12: ("A tiny inert mechanical spider.",  'None'),
    13: ("A shrunken head.",  'None'),
    14: ("A glass eye or a bezoar.",  'None'),
    15: ("A book written in an unknown language or a book containing things you never wanted to know.",  'None'),
    16: ("A deck of fortune-teller’s cards.",  'None'),
    17: ("A pair of loaded dice.",  'None'),
    18: ("Six small cakes that can nourish the person who eats one until the next day at dawn.",  'None'),
    19: ("A phylactery that holds a scrap of paper on which is written a single word.",  'None'),
    20: ("A reputation for being a badass.",  'None'),
}


def roll_interesting_things_table1(dice_roll):
    table1, rand = interesting_things_table1[dice_roll]
    return table1.format(eval(rand))


interesting_things_table2 = {
    1: ("A flute or set of panpipes, or other musical instrument.",  'None'),
    2: ("A reliquary containing a small bone.",  'None'),
    3: ("A tiny idol of a demon carved from green stone.",  'None'),
    4: ("A token from an admirer or lover.",  'None'),
    5: ("A pet mouse, squirrel, or rabbit.",  'None'),
    6: ("A monocle or pair of heavy goggles.",  'None'),
    7: ("A silver necklace with a medallion.",  'None'),
    8: ("A snuffbox filled with snuff.",  'None'),
    9: ("A gleaming dragon’s scale.",  'None'),
    10: ("A fist-sized egg covered in blue spots.",  'None'),
    11: ("Unrequited love.",  'None'),
    12: ("A black iron cauldron filled with bones.",  'None'),
    13: ("A box of 1d20 iron nails.",  'None'),
    14: ("A vial of sweet perfume or a bottle of rotgut.",  'None'),
    15: ("A feather made from bronze.",  'None'),
    16: ("An iron coin with a scratch on one side or a steel coin with a dragon’s head on either side.",  'None'),
    17: ("A box containing {} brushes.",  "roll('1d6+1')"),
    18: ("A bloodstained doll.",  'None'),
    19: ("A silver engagement ring worth 1 ss.",  'None'),
    20: ("A brush, comb, or umbrella.",  'None'),
}


def roll_interesting_things_table2(dice_roll):
    table2, rand = interesting_things_table2[dice_roll]
    return table2.format(eval(rand))


def teeth_ears_heads():
    teeth = roll('3d6t')
    ears = roll('1d6t')
    heads= roll('1d6t')
    return (teeth, ears, heads)


interesting_things_table3 = {
    1: ("A bar of soap or a towel.",  'None'),
    2: ("One hundred feet of twine wrapped up in a ball.",  'None'),
    3: ("A tiny portrait, a lock of hair, or some other favor from someone who loves you.",  'None'),
    4: ("A small keg of beer.",  'None'),
    5: ("A brace of conies or pack filled with pots and pans.",  'None'),
    6: ("An arrow or bolt with a silvered head.",  'None'),
    7: ("Half a treasure map, a map of a foreign land, or a large, blue map covered with circles with weird bits of writing between them.",  'None'),
    8: ("A weapon of the GM’s choice.",  'None'),
    9: ("A light or heavy shield with an unusual heraldic device.",  'None'),
    10: ("A fancy set of clothes bearing a curious stain.",  'None'),
    11: ("A personal servant.",  'None'),
    12: ("A silver holy symbol or a fine religious icon.",  'None'),
    13: ("A bag of {} rocks, acorns, severed heads, or yummy mushrooms.",  "roll('2d6t')"),
    14: ("A music box that plays a sad, sad song when opened.",  'None'),
    15: ("A bag of 100 marbles.",  'None'),
    16: ("A glass jar filled with saliva, a sack filled with rotting chicken parts, or an unseemly scar.",  'None'),
    17: ("A small bag containing {} teeth, a necklace of {} ears, or {} severed heads tied together by their hair.", teeth_ears_heads()),
    18: ("A newborn baby that might or might not be yours.",  'None'),
    19: ("A box of six fine white candles.",  'None'),
    20: ("A small dog with a tendency toward viciousness.",  'None'),
}


def roll_interesting_things_table3(dice_roll):
    table3, rand = interesting_things_table3[dice_roll]
    return table3.format(*rand)


interesting_things_table4 = {
    1: ("A glass jar holding a beetle covered in glowing spots (sheds light as a candle).",  'None'),
    2: ("A pair of boots that grants you 1 boon on rolls to sneak or a gray cloak that grants you 1 boon on rolls to hide.",  'None'),
    3: ("A glass jar containing a strange organ suspended in alcohol.",  'None'),
    4: ("A tiny glass cage.",  'None'),
    5: ("A box containing {} bottles of ink, each a different color.",  "roll('1d6t')"),
    6: ("A tiny inert mechanical owl.",  'None'),
    7: ("A length of rope, 20 yards long, that cannot be cut.",  'None'),
    8: ("A badge from a mercenary company.",  'None'),
    9: ("A box of cigars or a pipe and pouch of tobacco.",  'None'),
    10: ("A medallion depicting a hideous woman’s face.",  'None'),
    11: ("A spiked collar, skin clamps, and a scourge.",  'None'),
    12: ("A ten-pound bag of flour.",  'None'),
    13: ("A bronze plate with a name scratched on its face.",  'None'),
    14: ("A crystal bottle containing fluid that emits light in a 2-yard radius when the stopper is removed.",  'None'),
    15: ("A small box holding six sticks of chalk.",  'None'),
    16: ("A letter of introduction from a powerful and influential person.",  'None'),
    17: ("A mirror fragment that shows a strange location on its reflective surface.",  'None'),
    18: ("A small golden cage containing a living faerie that cannot talk.",  'None'),
    19: ("A bottle labeled “Eye of Newt.”",  'None'),
    20: ("A bag of beans.",  'None'),
}


def roll_interesting_things_table4(dice_roll):
    table4, rand = interesting_things_table4[dice_roll]
    return table4.format(eval(rand))


interesting_things_table5 = {
    1: ("A jar of grease or a bottle of glue.",  'None'),
    2: ("A glass globe filled with swirling mist.",  'None'),
    3: ("A cloak with {} pockets hidden in the lining.",  "roll('2d20t')"),
    4: ("A pair of spectacles that sometimes let you see through up to 1 inch of solid rock.",  'None'),
    5: ("A small blue box that’s bigger on the inside (twice normal capacity).",  'None'),
    6: ("A small steel ball.",  'None'),
    7: ("A petrified hand that twitches in the light of a full moon.",  'None'),
    8: ("The true name of a very minor devil.",  'None'),
    9: ("An animated mouse skeleton.",  'None'),
    10: ("A weapon of the GM’s choice that always emits light in a 1-yard radius.",  'None'),
    11: ("A pouch that holds {} pinches of dust that, when sprinkled over stone, causes up to a 1-yard cube of material to become soft clay.",  "roll('1d6+1')"),
    12: ("A jar of paint that refills itself once each day at dawn.",  'None'),
    13: ("A tiny metal ball that when released floats 1 inch above any solid surface.",  'None'),
    14: ("A pouch holding {} pinches of diamond dust.",  "roll('1d6+1')"),
    15: ("A brain in a jar.",  'None'),
    16: ("A bag filled with curiously fleshy rods.",  'None'),
    17: ("A mace made from purple metal with a name etched on the haft.",  'None'),
    18: ("A giant piece of charcoal that radiates menace.",  'None'),
    19: ("A piece of amber containing a human-faced fly.",  'None'),
    20: ("A lifetime of regrets.",  'None'),
}


def roll_interesting_things_table5(dice_roll):
    table5, rand = interesting_things_table5[dice_roll]
    return table5.format(eval(rand))


interesting_things_table6 = {
    1: ("A reputation for being a skilled lover.",  'None'),
    2: ("A mummified halfling.",  'None'),
    3: ("A set of clothing that can change appearance once each day at dusk.",  'None'),
    4: ("A can of beets.",  'None'),
    5: ("A stalker who follows you but flees when you approach.",  'None'),
    6: ("A shameful past.",  'None'),
    7: ("A recurring and disturbing dream.",  'None'),
    8: ("A trunk filled with body parts.",  'None'),
    9: ("A wagon or cart pulled by a sad donkey.",  'None'),
    10: ("Three small white mice that whisper strange things to you while you sleep.",  'None'),
    11: ("A tremor, a facial tic, or an irritating laugh.",  'None'),
    12: ("A thermometer.",  'None'),
    13: ("A collapsible pole, 3 yards long.",  'None'),
    14: ("A shadow you cast that never quite matches your movements.",  'None'),
    15: ("Fear and loathing.",  'None'),
    16: ("A fondness for the bottle.",  'None'),
    17: ("A thin shirt of mail that counts as light armor and can be worn under normal clothing (functions as mail and is not cumulative with other armor).",  'None'),
    18: ("A bizarre fetish.",  'None'),
    19: ("A demanding spouse.",  'None'),
    20: ("A terrible secret that you dare not reveal.",  'None'),
}


def roll_interesting_things_table6(dice_roll):
    table6, rand = interesting_things_table6[dice_roll]
    return table6.format(eval(rand))


interesting_things_tables = {
    1: print(roll_interesting_things_table1(roll('1d20t'))),
    2: print(roll_interesting_things_table2(roll('1d20t'))),
    3: print(roll_interesting_things_table3(roll('1d20t'))),
    4: print(roll_interesting_things_table4(roll('1d20t'))),
    5: print(roll_interesting_things_table5(roll('1d20t'))),
    6: print(roll_interesting_things_table6(roll('1d20t'))),
}


def roll_interesting_things_tables(dice_roll):
    tables, rand = interesting_things_tables[dice_roll]
    return tables.format(*rand)


def roll_interesting_things():
     print(roll_interesting_things_tables(roll('1d6t'))),

    
if __name__ == '__main__':
    roll_interesting_things()