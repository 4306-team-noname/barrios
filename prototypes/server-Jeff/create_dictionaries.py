import json
from json import JSONEncoder
import os
import pandas as pd
import numpy as np

path = '../../iss-data/csv'
target_dir = './dictionaries'


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def clean_filename(name_with_extension):
    extension_split = name_with_extension.split('.')
    no_extension = extension_split[0]
    no_nums_or_dashes = ''.join(
            i for i in no_extension if (not i.isdigit() and not i == '-')
        )
    if no_nums_or_dashes[-1:] == '_':
        no_nums_or_dashes = no_nums_or_dashes.rstrip(no_nums_or_dashes[-1])
    print(f'Cleaned: {no_nums_or_dashes}')
    return no_nums_or_dashes


file_list = os.listdir(path)
files = []
dirs = []

for file in file_list:
    if os.path.isfile(f"{path}/{file}"):
        files.append(file)
    elif os.path.isdir(f"{path}/{file}"):
        dirs.append(file)

dictionary = {}

for file in files:
    print(f"Reading {file}")
    df = pd.read_csv(f"{path}/{file}")
    cols = df.columns.to_numpy()
    print(f"Encoding columns for {file}")
    cols_list = cols.tolist()
    clean_name = clean_filename(file)
    if len(clean_name) > 0:
        dictionary[clean_name] = cols_list

with open(f'{target_dir}/dictionary.json', 'w') as outfile:
    json.dump(dictionary, outfile, indent=4)
print(f"Wrote {target_dir}/dictionary.json successfully")
