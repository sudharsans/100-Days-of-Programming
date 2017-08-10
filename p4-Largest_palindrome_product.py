numbers = []
for i in range(100,999):
	for j in range(100,999):
		product = (i * j)
		if str(product) == str(product)[::-1]:
			numbers.append(product)

print (max(numbers))