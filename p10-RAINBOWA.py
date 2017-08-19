# https://www.codechef.com/problems/RAINBOWA
# Code chef - Chef and Rainbow Array - problem
def rainbow(arr):
	mid = int(len(arr)/2)
	if not arr[mid] == 7:
		return "no"
	for i in range(len(arr[:mid])):
		if not arr[i] in range(1,8) or arr[i] != arr[(len(arr)-1)-i]:
			return "no"
	return "yes"

t = int(input().strip())
for i in range(t):
	e = int(input().strip())
	arr = list(map(int,input().strip().split()))
	print (rainbow(arr))