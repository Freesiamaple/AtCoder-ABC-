n,m=map(int,input().split())
X=list(map(int,input().split()))
X.sort()
L=[]
for i in range(m-1):
    L.append(X[i+1]-X[i])
L.sort()
ans=0

for j in range(m-n):
    ans+=L[j]
print(ans)