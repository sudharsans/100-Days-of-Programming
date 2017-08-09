def is_prime(no):
	for i in range(2,no):
		if no % i == 0:
			return False
	return True

def closest_prime(no,lh):
	while not is_prime(no):
		if lh == "high":
			no += 1
		else:
			no -= 1
	return no

number = 270

if is_prime(number):
	print ("{0} is a prime number").format(number)
else:
	print(closest_prime(number,"low"),number,closest_prime(number,"high"))	