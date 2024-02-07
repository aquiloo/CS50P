import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.match(r"^([0-9]+).([0-9]+).([0-9]+).([0-9]+)$", ip):
        for i in range(4):
            num = int(matches.group(i+1))
            if num > 255 or num < 0:
                return False
        return True
    return False
            


if __name__ == "__main__":
    main()