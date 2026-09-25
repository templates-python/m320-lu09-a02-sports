from dataclasses import dataclass
from datetime import datetime


@dataclass
class Result:
    """ a single measured result within a discipline """
    value: float
    date: 'datetime' = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('value must be a number')
        if not 0.0 <= value <= 10.0:
            raise ValueError('value must be between 0.0 and 10.0')
        self._value = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        """
        sets the date of this result.
        If a string "(d)d.(m)m.(yy)yy" is provided, it converts it to DateTime
        :param: value(mixed): The date or None=now
        """
        if isinstance(value, datetime):
            self._date = value
        elif isinstance(value, str) and value != '':
            self._date = datetime.strptime(value, '%d.%m.%y')
        else:
            self._date = datetime.now()
