def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not(s[0].isalpha() and s[1].isalpha()):
        return False
    begin = -1
    for index, char in enumerate(s):
        if not char.isalpha():
            if char >= '0' and char <= '9':
                if begin == -1:
                    begin = index
            else:
                return False
        elif begin > -1:
            return False
    if s[begin] == '0':
        return False
    return True

main()