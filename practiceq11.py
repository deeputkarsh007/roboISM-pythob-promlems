str = input("Enter a string: ")

rev = str[::-1]

if rev == str:
    print("Palindrome")
else:
    print("Not Palindrome")