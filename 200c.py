from operator import mul
from functools import reduce
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under
n=int(input())
A=list(map(int,input().split()))
DP=[0]*200
for i in range(n):
    DP[A[i]%200]+=1

count=0
for j in range(200):
    if DP[j]>=2:
        count+=cmb(DP[j],2)

print(count)