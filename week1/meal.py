def main():
    time = input("What time is it? ")
    ftime = convert(time)
    if ftime >= 7 and ftime <= 8:
        print("breakfast time")
    elif ftime >= 12 and ftime <= 13:
        print("lunch time")
    elif ftime >= 18 and ftime <= 19:
        print("dinner time")
    else:
        pass
def convert(time):
    time = time.strip().split(':')
    a = float(time[0])
    b = float(time[1])/60
    return a + b

if __name__ == "__main__":
    main()