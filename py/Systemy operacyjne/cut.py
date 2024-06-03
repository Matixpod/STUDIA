# Mateusz Podporski
# Zadanie 2.4
import argparse

def main():
    parser = argparse.ArgumentParser(description="Simplified cut command in Python")
    parser.add_argument("FILE", help="Input file to process")
    parser.add_argument("-d", "--delimiter", default="\t", help="Delimiter for separating columns (default: tab)")
    parser.add_argument("-f", "--fields", required=True, help="List of fields to display (comma-separated)")
    parser.add_argument("--output-delimiter", default="\t", help="Delimiter for output (default: tab)")

    args = parser.parse_args()

    with open(args.FILE, "r") as f:
        for line in f:
            fields = line.strip().split(args.delimiter)
            selected_fields = [fields[i - 1] for i in map(int, args.fields.split(","))]

            output = args.output_delimiter.join(selected_fields)
            print(output)

if __name__ == "__main__":
    main()