# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 11:16:33 2018

@author: Jonathan Tross
"""

import pytest

from ancestry import changeling


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_changeling_true_age(test_input):
    result = changeling.roll_changeling_true_age(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(1, 7)))
def test_roll_changeling_appearent_gender(test_input):
    result = changeling.roll_changeling_appearent_gender(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_changeling_appearent_ancestry(test_input):
    result = changeling.roll_changeling_appearent_ancestry(test_input)
    assert type(result) == tuple
    assert len(result) == 4
    for apparent in result:
        assert type(apparent) == str
    

@pytest.mark.parametrize("test_input", list(range(1, 21)))
def test_roll_changeling_background(test_input):
    result = changeling.roll_changeling_background(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_changeling_personality(test_input):
    result = changeling.roll_changeling_personality(test_input)
    assert type(result) == str
    assert len(result) > 0
    
@pytest.mark.parametrize("test_input", list(range(1, 21)))
def test_roll_changeling_quirk(test_input):
    result = changeling.roll_changeling_quirk(test_input)
    assert type(result) == str
    assert len(result) > 0
