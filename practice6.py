lowerlimit=input('Enter the Lower Limit: ')
upperlimit=input('Enter the Upper Limit: ')

a=int(lowerlimit)
b=int(upperlimit)
prime=1
print('prime numbers in the range '+lowerlimit+' to '+upperlimit+' are...')
for p in range(a, b+1):
	for i in range(2, int(p/2)+1):
		if(p%i==0):
			prime=0
			break
	if(prime==1):
		print(p,end=", ")
	prime=1	 