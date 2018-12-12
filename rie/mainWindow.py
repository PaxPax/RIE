import PySimpleGUI as sg
import os
from rie import startFile
from rie import resizeImage


class MainWindow:

    def __init__(self, settings_dir):
        self.settings_dir = settings_dir
        self.settings_file = self.settings_dir + "/settings.toml"
        self.define_widgets()
        self.build_window()

    def define_widgets(self):
        self.input_image_height = sg.InputText('', size=(10, 1), key='input_height')
        self.input_image_width = sg.InputText('', size=(10, 1), key='input_width')
        self.selected_folder = sg.InputText(key='selected_folder')
        self.checkbox_iszipped = sg.Checkbox('Zip Folder', size=(8, 1), key='zip')

    def build_window(self):
        self.layout = [[sg.Text('Choose Folder To Resize Images Inside')],
                       [sg.Text('Source Folder:', size=(15, 1)), self.selected_folder, sg.FolderBrowse()],
                       [sg.Text(' ' * 111), self.checkbox_iszipped],
                       [sg.Text('Set Height/Width: '), self.input_image_height, sg.Text('px'), sg.Text(' ' * 5),
                        self.input_image_width,
                        sg.Text('px')],
                       [sg.Text(' ' * 30), sg.Text('Height', size=(10, 1)), sg.Text(' ' * 15),
                        sg.Text('Width', size=(10, 1))],
                       [sg.Text('')],
                       [sg.Submit(), sg.Cancel(), sg.Text(' ' * 83), sg.Button('Settings', key='_settings_')]
                       ]
        self.window = sg.Window('RIE')
        self.window.Layout(self.layout)

    def isvalid_input(self, width, height):
        if isinstance(width, int) and isinstance(height, int):
            return (width and height) > 0
        else:
            return False

    def show_warning(self, reason):
        if reason == 'input':
            sg.Popup('Please enter valid HEIGHT and WIDTH')
        elif reason == 'path':
            sg.Popup('Please provide a valid DIRECTORY')

    def isvalid_dir(self, path):
        return os.path.isdir(path)

    def display_settings(self):
        read_settings = self.retrieve_settings()
        settings_window = sg.Window('Settings')
        settings_layout = [[sg.Multiline(read_settings, size=(40, 25))],
                           [sg.Save(), sg.Cancel()]]
        settings_window.Layout(settings_layout)

        settings_event, settings_value = settings_window.Read()
        if settings_event is None:
            settings_window.Close()
        else:
            self.save_settings(settings_value)



    def retrieve_settings(self):
        with open(self.settings_file) as file:
            read_data = file.read()
        return read_data

    def save_settings(self, new_settings):
        with open(self.settings_file, 'w') as file:
            file.write(''.join(new_settings))


if __name__ == '__main__':
    startFile.SetUp("./settings", "./settings/settings.toml")
    main_window = MainWindow("./settings")

    while True:
        event, values = main_window.window.Read()
        if event == 'Cancel' or event is None:
            break
        if event is "Submit":
            height = int(values['input_height'])
            width = int(values['input_width'])
            folder = values['selected_folder']
            if not main_window.isvalid_input(width, height):
                main_window.show_warning('input')
            elif not main_window.isvalid_dir(folder):
                main_window.show_warning('path')
            else:
                resizeImage.ResizeImage(width, height, folder, values['zip'])
                sg.Popup('Done!')
        elif event is '_settings_':
            main_window.display_settings()

    main_window.window.Close()
