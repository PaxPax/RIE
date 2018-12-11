import os


class SetUp:
    def __init__(self, folder_path, file_path):
        self.folder_path = folder_path
        self.file_path = file_path
        self.run_start_file()

    def has_settings_folder(self):
        return os.path.isdir(self.folder_path)

    def has_settings_file(self):
        return os.path.isfile(self.file_path)

    def make_settings_folder(self):
        os.makedirs(self.folder_path)

    def make_settings_file(self):
        settings_string = "[settings]\n"
        settings_string += "batch_size = 4\n"
        settings_string += "zip_location = './resized_folder'\n"
        settings_string += "zip_name = 'resized_folder'"
        with open(self.file_path, 'w') as out_file:
            out_file.write(settings_string)

    def make_resized_folder(self):
        folder_path = "./resized_folder"
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)

    def run_start_file(self):
        if not self.has_settings_folder():
            self.make_settings_folder()
            if not self.make_settings_file():
                self.make_settings_file()
        self.make_resized_folder()
