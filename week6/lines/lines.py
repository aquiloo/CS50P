import sys


if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    if not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)
    try:
        f = open(f"{sys.argv[1]}")
    except FileNotFoundError:
        print("File Not Exist")
        sys.exit(1)
    else:
        lines = 0
        for line in f:
            if line.lstrip().startswith("#"):
                continue
            elif line.strip() == "":
                continue
            else:
                lines += 1
        print(lines)