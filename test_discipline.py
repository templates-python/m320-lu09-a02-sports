from datetime import datetime

import pytest

from discipline import Discipline
from result import Result


@pytest.fixture
def discipline():
    """ returns the discipline 'Sprint' """
    return Discipline('Sprint')


@pytest.fixture
def result():
    """ returns a result """
    return Result(8.0, '1.2.33')


def test_empty_discipline(discipline):
    """ tests the constructor without results """
    assert discipline.name == 'Sprint'
    assert discipline.count_results() == 0


def test_single_result_added(discipline):
    """ tests adding a single result"""
    discipline.add_result(Result(7.0, '1.2.33'))
    assert discipline.count_results() == 1


def test_multi_result_added(discipline):
    """ tests adding multiple results """
    discipline.add_result(Result(7.0, '1.2.33'))
    discipline.add_result(Result(8.0, '1.2.44'))
    discipline.add_result(Result(6.5, '1.2.55'))
    assert discipline.count_results() == 3


def test_too_many_results_added(discipline):
    """ tests adding too many results """
    discipline.add_result(Result(7.0, '1.2.11'))
    discipline.add_result(Result(8.0, '1.2.22'))
    discipline.add_result(Result(6.5, '1.2.33'))
    discipline.add_result(Result(9.0, '1.2.44'))
    discipline.add_result(Result(5.5, '1.2.55'))
    with pytest.raises(OverflowError):
        discipline.add_result(Result(4.0, '1.2.66'))
    assert discipline.count_results() == 5


def test_get_result_valid(discipline, result):
    """ tests reading a result with a valid index """
    discipline.add_result(result)
    assert discipline.take_result(0).value == result.value
    assert discipline.take_result(0).date == result.date


def test_get_result_invalid(discipline, result):
    """ tests reading a result with an invalid index """
    discipline.add_result(result)
    with pytest.raises(IndexError):
        discipline.take_result(1)


def test_multi_result(discipline):
    """ tests reading multiple results and their attributes """
    discipline.add_result(Result(7.0, '1.2.33'))
    discipline.add_result(Result(8.0, '1.2.44'))
    discipline.add_result(Result(6.5, '1.2.55'))
    assert discipline.take_result(0).value == 7.0
    assert discipline.take_result(1).value == 8.0
    assert discipline.take_result(2).value == 6.5
    assert discipline.take_result(0).date == datetime(2033, 2, 1)
    assert discipline.take_result(1).date == datetime(2044, 2, 1)
    assert discipline.take_result(2).date == datetime(2055, 2, 1)


def test_average_without_result(discipline):
    """ tests the average without any results """
    assert discipline.average == 0


def test_single_result_average(discipline):
    """ tests the average with a single result """
    discipline.add_result(Result(7.0, '1.2.33'))
    assert discipline.average == 7.0


def test_average(discipline):
    """ tests the average with multiple results """
    discipline.add_result(Result(6.0, '1.2.11'))
    discipline.add_result(Result(8.0, '1.2.22'))
    discipline.add_result(Result(7.0, '1.2.33'))
    discipline.add_result(Result(5.0, '1.2.44'))
    assert discipline.average == 6.5
