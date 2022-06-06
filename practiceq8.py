str = input("Enter the string")
n = len(str)
sum = 0
for i in range (0,n):
    if 48 <= ord(str[i]) <= 57:
        sum = sum + int(str[i])
print(sum)