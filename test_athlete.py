import pytest

from athlete import Athlete
from performance_record import PerformanceRecord


@pytest.fixture
def athlete_record():
    """ returns a performance record """
    return PerformanceRecord()


@pytest.fixture
def nina(athlete_record):
    """ returns an athlete """
    return Athlete('Nina', athlete_record)


def test_initialisation(nina, athlete_record):
    """ tests the constructor """
    assert nina.name == 'Nina'
    assert nina.club is None
    assert nina.report is athlete_record


def test_relationship_to_record(nina, athlete_record):
    """ tests the reference between the athlete and the performance record """
    assert nina.report.athlete is nina


def test_default_record():
    """ tests that a default performance record is created when none is given """
    jon = Athlete('Jon')
    assert isinstance(jon.report, PerformanceRecord)
    assert jon.report.athlete is jon


def test_club_setter():
    """ tests that the club back-reference can be set """
    nina = Athlete('Nina')
    assert nina.club is None
    club = object()
    nina.club = club
    assert nina.club is club
