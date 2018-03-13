import pytest

from ancestry import human


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_human_personality(test_input):
    result = human.roll_human_personality(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_human_religion(test_input):
    result = human.roll_human_religion(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(1, 21)))
def test_roll_human_background(test_input):
    result = human.roll_human_background(test_input)
    assert type(result) == str
    assert len(result) > 0
    

@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_human_appearance(test_input):
    result = human.roll_human_appearance(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_human_age(test_input):
    result = human.roll_human_age(test_input)
    assert type(result) == str
    assert len(result) > 0


def test_human():
    john = human.Human('John')
    assert john.age == 'You are a young adult, 32 years old.'
    assert john.build == 'You are a bit overweight.'
    assert john.appearance == 'You have a physical quality that makes you attractive to others. You might have ' \
                              'pretty eyes, lips, hair, shape, or something else.'
    assert john.religion == 'You follow the tenets of the Old Faith.'
    assert john.background == 'The faerie held you prisoner for 7 years.'
    assert john.personality == 'You look after yourself first and foremost. You’re not above double-crossing friends.'
    assert john.professions[0] == 'You are a Musician. Choose an instrument. Examples include percussion, string, ' \
                                  'and wind.'
    assert john.professions[1] == 'You are a Patroller'
    assert john.ancestry == 'Human'
    assert john.wealth == 'Getting By. You earn enough to meet all your expenses.'
    assert john.interesting_thing == 'A box containing 7 brushes.'
