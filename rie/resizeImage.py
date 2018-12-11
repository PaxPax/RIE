import os, shutil, configparser
from PIL import Image
from multiprocessing import Process


class ResizeImage:
    def __init__(self, width, height, path, zipped=False):
        self.valid_formats = ['jpg', 'png', 'mp4']
        self.batch_size, self.zip_location, self.zip_name = self.read_from_settings()
        self.width = width
        self.height = height
        self.path = path
        self.zipped = zipped
        self.generate_batchs()

    def read_from_settings(self):
        try:
            parser = configparser.RawConfigParser()
            parser.read_file(open(r"./settings/settings.toml"))
            try:
                batch_size = int(parser.get('settings', 'batch_size'))
            except ValueError:
                print("Batch size in settings is not a valid number")
            zip_location = parser.get('settings', 'zip_location')
            zip_name = parser.get('settings', 'zip_name')
        except IOError:
            print("Couldn't open SETTINGS FILE")

        return (batch_size, zip_location, zip_name)

    def image_generator(self):
        try:
            image_list = os.listdir(self.path)
            return (image for image in image_list)
        except IOError:
            print("Couldn't open IMAGE FOLDER")

    def generate_batchs(self):
        image_batch = []
        image_list = self.image_generator()
        for image in image_list:
            image_batch.append(image)
            if len(image_batch) == self.batch_size:
                spawned_process = Process(target=self.image_resize, args=(image_batch,))
                spawned_process.start()
                image_batch = []
                spawned_process.join()

        # must catch the leftover images
        spawned_process = Process(target=self.image_resize, args=(image_batch,))
        spawned_process.start()
        spawned_process.join()

        if self.zipped:
            self.archive_file()

    def image_resize(self, image_batch):
        try:
            for user_image in image_batch:
                # split the incoming image to make sure it's a valid format me can use
                tokens = user_image.split('.')
                if tokens[1] in self.valid_formats:
                    image = Image.open(self.path + '/' + user_image)
                    image = image.resize((self.height, self.width), Image.ANTIALIAS)
                    image.save('./resized_folder/' + user_image)
        except IOError as e:
            print(e)

    def archive_file(self):
        try:
            shutil.make_archive(self.zip_name, 'zip', self.zip_location)
        except IOError as e:
            print(e)
