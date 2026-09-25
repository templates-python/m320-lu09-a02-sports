from performance_record import PerformanceRecord


class Athlete:
    """ a member of a sports club """

    def __init__(self, name, report=None):
        if report is None:
            report = PerformanceRecord()
        self._name = name
        self._club = None
        self._performance_report = report
        self._performance_report.athlete = self

    @property
    def name(self):
        return self._name

    @property
    def club(self):
        return self._club

    @club.setter
    def club(self, club):
        self._club = club

    @property
    def report(self):
        return self._performance_report
