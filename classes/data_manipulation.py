from classes.file_manipulation import FileManipulation


class DataManipulation(FileManipulation):
    def __init__(self, args_list):
        super().__init__(args_list)
        self.data_sheet = []

    def print_data(self):
        for line in self.data_sheet:
            print(line)

    def load_into_data_sheet(self):
        if self.extentions_list[0] == '.csv':
            for line in self.load_from_csv(self.args_list[1]):
                self.data_sheet.append(line)
        elif self.extentions_list[0] == '.json':
            self.data_sheet = self.load_from_json(self.args_list[1])
        elif self.extentions_list[0] == '.pickle':
            self.data_sheet = self.load_from_pickle(self.args_list[1])

    def dump_data_sheet_into_file(self):
        if self.extentions_list[1] == '.csv':
            self.write_to_csv(self.args_list[2], self.data_sheet)
        elif self.extentions_list[1] == '.json':
            self.write_to_json(self.args_list[2], self.data_sheet)
        elif self.extentions_list[1] == '.pickle':
            self.write_to_pickle(self.args_list[2], self.data_sheet)

    def change_cells_values(self):
        self.changes_params.sort()
        for item in self.changes_params:
            try:
                self.data_sheet[item[0]][item[1]] = item[2]
            except IndexError:
                print('Poza zasiegiem tablicy')
