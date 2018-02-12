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
