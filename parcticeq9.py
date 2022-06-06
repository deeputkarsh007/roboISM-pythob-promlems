strA = input("Enter the string\t")
n = len(strA)
listA = []
strB = ""
for i in range(0, n):
    listA.append(ord(strA[i]))
listA.sort()
for i in range(0, n):
    strB += chr(listA[i])

print(strB)