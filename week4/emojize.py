import emoji
s = input("Input: ")
res = emoji.emojize(s, language="alias")
print(res)