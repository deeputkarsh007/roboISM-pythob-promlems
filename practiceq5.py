n = int(input("Enter size of list"))
listA=[n]
listb=[]
for i in range(0, n):
    num = int(input("Enter elements"))
    listA.append(num)

for i in range(0, n):
    if(listA.count(listA[i])>=2):
        listb.append(listA[i])

print(listb)
