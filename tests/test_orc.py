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


# def test_orc():
#     gimli = orc.orc('Gimli')
#     assert gimli.age == 'You are a young adult, 48 years old.'
#     assert gimli.build == 'You are average in height and build.'
#     assert gimli.appearance == 'You take better care of yourself than most orcs and keep your facial hair well ' \
#                                'groomed.'
#     assert gimli.hatred == 'You hate elves'
#     assert gimli.background == 'You are the rightful heir to a stronghold overrun by the enemies of your people.'
#     assert gimli.personality == 'Your honor is your life. You would never do anything to bring shame to your people.'
#     assert gimli.professions[0] == 'You are a Pilgrim. You travel to sites deemed holy to members of your religion.'
#     assert gimli.professions[1] == 'You are a Marine'
#     assert gimli.ancestry == 'orc'