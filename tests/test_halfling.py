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