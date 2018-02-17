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