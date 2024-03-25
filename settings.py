from aiogram.types import InputFile

class CustomInputFile(InputFile):
    def __init__(self, file_path,filename):
        self.file_path = file_path
        self.filename = filename

    def read(self, bot):
        with open(self.file_path, 'rb') as file:
            return file.read()
