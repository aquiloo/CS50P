import re
import sys

# 解构赋值和标准化输出
def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.match(r"([0-9]+):?([0-9]+)? (AM|PM) to ([0-9]+):?([0-9]+)? (AM|PM)", s):

        # check validness
        hour1, min1, t1, hour2, min2, t2 = match.groups()
        if min1 is None and min2 is None:
            min1 = min2 = 0
        hour1, min1, hour2, min2 = map(int, [hour1, min1, hour2, min2])
        if hour1 > 12 or hour2 > 12:
            raise ValueError
        if min1 > 59 or min2 > 59:
            raise ValueError
        
        if t1 == "PM" and hour1 != 12:
            hour1 += 12
        elif t1 == "AM" and hour1 == 12:
            hour1 = 0

        if t2 == "PM" and hour2 != 12:
            hour2 += 12
        elif t2 == "AM" and hour2 == 12:
            hour2 = 0
        
        # convert
        return f"{hour1:02d}:{min1:02d} to {hour2:02d}:{min2:02d}"
     
    else:
        raise ValueError




if __name__ == "__main__":
    main()