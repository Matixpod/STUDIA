# Mateusz Podporski
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("path",nargs='?', help="Path to the directory", default="")
parser.add_argument("-d", action='store_true', help="Show only directories")
args = parser.parse_args()

path = args.path or os.getcwd()
d = args.d



if path != "":
    obj = os.scandir(path)
    print("Files and Directories in '% s':" % path)
else:
    print("Files and Directories in current directory")
    obj = os.scandir(path)

for entry in obj:
    if d == True:
        if entry.is_dir() and not entry.name.startswith("."):
            print(f"    {entry.name}")
    elif not entry.name.startswith("."):
        print(f"    {entry.name}")



























