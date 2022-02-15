from classes.file_manipulation import FileManipulation


class DataManipulation(FileManipulation):
    def __init__(self, args_list):
        super().__init__(args_list)
        self.data_sheet = []
        # zwracane przez metode check_array_index:
        self.old_cells_values = []
        self.index_error = ()

    def print_data(self):
        for line in self.data_sheet:
            print(line)

    def load_data_into_data_sheet(self):
        if self.extentions_list[0] == '.csv':
            for line in self.load_from_csv(self.abs_paths_list[1]):
                self.data_sheet.append(line)
        elif self.extentions_list[0] == '.json':
            self.data_sheet = self.load_from_json(self.abs_paths_list[1])
        elif self.extentions_list[0] == '.pickle':
            self.data_sheet = self.load_from_pickle(self.abs_paths_list[1])

    def dump_data_sheet_into_file(self):
        if self.extentions_list[1] == '.csv':
            self.write_to_csv(self.abs_paths_list[2], self.data_sheet)
        elif self.extentions_list[1] == '.json':
            self.write_to_json(self.abs_paths_list[2], self.data_sheet)
        elif self.extentions_list[1] == '.pickle':
            self.write_to_pickle(self.abs_paths_list[2], self.data_sheet)

    def check_array_index(self):
        self.changes_params_list.sort()
        for item in self.changes_params_list:
            try:
                self.old_cells_values.append(
                    self.data_sheet[item[0]][item[1]]
                )
            except IndexError:
                self.index_error = (-9, item[0], item[1])
                return self.index_error
        return 0, 0, 0

    def change_cell_value(self, cell_row, cell_column, value):
        self.data_sheet[cell_row][cell_column] = value
