#Codewars problem to sort array keeping even number intact.

def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)

  sorted_array = []
  for x in arr:
    if x%2 == 0:
        sorted_array.append(x)
    else:
        sorted_array.append(odds.pop())
  return sorted_array