import json


def get_dictionary():
    with open('utils/data_dictionary.json') as json_file:
        try:
            data_dictionary = json.load(json_file)
        except FileNotFoundError:
            print('Data dictionary file not found')

        return data_dictionary

