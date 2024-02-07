s = input("Input: ")
res = ''.join(char for char in s if char != 'a' and char != 'A' and char != 'e' and char != 'E' and char != 'i' and char != 'I' and char != 'o' and char != 'O' and char != 'u' and char != 'U')
print("Output: "+res)