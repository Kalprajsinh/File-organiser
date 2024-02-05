import os
import shutil
from collections import defaultdict

path = input("Enter Path: ")

files = os.listdir(path)

extension_dict = defaultdict(list)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    extension_dict[extension].append(file)

for extension, files_list in extension_dict.items():
    target_folder = os.path.join(path, extension)
    
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    for file in files_list:
        shutil.move(os.path.join(path, file), os.path.join(target_folder, file))






