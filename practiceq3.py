def operation(*tp):
    if tp[1]=="+":
        c = tp[0]+tp[2]
        return c

    elif tp[1]=="-":
        c = tp[0]-tp[2]
        return c

    elif tp[1] == "*":
       c = tp[0]*tp[2]
       return c

    elif tp[1] == "/":
       c = tp[0]/tp[2]
       return c

a = int(input("Enter number 1 "))
op = input('Enter +,-,/,. ')
print("\n")
b = int(input("Enter number 2 "))

d=operation(a,op,b)
print(d)
