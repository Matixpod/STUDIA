# Mateusz Podporski
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("path",nargs='?', help="Path to the directory", default="")
parser.add_argument("-d", action='store_true', help="Show only directories")
parser.add_argument("-L", type=int, help="Max depth of the tree", default=None)
args = parser.parse_args()

path = args.path or os.getcwd()
d = args.d
max_depth = args.L

if path != "":
    obj = os.scandir(path)
    print("Files and Directories in '% s':" % path)
else:
    print("Files and Directories in current directory")
    obj = os.scandir(path)

dir_count = 0
file_count = 0

def tree(d,path="",n=1):
    global dir_count, file_count
    tab = "   "
    if max_depth is not None and n > max_depth:
        return
    obj = os.scandir(path)

    for entry in obj :
        if entry.is_dir() and not entry.name.startswith("."):
            print(f"{tab * n}\--{entry.name}")
            
            dir_count += 1
            tree(d,f"{path}\{entry.name}",n+1)
    
        elif d == False:
            print(f"{tab * n}|--{entry.name}")
            file_count += 1

        

tree(d,path)
print(f"\nTotal directories: {dir_count}")
print(f"Total files: {file_count}")