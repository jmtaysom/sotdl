# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 08:33:08 2018

@author: Jonathan Tross
"""

import pytest

from ancestry import halfling


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_halfling_age(test_input):
    result = halfling.roll_halfling_age(test_input)
    assert type(result) == str
    assert len(result) > 0
    

@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_halfling_build(test_input):
    result = halfling.roll_halfling_build(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_halfling_appearance(test_input):
    result = halfling.roll_halfling_appearance(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(1, 21)))
def test_roll_halfling_background(test_input):
    result = halfling.roll_halfling_background(test_input)
    assert type(result) == str
    assert len(result) > 0

 
@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_halfling_religion(test_input):
    result = halfling.roll_halfling_religion(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_halfling_personality(test_input):
    result = halfling.roll_halfling_personality(test_input)
    assert type(result) == str
    assert len(result) > 0    
    
def test_halfling():
    sam = halfling.Halfling('Sam')
    assert sam.age == 'You are an adolescent, 15 years old.'
    assert sam.build == 'You are normal height and weight for a halfling.'
    assert sam.appearance == 'Other halflings find you attractive, likely due to your winning personality.'
    assert sam.religion == 'You don’t believe the gods exist.'
    assert sam.background == 'Hard times forced you to make ends meet by committing crimes. Gain one criminal ' \
                             'profession.'
    assert sam.personality == 'Something is wrong with you. You dream about hurting people, cutting them up and ' \
                              'making them scream. You worry that you may one day act out on these fantasies.'
    assert sam.professions[0] == 'You are an academic of Magic'
    assert sam.professions[1] == 'You are a Hunter'
    assert sam.ancestry == 'Halfling'
    assert sam.wealth == 'Poor. You live in squalid conditions and you’re never sure where you’re going to get your ' \
                         'next meal.'
    assert sam.intersting_thing == 'A pet mouse, squirrel, or rabbit.'
