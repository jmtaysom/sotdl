import pytest

from ancestry import interesting_things


@pytest.mark.parametrize("test_input", [(one, two) for one in range(1, 7) for two in range(1, 21)])
def test_roll_interesting_thing(test_input):
    thing = interesting_things.roll_interesting_thing(*test_input)
    assert type(thing) == str
    assert len(thing) > 0
