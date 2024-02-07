greeting = input("How are you doing? ")
if greeting.lstrip().lower()[0:5] == "hello":
    print("$0")
elif greeting.lstrip()[0] == 'h' or greeting.lstrip()[0] == 'H':
    print("$20")
else:
    print("$100")