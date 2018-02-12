import pytest

from ancestry import human


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_human_personality(test_input):
    assert type(human.roll_human_personality(test_input)) == str


@pytest.mark.parametrize("test_input", list(range(3, 19)))
def test_roll_human_religion(test_input):
    assert type(human.roll_human_religion(test_input)) == str


@pytest.mark.parametrize("test_input", list(range(1, 21)))
def test_roll_human_background(test_input):
    assert type(human.roll_human_background(test_input)) == str