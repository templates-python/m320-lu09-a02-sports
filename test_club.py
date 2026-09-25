import pytest

from athlete import Athlete
from club import Club
from performance_record import PerformanceRecord


@pytest.fixture
def a_club():
    return Club('LC Zürisee')


@pytest.fixture
def a_record():
    return PerformanceRecord()


def test_club_init(a_club):
    """ tests the constructor """
    assert a_club.designation == 'LC Zürisee'
    assert a_club.count_athletes() == 0


def test_single_athlete_added(a_club, a_record):
    """ tests adding a single athlete """
    peter = Athlete('Peter', a_record)
    a_club.add_athlete(peter)
    assert a_club.take_athlete(0) is peter
    assert peter.club is a_club


def test_take_invalid_athlete(a_club, a_record):
    """ tests reading an athlete with an invalid index """
    peter = Athlete('Peter', a_record)
    a_club.add_athlete(peter)
    with pytest.raises(IndexError):
        a_club.take_athlete(3)


def test_multi_athlete_added(a_club, a_record):
    """ tests adding multiple athletes """
    for idx in range(4):
        a_club.add_athlete(Athlete('A', a_record))
    assert a_club.count_athletes() == 4


def test_too_many_athletes_added(a_club, a_record):
    """ tests adding more than 25 athletes """
    for idx in range(25):
        a_club.add_athlete(Athlete('A', a_record))
    with pytest.raises(OverflowError):
        a_club.add_athlete(Athlete('B', a_record))
    assert a_club.count_athletes() == 25


def test_athlete_list(a_club, a_record):
    """ tests showing the list of all athletes in a club """
    a_club.add_athlete(Athlete('Max', a_record))
    a_club.add_athlete(Athlete('Mia', a_record))
    a_club.add_athlete(Athlete('Cem', a_record))
    a_club.add_athlete(Athlete('Ali', a_record))
    output = a_club.show_athlete_list()
    assert output == 'Max\nMia\nCem\nAli\n'


def test_athlete_report_not_found(a_club, a_record):
    """ tests showing the report of an unknown athlete """
    a_club.add_athlete(Athlete('Max', a_record))
    output = a_club.show_athlete_report('Theo')
    assert output == 'Athlet Theo nicht gefunden'


def test_remove_athlete(a_club, a_record):
    """ tests removing an athlete and clearing its club back-reference """
    max_ = Athlete('Max', a_record)
    mia = Athlete('Mia', a_record)
    a_club.add_athlete(max_)
    a_club.add_athlete(mia)
    a_club.remove_athlete(0)
    assert a_club.count_athletes() == 1
    assert a_club.take_athlete(0) is mia
    assert max_.club is None


def test_remove_invalid_athlete(a_club, a_record):
    """ tests removing an athlete with an invalid index """
    a_club.add_athlete(Athlete('Max', a_record))
    with pytest.raises(IndexError):
        a_club.remove_athlete(3)
