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
