from random import seed
import pytest

from ancestry import orc


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_orc_personality(test_input):
    result = orc.roll_orc_personality(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_orc_build(test_input):
    result = orc.roll_orc_build(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(1, 21)))
def test_roll_orc_background(test_input):
    result = orc.roll_orc_background(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_orc_appearance(test_input):
    result = orc.roll_orc_appearance(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_orc_age(test_input):
    result = orc.roll_orc_age(test_input)
    assert type(result) == str
    assert len(result) > 0



def test_orc_children():
    result = orc.orc_children()
    assert result[0] >= result[1] >= 0


def test_orc():
    azog = orc.Orc('Azog')
    assert azog.age == 'You are a young adult, 13 years old.'
    assert azog.build == 'You are thin.'
    assert azog.appearance == 'You are grotesque. Your face is a mass of scar tissue. Thick scars crisscross your ' \
                              'body, held together with excrement, blood, and rot. Swaths of open sores weep streams ' \
                              'of pus, and you reek ofcrude, leather stitching.'
    assert azog.background == 'You received an education. You know how to read the Common Tongue.'
    assert azog.personality == 'You never question orders. You always do as you’re commanded.'
    assert azog.professions[0] == 'You are a Patroller'
    assert azog.professions[1] == 'You are a Initiate of the Old Faith. You have been initiated into the Old Faith.'
    assert azog.intersting_thing == 'A brace of conies or pack filled with pots and pans.'
    assert azog.ancestry == 'Orc'
    assert azog.wealth == 'Poor. You live in squalid conditions and you’re never sure where you’re going to get your ' \
                          'next meal.'