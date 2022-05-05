n=int(input())
X=list(map(int,input().split()))
L=sorted(X)
R=L[n//2]
L=L[n//2-1]
for i in range(n):
    if X[i]<=L:
        print(R)
        continue
    else:
        print(L)