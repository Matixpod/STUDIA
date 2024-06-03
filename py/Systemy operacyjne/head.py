# Mateusz Podporski
# Zadania 2.1 , 2.2, 2.3
import sys
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument(
    "-n", "--lines",
    default=[10],
    type=int,
    nargs=1,
    help="Number of lines to show."
)

parser.add_argument(
    "file",
    type=str,
    help="File which should be displayed."
)

parser.add_argument(
    "-v", "--verbose",
    action="store_true",
    default=False,
    help="Explain what is done."
)

args = parser.parse_args()

script_name = os.path.basename(sys.argv[0])

if args.verbose:
    print(f"Program is running with name {script_name}")
    print(f"It will print {args.lines[0]} lines from {args.file}.")
    if script_name == 'tail.py':
        print(f"It will print the last {args.lines[0]} lines.")
    else:
        print(f"It will print the first {args.lines[0]} lines.")
    print("="*50)

try:
    with open(args.file) as f:
        lines = f.readlines()
        if script_name == 'tail.py':
            lines_to_print = lines[-args.lines[0]:]
        else:
            lines_to_print = lines[:args.lines[0]]
        
        for line in lines_to_print:
            print(line.strip())
except FileNotFoundError:
    print(f"Error: The file '{args.file}' does not exist. Please provide an existing text file.")

if args.verbose:
    print("="*50)
