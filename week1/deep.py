ans = input("What is the Answer of the the Great Question of Life, the Universe and Everything? ")
if ans.strip() == "42":
    print("Yes")
elif ans.lower().strip() == "forty-two":
    print("Yes")
elif ans.lower().strip() == "forty two":
    print("Yes")
else:
    print("NO")
