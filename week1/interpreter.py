exp = input("Expression: ").strip().split(' ')
x = float(exp[0])
y = exp[1]
z = float(exp[2])
match y:
    case '+':
        print(f"{(x+z):.1f}")
    case '-':
        print(f"{(x-z):.1f}")
    case '*':
        print(f"{(x*z):.1f}")
    case '/':
        print(f"{(x/z):.1f}")
    case _:
        print("Invalid")