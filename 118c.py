n=int(input())
A=list(map(int,input().split()))
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


ans=A[0]

for i in range(1,n):
    ans=gcd(A[i],ans)
print(ans)