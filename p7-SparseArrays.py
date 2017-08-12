# Hackerrank problem
# https://www.hackerrank.com/challenges/sparse-arrays?h_r=next-challenge&h_v=zen

def sparse(queries,strings):
	count = 0
	counts = []
	for q in queries:
		for s in strings:
			if q == s:
				count += 1
		counts.append(count)
		count = 0
	return counts

n = int(input().strip())
strings = [ str(input().strip()) for i in range(n)]

q = int(input().strip())
queries = [ str(input().strip()) for i in range(q)]
results = sparse(queries,strings)
print ("\n".join(map(str,results)))
