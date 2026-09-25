MAX_DISCIPLINES = 4


class PerformanceRecord:
    """ the performance record (Leistungsausweis) of a single athlete """

    def __init__(self):
        self._disciplines = []
        self._athlete = None

    @property
    def athlete(self):
        return self._athlete

    @athlete.setter
    def athlete(self, athlete):
        self._athlete = athlete

    def add_discipline(self, discipline):
        """ adds a discipline, raises OverflowError if the maximum is reached """
        if len(self._disciplines) >= MAX_DISCIPLINES:
            raise OverflowError(f'a performance record can only hold {MAX_DISCIPLINES} disciplines')
        self._disciplines.append(discipline)

    def take_discipline(self, index):
        """ returns the discipline at the given index, raises IndexError if invalid """
        if not 0 <= index < len(self._disciplines):
            raise IndexError('no discipline at this index')
        return self._disciplines[index]

    def count_disciplines(self):
        """ returns the number of disciplines """
        return len(self._disciplines)

    def show_overview(self):
        """ returns one line per discipline with its average """
        lines = [f'\t  {d.name:<12}:  {d.average:.2f}' for d in self._disciplines]
        return '\n'.join(lines) + '\n' if lines else ''

    def show_details(self):
        """ returns every discipline with each individual result and the average """
        blocks = []
        for discipline in self._disciplines:
            lines = [f'  {discipline.name} (Schnitt: {discipline.average:.2f})']
            for index in range(discipline.count_results()):
                result = discipline.take_result(index)
                lines.append(f'\t  {result.date:%d.%m.%Y}  :  {result.value:.2f}')
            blocks.append('\n'.join(lines))
        return '\n'.join(blocks) + '\n' if blocks else ''
