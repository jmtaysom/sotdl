import pytest

from ancestry import dwarf


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_dwarf_personality(test_input):
    result = dwarf.roll_dwarf_personality(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_dwarf_build(test_input):
    result = dwarf.roll_dwarf_build(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(1, 21)))
def test_roll_dwarf_background(test_input):
    result = dwarf.roll_dwarf_background(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_dwarf_appearance(test_input):
    result = dwarf.roll_dwarf_appearance(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_dwarf_age(test_input):
    result = dwarf.roll_dwarf_age(test_input)
    assert type(result) == str
    assert len(result) > 0


@pytest.mark.parametrize("test_input", list(range(1, 11)))
def test_roll_dwarf_hatred(test_input):
    result = dwarf.roll_dwarf_hatred(test_input)
    assert type(result) == str
    assert len(result) > 0


def test_dwarf():
    gimli = dwarf.Dwarf('Gimli')
    assert gimli.age == 'You are a young adult, 48 years old.'
    assert gimli.build == 'You are average in height and build.'
    assert gimli.appearance == 'You take better care of yourself than most dwarfs and keep your facial hair well ' \
                               'groomed.'
    assert gimli.hatred == 'You hate elves'
    assert gimli.background == 'You are the rightful heir to a stronghold overrun by the enemies of your people.'
    assert gimli.personality == 'Your honor is your life. You would never do anything to bring shame to your people.'
    assert gimli.professions[0] == 'You are a Pilgrim. You travel to sites deemed holy to members of your religion.'
    assert gimli.professions[1] == 'You are a Marine'
    assert gimli.ancestry == 'Dwarf'
    assert gimli.wealth == 'Getting By. You earn enough to meet all your expenses.'
    assert gimli.interesting_thing == 'A small dog with a tendency toward viciousness.'
