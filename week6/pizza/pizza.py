import sys
import csv


from tabulate import tabulate

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    if not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    elif sys.argv[1] not in {"regular.csv", "sicilian.csv"}:
        print("File Not Exist")
        sys.exit(1)
    with open(f"{sys.argv[1]}") as f:
        reader = csv.DictReader(f)
        print(tabulate(reader, headers="keys", tablefmt="grid"))