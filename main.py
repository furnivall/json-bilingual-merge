import json
import os
from tkinter.filedialog import askdirectory

dir1 = askdirectory()
dir2 = askdirectory()
files = os.listdir(dir1)

def add_english_to_welsh(path, key, value):
    match value:
        case str():
            path[key] += " / " + englishFile[key]
        case list():
            for index, item in enumerate(value):
               path[key][index] += " / " + englishFile[key][index]
        case dict():
            for nested_key, in value.keys():
                path[key][nested_key] += " / " + englishFile[key][nested_key]

os.mkdir("bil")
for i in files:
    with open(dir1 + '/' + i, 'r') as file:
        welshFile = json.load(file)
        bilingualFile = welshFile.copy()
        with open(dir2 + '/' + i, 'r') as file2:
            englishFile = json.load(file2)
            for key, value in welshFile.items():
                otherValue = englishFile.get(key)
                add_english_to_welsh(bilingualFile, key, value)
        with open(f'bil/{i}', 'w') as our_file:
            json.dump(bilingualFile, our_file)



