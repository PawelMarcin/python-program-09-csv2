ARGUMENTS_ERROR = 'Blad wywolania programu, brak argumentow.\n' \
               'Poprawne wywolanie:\n' \
               '\treader2.py <src> <dst> [<change1> [<change2> [<change3> ' \
               '[...]]]]\n' \
               '<src> :\t  plik zrodlowy (.csv, .json, .pickle)\n' \
               '<dst> :\t  plik docelowy (.csv, .json, .pickle)\n' \
               '<changeN> :\t  zmiana w komorce w formacie: "Y,X,wartosc"\n' \
               '\tgdzie:\n' \
               '\t\tY :\t  nr wiersza komorki\n' \
               '\t\tX :\t  nr kolumny komorki\n' \
               '\t\twartosc :\t  nowa wartosc komorki'

SRC_NOT_EXISTS = 'Plik zrodlowy nie istnieje.\n' \
                 'Zawartosc ostatniego istniejacego folderu ("{}") w sciezce ' \
                 'zrodlowej:'

DST_NOT_EXISTS = 'Folder docelowy nie istnieje.\n' \
                 'Zawartosc ostatniego istniejacego folderu ("{}") w sciezce ' \
                 'docelowej:'

BELOW_ZERO = 'Ujemna wartosc w parametrze {}.'

PRINTS = {
    ('a', -1): ARGUMENTS_ERROR,
    ('a', -2): SRC_NOT_EXISTS,
    ('a', -3): DST_NOT_EXISTS,
    ('a', -4): BELOW_ZERO,
    ('a', 2): 'Zostanie wydrukowana zawartosc pliku:\n\t{}.',
    ('a', 3): 'Plik zrodlowy:\n\t{}\nzostanie skopiowany do pliku:\n\t{}'
    # ('p', 1): 'W parametrze {} jest niedozwolony znak',
    }


class PrintOuts():
    # def __init__(self, args_list, data_sheet):
    #     DataManipulation.__init__(args_list, data_sheet)
    #     self.PRINTS = {}

    def print_question(self):
        while True:
            answer = input(' Tak/Nie: ').lower()
            if answer[0] == 't':
                return True
            elif answer[0] == 'n':
                return False

    def print_action_msgs(self, key, arg1=None, arg2=None, arg3=None):
        print(PRINTS[key].format(arg1, arg2, arg3))
