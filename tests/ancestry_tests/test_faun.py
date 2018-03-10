# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 09:19:58 2018

@author: Jonathan Tross
"""


import pytest

from ancestry import faun


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_faun_age(test_input):
    result = faun.roll_faun_age(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_faun_build(test_input):
    result = faun.roll_faun_build(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_faun_appearance(test_input):
    result = faun.roll_faun_appearance(test_input)
    assert type(result) == str
    assert len(result) > 0
    

@pytest.mark.parametrize("test_input", list(range(1, 21)))
def test_roll_faun_background(test_input):
    result = faun.roll_faun_background(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_faun_personality(test_input):
    result = faun.roll_faun_personality(test_input)
    assert type(result) == str
    assert len(result) > 0


def test_faun():
    pan = faun.Faun('Pan')
    assert pan.age == 'You are a young adult, 24 years old.'
    assert pan.build == 'You have a typical height and weight for a faun'
    assert pan.appearance == 'You have an appealing appearance, such as a well-formed body, bright eyes, or warm ' \
                               'smile. Your appearance can put others more at ease.'
    assert pan.background == 'A wizard raised you and gave you a formal education. You can read the Common Tongue.'
    assert pan.personality == 'You put your best foot forward. If you can prove your heart is good, maybe others will' \
                              ' give you a chance.'
    assert pan.professions[0] == 'You are a Pilgrim. You travel to sites deemed holy to members of your religion.'
    assert pan.professions[1] == 'You are a Guide'
    assert pan.ancestry == 'Faun'
    assert pan.wealth == 'Poor. You live in squalid conditions and you’re never sure where you’re going to get your next meal.'
    assert pan.intersting_thing == 'A can of beets.'
