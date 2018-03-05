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


# def test_goblin():
#     gimli = goblin.goblin('Gimli')
#     assert gimli.age == 'You are a young adult, 48 years old.'
#     assert gimli.build == 'You are average in height and build.'
#     assert gimli.appearance == 'You take better care of yourself than most goblins and keep your facial hair well ' \
#                                'groomed.'
#     assert gimli.hatred == 'You hate elves'
#     assert gimli.background == 'You are the rightful heir to a stronghold overrun by the enemies of your people.'
#     assert gimli.personality == 'Your honor is your life. You would never do anything to bring shame to your people.'
#     assert gimli.professions[0] == 'You are a Pilgrim. You travel to sites deemed holy to members of your religion.'
#     assert gimli.professions[1] == 'You are a Marine'
#     assert gimli.ancestry == 'goblin'