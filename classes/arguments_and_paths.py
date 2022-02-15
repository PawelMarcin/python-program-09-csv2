import os
import sys
from classes.print_outs import PrintOuts
from classes.print_outs import PRINTS

EXT = ['.csv', '.json', '.pickle']


def get_args():
    return sys.argv[0:]


class ArgumentsAndPaths(PrintOuts):
    def __init__(self, args_list):
        # lista argumentow wywolania programu:
        self.args_list = args_list
        # dlugosc listy wywolania programu:
        self.args_length = len(self.args_list)
        # lista typow plikow w wywolaniu programu:
        self.extentions_list = []
        # lista sciezek absolutnych:
        self.abs_paths_list = [0]
        # lista parametrow zmian:
        self.changes_params_list = []
        # zwracane przez metode actions:
        self.action = ()

    def args_validator(self):
        valid_args = [0]
        for i in range(1, self.args_length):
            if i == 1:
                if sum(valid_args) == 0:
                    self.abs_paths_list.append(
                        self.set_abs_path(self.args_list[i])
                    )
                    valid_args.append(self.path_validator(
                        self.abs_paths_list[i], dst=False))
            elif i == 2:
                if sum(valid_args) == 0:
                    self.abs_paths_list.append(
                        self.set_abs_path(self.args_list[i])
                    )
                    valid_args.append(self.path_validator(
                        self.abs_paths_list[i], dst=True))
            elif i > 2:
                if sum(valid_args) == 0:
                    valid_args.append(self.params_validator(i))
        return valid_args

    def path_validator(self, given_path, dst):
        ext = self.get_file_extension(given_path)
        if ext in EXT:
            self.extentions_list.append(ext)
            if self.path_exists(given_path, dst=False):
                if self.is_file(given_path):
                    return 0
                else:
                    return -2
            else:
                if self.path_exists(given_path, dst):
                    return 0
                else:
                    return -1
        else:
            return -3

    def params_validator(self, i):
        change = self.args_list[i].split(',')
        self.changes_params_list.append(change)
        if len(change) == 3:
            for j in range(2):
                try:
                    change[j] = int(change[j])
                except ValueError:
                    # print(f'"{change[j]}" nie jest liczba calkowita '
                    #       f'(w parametrze {i}: {self.args_list[i]})')
                    return -2 * j - 4
                if change[j] < 0:
                    return -2 * j - 5
            return 0
        else:
            return -8

    def set_abs_path(self, given_path):
        given_path = os.path.abspath(given_path)
        return given_path

    def split_path(self, given_path):
        return os.path.split(given_path)[0]

    def get_file_extension(self, path_to_file):
        return os.path.splitext(path_to_file)[1]

    def path_exists(self, given_path, dst=True):
        if dst:
            given_path = os.path.split(given_path)[0]
        return os.path.exists(given_path)

    def is_file(self, given_path):
        return os.path.isfile(given_path)

    def last_existing_folder(self, given_path):
        while not os.path.exists(given_path):
            given_path = os.path.split(given_path)[0]
        return given_path

    def simple_folder_content(self, given_path):
        return os.listdir(given_path)

    def less_simple_folder_content(self, given_path):
        with os.scandir(given_path) as fc:
            for item in fc:
                yield '     ' if item.is_file() else '(dir)', item.name

    def actions(self):
        valid_args = self.args_validator()
        if self.args_length == 1:
            self.action = (-100, 0)
            return self.action
        else:
            if sum(valid_args) == 0:
                if len(valid_args) in [2, 3]:
                    self.action = (len(valid_args), 0)
                    return self.action
                else:
                    self.action = (4, 0)
                    return self.action
            else:
                self.action = (sum(valid_args), len(valid_args) - 1)
                return self.action
