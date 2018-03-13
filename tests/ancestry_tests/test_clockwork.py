# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 21:36:18 2018

@author: Jonathan Tross
"""

import pytest

from ancestry import clockwork


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_clockwork_personality(test_input):
    result = clockwork.roll_clockwork_personality(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_clockwork_form(test_input):
    result = clockwork.roll_clockwork_form(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(1, 21)))
def test_roll_clockwork_background(test_input):
    result = clockwork.roll_clockwork_background(test_input)
    assert type(result) == str
    assert len(result) > 0
    

@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_clockwork_appearance(test_input):
    result = clockwork.roll_clockwork_appearance(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_clockwork_age(test_input):
    result = clockwork.roll_clockwork_age(test_input)
    assert type(result) == str
    assert len(result) > 0
    

@pytest.mark.parametrize("test_input", list(range(1, 21)))
def test_roll_clockwork_purpose(test_input):
    result = clockwork.roll_clockwork_purpose(test_input)
    assert type(result) == str
    assert len(result) > 0
    

def test_clockwork():
    cogsworth = clockwork.Clockwork('Cogsworth')
    assert cogsworth.age == 'You are experienced, 9 years old.'
    assert cogsworth.form == 'You are a small humanoid clockwork. Reduce your Size to 1/2. You are 4 feet tall and ' \
                             'weigh 75 pounds.'
    assert cogsworth.appearance == 'You have a mere suggestion of facial features.'
    assert cogsworth.purpose == 'You were built to gather intelligence about or assassinate targets. Increase your ' \
                                'Agility or Intellect by 2.'
    assert cogsworth.background == 'You fell off a boat and spent 2 years walking to shore.'
    assert cogsworth.personality == 'You search for meaning in a world in which you have no place.'
    assert cogsworth.professions[0] == 'You are a Exile'
    assert cogsworth.professions[1] == 'You are a Informant'
    assert cogsworth.ancestry == 'Clockwork'
    assert cogsworth.wealth == 'Getting By. You earn enough to meet all your expenses.'
    assert cogsworth.interesting_thing == 'A fancy set of clothes bearing a curious stain.'
