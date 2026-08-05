import os
import json


class FileManager:

    @staticmethod
    def create_folder(path):
        os.makedirs(path, exist_ok=True)


    @staticmethod
    def save_text(file_path, text):

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(text)


    @staticmethod
    def read_text(file_path):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()


    @staticmethod
    def save_json(file_path, data):

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )


    @staticmethod
    def read_json(file_path):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)