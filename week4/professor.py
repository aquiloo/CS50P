import random


def main():
    n = get_level()
    wrong = 0

    for i in range(10):
        times = 0
        x = generate_integer(n)
        y = generate_integer(n)
        ans = x + y
        while True:
            if times == 3:
                wrong += 1
                break
            res = int(input(f"{x} + {y} = ", end=''))
            if res == ans:
                break
            else:
                print("EEE")
                times += 1
    print(10-wrong)
           

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    try:
        x = random.randint(10**(level-1), 10**level-1)
        if x < 0 or x > 999:
            raise ValueError("Wrong level input")
    except ValueError:
        pass
    return x

if __name__ == "__main__":
    main()
