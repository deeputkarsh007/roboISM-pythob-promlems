a = int(input("Enter number 1 "))
b = int(input("Enter number 2 "))
print("Numbers before swapping: ")
print(a, b)

a = a ^ b
b = a ^ b
a = a ^ b

print("Numbers after swapping: ")
print(a, b)