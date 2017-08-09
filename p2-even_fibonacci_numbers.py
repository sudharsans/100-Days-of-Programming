def fibonacci(no):
	fib = []
	fib.insert(0,0)
	fib.insert(1,2)
	for i in range(2,no+3):
			curr = ((4*fib[i-1]) + fib[i-2])
			if curr > no:
				break
			fib.insert(i,curr)
	return (sum(fib))
	
def fib(no):
	pervious,current,total = 0,1,0
	
	while( current < no ):
		if current % 2 == 0:
			#print (current)
			total += current
		pervious,current = current, pervious + current
	return total

print (fibonacci(1000000))
print (fib(1000000))
