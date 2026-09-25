import pytest

from discipline import Discipline
from performance_record import PerformanceRecord


@pytest.fixture
def discipline_list():
    """ returns a list of disciplines """
    return [Discipline('Sprint'), Discipline('Weitsprung'), Discipline('Kugelstoss')]


@pytest.fixture
def record_empty():
    """ returns an empty performance record """
    return PerformanceRecord()


@pytest.fixture
def record_max_disciplines(record_empty: PerformanceRecord, discipline_list):
    """ returns a performance record with the maximum number of disciplines """
    for discipline in discipline_list:
        record_empty.add_discipline(discipline)
    return record_empty


def test_empty_record(record_empty):
    """ tests the constructor with an empty performance record """
    assert record_empty.count_disciplines() == 0
    assert record_empty.athlete is None


def test_add_discipline(record_empty):
    """ tests adding a single discipline """
    record_empty.add_discipline(Discipline('Sprint'))
    assert record_empty.count_disciplines() == 1


def test_add_multiple_disciplines(record_max_disciplines, discipline_list):
    """ tests adding multiple disciplines """
    assert record_max_disciplines.count_disciplines() == 3
    names = {record_max_disciplines.take_discipline(i).name for i in range(3)}
    assert names == {d.name for d in discipline_list}


def test_max_disciplines(record_max_disciplines):
    """ tests adding too many disciplines """
    record_max_disciplines.add_discipline(Discipline('Hochsprung'))
    with pytest.raises(OverflowError):
        record_max_disciplines.add_discipline(Discipline('too many disciplines'))
    assert record_max_disciplines.count_disciplines() == 4


def test_take_valid(record_max_disciplines):
    """ tests reading a discipline with a valid index """
    discipline = record_max_disciplines.take_discipline(1)
    assert discipline.name == 'Weitsprung'


def test_take_invalid(record_empty):
    """ tests reading a discipline with an invalid index """
    record_empty.add_discipline(Discipline('Sprint'))
    with pytest.raises(IndexError):
        record_empty.take_discipline(2)
