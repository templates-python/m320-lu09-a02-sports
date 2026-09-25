from datetime import date, datetime

# DAS IST EINE @DATACLASS
class Result:
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
