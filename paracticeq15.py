str = input("Enter a string: ")
n = len(str)
alpha = []
number = []
special = []

for i in range(0, n):
    if 57 >= ord(str[i]) >= 48:
        number.append(str[i])
    elif 90 >= ord(str[i]) >= 65:
        alpha.append(str[i])
    elif 122 >= ord(str[i]) >= 97:
        alpha.append(str[i])
    else:
        special.append(str[i])

a = len(alpha)
b = len(number)
c = len(special)

print(a, b, c)