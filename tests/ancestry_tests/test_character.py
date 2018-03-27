import pytest

from ancestry import character


@pytest.mark.parametrize("test_input", [(one, two) for one in range(1, 7) for two in range(1, 21)])
def test_roll_profession(test_input):
    profession = character.roll_profession(*test_input)
    assert type(profession) == str
    assert len(profession) > 0

def test_seed_permanence():
    char1 = character.Character()
    char2 = character.Character(char1.seed)
    assert char1.seed == char2.seed
    assert repr(char1) == repr(char2)
