grocery = {}
while True:
    try:
        x = input().lower()
    except EOFError:
        break
    if x == '':
        continue
    elif x in grocery:
        grocery[x] += 1
    else:
        grocery[x] = 1
         
res = sorted(grocery.items())
res = dict(res)
for key, value in res.items():
    print(f"{value} {key.upper()}")
