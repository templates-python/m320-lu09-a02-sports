MAX_RESULTS = 5


class Discipline:
    """ a discipline (e.g. sprint, long jump) within a performance record """

    def __init__(self, name):
        self._name = name
        self._results = []

    @property
    def name(self):
        return self._name

    def add_result(self, result):
        """ adds a result, raises OverflowError if the maximum is reached """
        if len(self._results) >= MAX_RESULTS:
            raise OverflowError(f'a discipline can only hold {MAX_RESULTS} results')
        self._results.append(result)

    def take_result(self, index):
        """ returns the result at the given index, raises IndexError if invalid """
        if not 0 <= index < len(self._results):
            raise IndexError('no result at this index')
        return self._results[index]

    def count_results(self):
        """ returns the number of results """
        return len(self._results)

    @property
    def average(self):
        """ returns the average of all results, 0.00 if there are none """
        if not self._results:
            return 0.00
        return round(sum(result.value for result in self._results) / len(self._results), 2)
