from classes.arguments_and_paths import get_args
from classes.data_manipulation import DataManipulation
from classes.print_outs import PrintOuts


dm = DataManipulation(get_args())

if dm.actions() == -1:
    PrintOuts.print_action_msgs(PrintOuts(), ('a', -1))
elif dm.actions() == -2:
    last_folder = dm.last_existing_folder(dm.args_list[-1])
    PrintOuts.print_action_msgs(PrintOuts(), ('a', -2), last_folder)
    for folder in dm.less_simple_folder_content(last_folder):
        print(folder[0], folder[1])
elif dm.actions() == -3:
    last_folder = dm.last_existing_folder(dm.args_list[-1])
    PrintOuts.print_action_msgs(PrintOuts(), ('a', -3), last_folder)
    for folder in dm.less_simple_folder_content(last_folder):
        print(folder[0], folder[1])
elif dm.actions() < -3:
    idx = -1 * (dm.actions() + 1)
    PrintOuts.print_action_msgs(PrintOuts(), ('a', -4), dm.args_list[idx])
elif dm.actions() == 2:
    PrintOuts.print_action_msgs(PrintOuts(), ('a', 2), dm.args_list[1])
    if PrintOuts.print_question(PrintOuts()):
        dm.load_into_data_sheet()
        dm.print_data()
elif dm.actions() == 3:
    PrintOuts.print_action_msgs(PrintOuts(), ('a', 3), dm.args_list[1],
                                dm.args_list[2])
    if PrintOuts.print_question(PrintOuts()):
        dm.load_into_data_sheet()
        dm.dump_data_sheet_into_file()
elif dm.actions() == 4:
    dm.load_into_data_sheet()
    dm.change_cells_values()
    dm.dump_data_sheet_into_file()
