n=int(input())
K = [list(map(str, input().rstrip('\n').split())) for _ in range(2*n-1)]
import itertools
N=[]
for i in range(2*n):
    N.append(i+1)
print(N)
