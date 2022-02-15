# Przebieg dzialania programu:
# 1.    Walidacja parametrow uruchomieniowych:
#   1.1. Jesli ktorykolwiek argument jest niepoprawny to walidacja zostaje
#   przerwna niezaleznie od liczby argumentow i program konczy dzialanie
#   z odpowiednim komunikatem
#   1.2. Jesli nie podano argumentow --> wyswietla pomoc
#   1.3. Jesli podano co najmniej 1 argument:
#       1.3.1.  1 - 2 argumenty (sciezki do plikow) --> sprawdzenie poprawnosci
#       sciezek --> jesli poprawne to propozycja wyswietlenia pliku zrodlowego
#       (1 argument) lub skopiowania pliku (2 argumenty), jesli argument jest
#       bledny --> koniec programu z odpowiednim komunikatem.
#       1.3.2.  co najmniej 3 argumenty --> sprawdzenie poprawnosci sciezek,
#       sprawdzenie poprawnosci parametrow zmian --> jesli argument niepoprawny
#       to koniec programu z odpowiednim komunikatem, jesli argumenty poprawne
#       --> wprowadzenie zmian w pliku.
# 2.    Jesli walidacja pomyslna --> wykonanie wybranej akcji
# 3.    Koniec dzialania programu

"""
TODO: przed wprowadzeniem zmiany komorki dodac wyswietlenie starej
i nowej wartosci komorki i mozliwosc potwierdzenia/rezygnacji ze zmiany
TODO: dodac mozliwosc cofniecia juz wprowadzonej zmiany (cache zmian potrzebny)
"""

from classes.arguments_and_paths import get_args
from classes.data_manipulation import DataManipulation


dm = DataManipulation(get_args())
dm.actions()

if dm.action[0] == -100:
    # HELP
    dm.print_action_msgs((-100, 0))
elif dm.action[0] in [-2, -1]:
    # SRC/DST ERRORS
    ap = dm.split_path(dm.abs_paths_list[dm.action[1]])
    last_folder = dm.last_existing_folder(ap)
    if dm.action == (-1, 2):
        dm.print_action_msgs(dm.action, ap, last_folder)
    else:
        dm.print_action_msgs(
            dm.action, dm.abs_paths_list[dm.action[1]], last_folder
        )
    if dm.print_question():
        for folder in dm.less_simple_folder_content(last_folder):
            print(folder[0], folder[1])
elif dm.action[0] == -3:
    # EXTENTION_ERROR
    dm.print_action_msgs(dm.action, dm.abs_paths_list[dm.action[1]])
elif dm.action[0] in [-6, -4]:
    # TYPE_ERROR
    i = int(-1 * (dm.action[0] + 4) / 2)
    dm.print_action_msgs(
        (dm.action[0], i + 1),
        dm.changes_params_list[-1][i],
        dm.changes_params_list[-1]
    )
elif dm.action[0] in [-7, -5]:
    # BELOW_ZERO
    i = int(-1 * (dm.action[0] + 5) / 2)
    dm.print_action_msgs(
        (dm.action[0], i + 1),
        dm.changes_params_list[-1][i],
        dm.changes_params_list[-1]
    )
elif dm.action[0] == -8:
    # CHANGE_PARAM_ERROR
    dm.print_action_msgs((dm.action[0], 0), dm.changes_params_list[-1])
elif dm.action[0] == 2:
    dm.print_action_msgs(dm.action, dm.abs_paths_list[1])
    if dm.print_question():
        dm.load_data_into_data_sheet()
        dm.print_data()
elif dm.action[0] == 3:
    dm.print_action_msgs(
        dm.action, dm.abs_paths_list[1], dm.abs_paths_list[2]
    )
    if dm.print_question():
        dm.load_data_into_data_sheet()
        dm.dump_data_sheet_into_file()
elif dm.action[0] == 4:
    dm.print_action_msgs(dm.action, dm.abs_paths_list[1], dm.abs_paths_list[2])
    if dm.print_question():
        dm.load_data_into_data_sheet()
        dm.change_cells_values()
        dm.dump_data_sheet_into_file()

dm.print_action_msgs((5, 0))
