import os
import shutil

path = input("Enter the file path: ")

files = os.listdir(path)

for i in files:
    filesname, extension = os.path.splitext(i)
    extension_1 = extension[1:]

    folder_path = path + "\\" + extension_1

    if os.path.exists(folder_path):
        shutil.move(path + "\\" + i, folder_path + "\\" + i)
    else:
        os.makedirs(folder_path)
        shutil.move(path + "\\" + i, folder_path + "\\" + i)

print("All files have been organized.")