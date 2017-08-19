n,m = (map(int,input().strip().split(" ")))

lis = [0]*n
maxvalue = 0
for i in range(m):
	a,b,k = (map(int,input().strip().split(" ")))
	for index in range(a-1,b):
		lis[index]+=k
		if  lis[index] > maxvalue:
			maxvalue = lis[index]

print(maxvalue)


