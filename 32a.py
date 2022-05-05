import math
from re import A
 
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
def lcm(x, y):
    return (x * y) // gcd(x, y)

A=int(input())
B=int(input())
n=int(input())


for i in range(n,10**6):
    if i%lcm(A,B)==0:
        print(i)
        exit()