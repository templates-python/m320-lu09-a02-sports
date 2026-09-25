MAX_ATHLETES = 25


class Club:
    """ a sports club that manages its athletes """

    def __init__(self, designation):
        self._designation = designation
        self._athletes = []

    @property
    def designation(self):
        return self._designation

    def add_athlete(self, athlete):
        """ adds an athlete, raises OverflowError if the maximum is reached """
        if len(self._athletes) >= MAX_ATHLETES:
            raise OverflowError(f'a club can only hold {MAX_ATHLETES} athletes')
        athlete.club = self
        self._athletes.append(athlete)

    def count_athletes(self):
        """ returns the number of athletes """
        return len(self._athletes)

    def take_athlete(self, index):
        """ returns the athlete at the given index, raises IndexError if invalid """
        if not 0 <= index < len(self._athletes):
            raise IndexError('no athlete at this index')
        return self._athletes[index]

    def remove_athlete(self, index):
        """ removes the athlete at the given index, raises IndexError if invalid """
        if not 0 <= index < len(self._athletes):
            raise IndexError('no athlete at this index')
        athlete = self._athletes.pop(index)
        athlete.club = None

    def show_athlete_list(self):
        """ returns the names of all athletes, one per line """
        return ''.join(f'{athlete.name}\n' for athlete in self._athletes)

    def show_athlete_report(self, name):
        """ returns the performance overview of the athlete with the given name """
        for athlete in self._athletes:
            if athlete.name == name:
                return f'Leistungsausweis für: {name}\n{athlete.report.show_overview()}'
        return f'Athlet {name} nicht gefunden'
