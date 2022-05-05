import bisect
n,Q=map(int,input().split())
S=input()
ab = [map(int, input().split()) for _ in range(Q)]
a, b = [list(i) for i in zip(*ab)]
L=[0]*n
for i in range(n-1):
    if S[i]=="A" and S[i+1]=="C":
        L[i]+=1

for j in range(Q):
    print(sum(L[a[j]-1:b[j]-1]))