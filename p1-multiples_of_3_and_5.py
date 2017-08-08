# Arithmetic Progression
# x = 1000
# Sum = no_of_terms ( start_term + last_term )/2 = # Sum = common_difference * int(x/common_difference) * int(1+ x/common_difference)/2
# no_of_terms = x/d = 1000/3 = 333
# start_term = common_difference = 3
# last_term = common_difference * int( x / common_difference) = 3 * int(1000/3) = 999
# Sum = int(333 * ( 3 + 999 ) /2)
# Sum = 3 * int(1000/3) * int(1+1000/3) / 2

def multiples_of_3_and_5(no):
	sum = 0
	for number in range(1,no):
		if number % 3 == 0 or number % 5 == 0:
			sum += number
	return sum

def fast_sum(no,diff):
	return int(diff*int(no/diff)*(1+int(no/diff))/2)


div_by_3 = fast_sum(1000,3)
div_by_5 = fast_sum(1000,5)
div_by_15 = fast_sum(1000,15)
print ((div_by_3 + div_by_5) - div_by_15)