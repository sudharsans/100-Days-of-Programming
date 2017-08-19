def insertionSort(alist):
    count = 0
    for index in range(1,len(alist)):
        position = index
        currentValue = alist[position]
        while position > 0 and alist[position - 1 ] > currentValue:
            alist[position] = alist[position - 1]
            alist[position - 1] = currentValue
            position -= 1
            count += 1
    return count

n = int(input().strip())
alist = list(map(int,input().strip().split(" ")))
print (insertionSort(alist))
#print (" ".join(map(str,alist)))