while True:
    s = input("Fraction: ").split('/')
    try:
        a = int(s[0])
        b = int(s[1])
    except ValueError:
        pass
    else:
        try:
            res = round(a/b, 2)
        except ZeroDivisionError:
            pass
        else:
            if res <= 0.01:
                print("E")
            elif res >= 0.99 and res <=1:

                print("F")
            elif res > 1:
                continue
            else:
                print(f"{int(res*100)}%")
            break
