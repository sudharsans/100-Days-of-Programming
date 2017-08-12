#!/bin/python3

import sys

def leftRotation(a, d):
    print (a,d)
    for i in a[:d]:
    	a.remove(i)
    	print(a)
    	a.append(i)
    	print(a)
    return a 

n,d = (map(int,input().strip().split(" ")))
a = list(map(int,input().strip().split(" ")))
result = leftRotation(a, d)
print (" ".join(map(str, result)))

