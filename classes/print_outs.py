HELP = 'Uruchamianie programu "reader2.py":\n' \
       'reader2.py <src> <dst> [<change1> [<change2> [<change3> ' \
       '[...]]]]\n' \
       '    <src> :\t  plik zrodlowy (.csv, .json, .pickle)\n' \
       '    <dst> :\t  plik docelowy (.csv, .json, .pickle)\n' \
       '<changeN> :\t  zmiana w komorce w formacie: "Y,X,wartosc"\n' \
       '\tgdzie:\n' \
       '\t\t      Y :\tnr wiersza komorki (numeracja od 0)\n' \
       '\t\t      X :\tnr kolumny komorki (numeracja od 0)\n' \
       '\t\twartosc :\tnowa wartosc komorki'

CHANGE_PARAM_ERROR = 'Bledny argument <changeN> {}.\n' + HELP

SRC_NOT_EXISTS = 'Plik zrodlowy ({}) nie istnieje.\n' \
                 'Wyswietlic zawartosc ostatniego istniejacego folderu ' \
                 'w sciezce zrodlowej ({})?'

DST_NOT_EXISTS = 'Folder docelowy ({}) nie istnieje.\n' \
                 'Wyswietlic zawartosc ostatniego istniejacego folderu ' \
                 'w sciezce docelowej ({})?'

SRC_POINTS_FOLDER = 'Nazwa pliku zrodlowego ({}) wskazuje na folder.\n' \
                    'Wyswietlic zawartosc ostatniego istniejacego folderu ' \
                    'w sciezce zrodlowej ({})?'

DST_POINTS_FOLDER = 'Nazwa pliku docelowego ({}) wskazuje na folder.\n' \
                    'Wyswietlic zawartosc ostatniego istniejacego folderu ' \
                    'w sciezce docelowej ({})?'

SRC_EXTENTION_ERROR = 'Nieobslugiwany typ pliku w sciezce zrodlowej:\n\t{}\n' \
                      'Obslugiwane typy plikow:\n\t.csv\n\t.json\n\t.pickle'

DST_EXTENTION_ERROR = 'Nieobslugiwany typ pliku w sciezce docelowej:\n\t{}\n' \
                      'Obslugiwane typy plikow:\n\t.csv\n\t.json\n\t.pickle'

TYPE_ERROR = 'Wartosc "{}" w parmetrze {} nie jest liczba calkowita.\n' \
             'Aby uzyskac pomoc wpisz: reader2.py'

BELOW_ZERO = 'Ujemna wartosc ({}) w parametrze {}.\n' \
             'Aby uzyskac pomoc wpisz: reader2.py'

ARRAY_INDEX_ERROR = 'Komorka ({}, {}) poza zakresem tablicy.\n' \
                    'Wymiary tablicy:\n' \
                    '\tY: {} wiersze/-y (od 0 do {})\n' \
                    '\tX: {} kolumn (od 0 do {})\n' \
                    'Nie zmieniono wartosci komorek.'

LIST_FILE = 'Zostanie wydrukowana zawartosc pliku:' \
            '\n\t{}.'

COPY_FILE = 'Zawartosc pliku zrodlowego:' \
            '\n\t{}' \
            '\nzostanie skopiowana do pliku:' \
            '\n\t{}'

MODIFY_FILE = 'Zawartosc pliku: \n\t' \
              '{}\n' \
              'zostanie zmodyfikowana i zapisana w pliku: \n\t' \
              '{}'

READY_TO_CHANGE_CELL = '\nCzy zmienic wartosc komorki ({}, {})?\n' \
                       '\tStara wartosc: {}\n' \
                       '\tNowa wartosc: {}'

CELL_CHANGED = 'Zmieniono i zapisano wartosc komorki ({}, {})\n' \
               '\tStara wartosc: {}\n' \
               '\tNowa wartosc: {}'

CELL_NOT_CHANGED = 'Nie zmieniono wartosci komorki ({}, {})'

PROGRAM_END = '\nKoniec programu.'

PRINTS = {
    (-100, 0): HELP,
    (-1, 1): SRC_NOT_EXISTS,
    (-1, 2): DST_NOT_EXISTS,
    (-2, 1): SRC_POINTS_FOLDER,
    (-2, 2): DST_POINTS_FOLDER,
    (-3, 1): SRC_EXTENTION_ERROR,
    (-3, 2): DST_EXTENTION_ERROR,
    (-4, 1): TYPE_ERROR,
    (-5, 1): BELOW_ZERO,
    (-6, 2): TYPE_ERROR,
    (-7, 2): BELOW_ZERO,
    (-8, 0): CHANGE_PARAM_ERROR,
    (-9, 0): ARRAY_INDEX_ERROR,
    (2, 0): LIST_FILE,
    (3, 0): COPY_FILE,
    (4, 0): MODIFY_FILE,
    (5, 0): READY_TO_CHANGE_CELL,
    (6, 0): CELL_CHANGED,
    (7, 0): CELL_NOT_CHANGED,
    (8, 0): PROGRAM_END
    }


class PrintOuts:
    def print_question(self):
        while True:
            answer = input('Kontynuowac? (domyslnie: NIE)\n'
                           'T(ak)/N(ie): ').lower()
            if answer and answer[0] == 't':
                return True
            elif answer and answer[0] == 'n':
                return False
            else:
                return False

    def print_action_msgs(self, key, *values):
        print(PRINTS[key].format(*values))
