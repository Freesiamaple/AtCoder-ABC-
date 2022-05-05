from collections import defaultdict
n,Q=map(int, input().split())
A=list(map(int, input().split()))

R=list(set(A))

D=defaultdict(list)
for i in range(n):
    D[A[i]].append(i)



for h in range(Q):
    a,b=map(int,input().split())
    P=D[a]
    if len(P)<b:
        print(-1)
        continue
    print(P[b-1]+1)