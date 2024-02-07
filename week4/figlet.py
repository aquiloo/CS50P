from pyfiglet import Figlet
import sys
import random


f = Figlet()
font_list = f.getFonts()

# check parameters
if len(sys.argv) < 2:
    # get random font
    length = len(font_list)
    rand_int = random.randint(0, length-1)
    f.setFont(font=font_list[rand_int])
elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in font_list:
            f.setFont(font=sys.argv[2])
        else:
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)
else:
    print("Invalid usage")
    sys.exit(1)

# get input
s = input("Input: ")

print(f.renderText(s))

