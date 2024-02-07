name = input("camelCase: ")
res = ""
begin = 0
for index, val in enumerate(name):
    if val.isupper():
        res += name[begin:index]
        res += '_'
        begin = index
res += name[begin:len(name)]
print("snake_case: " + res.lower())