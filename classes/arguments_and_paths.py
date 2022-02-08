import os
import sys

EXT = ['.csv', '.json', '.pickle']

def get_args():
    return sys.argv[0:]


class ArgumentsAndPaths:
    def __init__(self, args_list):
        self.args_list = args_list
        self.args_length = len(self.args_list)
        self.extentions_list = []
        self.changes_params = []

    def args_validator(self):
        valid_args = [0]
        for i in range(1, self.args_length):
            if i == 1:
                self.args_list[i] = self.set_abs_path(self.args_list[i])
                ext = self.get_file_extension(self.args_list[i])
                if valid_args[i - 1] == 0:
                    if self.path_exists(self.args_list[i], dst=False) and ext \
                            in EXT:
                        valid_args.append(0)
                        self.extentions_list.append(ext)
                        if not self.is_file(self.args_list[i]):
                            valid_args[i] = -1
                    else:
                        valid_args.append(-1)
            elif i == 2:
                self.args_list[i] = self.set_abs_path(self.args_list[i])
                ext = self.get_file_extension(self.args_list[i])
                if valid_args[i - 1] == 0:
                    if self.path_exists(self.args_list[i]) and ext in EXT:
                        valid_args.append(0)
                        self.extentions_list.append(ext)
                    else:
                        valid_args.append(-1)
            elif i > 2:
                if valid_args[i - 1] == 0:
                    if self.params_validator(i):
                        valid_args.append(0)
                    else:
                        valid_args.append(-1)
        return valid_args

    def set_abs_path(self, given_path):
        given_path = os.path.abspath(given_path)
        return given_path

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

    def params_validator(self, i):
        change = self.args_list[i].split(',')
        if not len(change) == 3:
            return False
        else:
            for j in range(2):
                try:
                    change[j] = int(change[j])
                except ValueError():
                    print(f'"{change[j]}" nie jest liczba calkowita '
                          f'(w parametrze {i}: {self.args_list[i]})')
                    return False
                if change[j] < 0:
                    return False
            self.changes_params.append(change)
            return True

    def actions(self):
        valid_args = self.args_validator()
        value_to_return = 0
        if not sum(valid_args) == 0 or self.args_length == 1:
            if self.args_length == 1:
                value_to_return = -1
            else:
                for i in range(len(valid_args)):
                    if valid_args[i] == -1:
                        if i == 1:
                            value_to_return = -2
                        elif i == 2:
                            value_to_return = -3
                        else:
                            value_to_return = -1 * (i + 1)
        else:
            if self.args_length == 2:
                value_to_return = 2
            elif self.args_length == 3:
                value_to_return = 3
            elif self.args_length > 3:
                value_to_return = 4
        return value_to_return
