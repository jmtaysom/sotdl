import pytest

from ancestry import goblin


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_goblin_personality(test_input):
    result = goblin.roll_goblin_personality(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_goblin_build(test_input):
    result = goblin.roll_goblin_build(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(1, 21)))
def test_roll_goblin_background(test_input):
    result = goblin.roll_goblin_background(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(1, 21)))
def test_roll_goblin_appearance(test_input):
    result = goblin.roll_goblin_appearance(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_goblin_age(test_input):
    result = goblin.roll_goblin_age(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(1, 21)))
def test_roll_goblin_odd_habbit(test_input):
    result = goblin.roll_goblin_odd_habit(test_input)
    assert type(result) == str
    assert len(result) > 0


def test_goblin():
    warwick = goblin.Goblin('Warwick')
    assert warwick.age == 'You are an adolescent, 9 years old.'
    assert warwick.build == 'You fall within the normal height and weight ranges for goblins.'
    assert warwick.appearance == 'You have all the warts.'
    assert warwick.odd_habit == 'You never bathe.'
    assert warwick.background == 'You earned a living working in your profession.'
    assert warwick.personality == 'You love playing tricks on other people and find their pain hilarious!'
    assert warwick.professions[0] == 'You are a Thug'
    assert warwick.professions[1] == 'You are a Musician. Choose an instrument. Examples include percussion, string, and wind.'
    assert warwick.ancestry == 'Goblin'
    assert warwick.wealth == 'Poor. You live in squalid conditions and you’re never sure where you’re going to get ' \
                             'your next meal.'
