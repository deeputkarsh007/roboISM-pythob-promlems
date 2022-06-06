cc_no = input("Enter your credit card number\t")
c = len(cc_no) - 4
otpt = int(cc_no)%10000
print("*"*c,end="")
print(otpt)
