from datetime import datetime

import pytest

from result import Result


@pytest.fixture
def some_date():
    """ returns a date """
    return datetime(2024, 8, 28)


def test_result_init_valid(some_date):
    """ tests the constructor with valid data """
    result = Result(8.0, some_date)
    assert result.value == 8.0
    result = Result(0.0, some_date)
    assert result.value == 0.0
    result = Result(10.0, some_date)
    assert result.value == 10.0


def test_result_init_invalid(some_date):
    """ tests the constructor with invalid data """
    with pytest.raises(TypeError):
        Result('a', some_date)


def test_result_init_too_small(some_date):
    """ tests the constructor with an illegal value """
    with pytest.raises(ValueError):
        Result(-0.5, some_date)


def test_result_init_too_high(some_date):
    """ tests the constructor with an illegal value """
    with pytest.raises(ValueError):
        Result(10.5, some_date)


def test_result_date_as_string():
    """ tests that a date given as a string is converted """
    result = Result(7.5, '24.8.24')
    assert result.date == datetime(2024, 8, 24)


def test_result_date_default():
    """ tests that a missing date defaults to now """
    before = datetime.now()
    result = Result(7.5)
    after = datetime.now()
    assert before <= result.date <= after


def test_result_value_setter(some_date):
    """ tests that the value setter validates on reassignment """
    result = Result(7.5, some_date)
    result.value = 9.0
    assert result.value == 9.0
    with pytest.raises(ValueError):
        result.value = 11.0
