from athlete import Athlete
from club import Club
from discipline import Discipline
from performance_record import PerformanceRecord
from result import Result


def main():
    """ Let's create some data and see how it works """
    # In the beginning, there was a club
    the_club = Club('LC Zürisee')

    # Let there be some performance records
    record_nina = PerformanceRecord()
    create_discipline_list(record_nina)

    record_jon = PerformanceRecord()
    create_discipline_list(record_jon)

    record_aylin = PerformanceRecord()
    create_discipline_list(record_aylin)

    # And some athletes, of course
    nina = Athlete('Nina', record_nina)
    jon = Athlete('Jon', record_jon)
    aylin = Athlete('Aylin', record_aylin)

    # Add those athletes to the club
    the_club.add_athlete(nina)
    the_club.add_athlete(jon)
    the_club.add_athlete(aylin)
    # And print the list of athletes in this club
    print(the_club.show_athlete_list())

    # Next we need a couple of results
    record_nina.take_discipline(0).add_result(Result(8.0, '1.1.11'))
    record_nina.take_discipline(0).add_result(Result(8.5, '2.2.22'))
    record_nina.take_discipline(1).add_result(Result(7.0, '3.3.33'))
    record_nina.take_discipline(1).add_result(Result(7.5, '4.4.44'))
    record_nina.take_discipline(2).add_result(Result(6.5, '5.5.55'))
    record_nina.take_discipline(2).add_result(Result(7.0, '6.6.66'))

    record_jon.take_discipline(0).add_result(Result(6.5, '1.1.11'))
    record_jon.take_discipline(0).add_result(Result(7.0, '2.2.22'))
    record_jon.take_discipline(1).add_result(Result(8.0, '3.3.33'))
    record_jon.take_discipline(1).add_result(Result(8.5, '4.4.44'))
    record_jon.take_discipline(2).add_result(Result(7.5, '5.5.55'))
    record_jon.take_discipline(2).add_result(Result(8.0, '6.6.66'))

    record_aylin.take_discipline(0).add_result(Result(9.0, '1.1.11'))
    record_aylin.take_discipline(0).add_result(Result(8.5, '2.2.22'))
    record_aylin.take_discipline(1).add_result(Result(7.5, '3.3.33'))
    record_aylin.take_discipline(1).add_result(Result(8.0, '4.4.44'))
    record_aylin.take_discipline(2).add_result(Result(9.0, '5.5.55'))
    record_aylin.take_discipline(2).add_result(Result(8.5, '6.6.66'))

    print('----')
    print(the_club.show_athlete_report('Nina'))
    print('----')
    print(the_club.show_athlete_report('Jon'))
    print('----')
    print(the_club.show_athlete_report('Aylin'))
    print('----')
    print(the_club.show_athlete_report('Theo'))

    # Finally we show the detailed report for one athlete
    print(record_aylin.show_details())


def create_discipline_list(record):
    """ creates a list of disciplines """
    record.add_discipline(Discipline('Sprint'))
    record.add_discipline(Discipline('Weitsprung'))
    record.add_discipline(Discipline('Kugelstoss'))


if __name__ == '__main__':
    main()
