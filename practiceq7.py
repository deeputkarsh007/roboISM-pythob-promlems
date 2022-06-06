listA = []
y = 1
n = int(input("Enter number of elements in the list: "))
for i in range(0, n):
   elm = input("enter values ")
   listA.append(elm)
print("The entered list is: \n",listA)
for i in range(0, n):
    x = listA.count(listA[i])
    if x >= y:
        y = x
        z = listA[i]

print(str(z)+ " is repeated " +str(y)+ " times.")