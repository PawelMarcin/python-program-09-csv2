import csv
import json
import pickle
from classes.arguments_and_paths import ArgumentsAndPaths


class FileManipulation(ArgumentsAndPaths):
    def load_from_csv(self, path_to_file):
        with open(path_to_file, 'r', newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter=';')
            for csv_line in csv_reader:
                yield csv_line

    def load_from_json(self, path_to_file):
        with open(path_to_file, 'r', encoding='utf-8') as f:
            json_data_as_list = json.loads(f.read())
            try:
                json_data_as_list = json.loads(json_data_as_list)
            except TypeError:
                ...
        return json_data_as_list

    def load_from_pickle(self, path_to_file):
        with open(path_to_file, 'rb') as f:
            pickle_data_as_list = pickle.load(f)
            try:
                pickle_data_as_list = json.loads(pickle_data_as_list)
            except TypeError:
                ...
        return pickle_data_as_list

    def write_to_csv(self, path_to_file, data_sheet):
        with open(path_to_file, 'w', newline='', encoding='utf-8') as f:
            csv_writer = csv.writer(f, delimiter=';')
            for csv_line in data_sheet:
                csv_writer.writerow(csv_line)

    def write_to_json(self, path_to_file, data_sheet):
        with open(path_to_file, 'w', encoding='utf-8') as f:
            json.dump(data_sheet, f, ensure_ascii=False)

    def write_to_pickle(self, path_to_file, data_sheet):
        with open(path_to_file, 'wb') as f:
            pickle.dump(data_sheet, f)

