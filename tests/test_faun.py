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

