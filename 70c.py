n=int(input())

import math
 
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(x, y):
    return (x * y) // gcd(x, y)
ans=1
for i in range(n):
    ans=lcm(ans,int(input()))
print(ans)