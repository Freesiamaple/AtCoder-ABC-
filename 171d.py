n=int(input())
A=list(map(int,input().split()))
Q=int(input())
bc = [map(int, input().split()) for _ in range(Q)]
b,c = [list(i) for i in zip(*bc)]
DP=[0]*10**5
ans=0
for i in range(n):
    DP[A[i]-1]+=1
    ans+=A[i]

for j in range(Q):
    ans+= (DP[b[j]-1])*c[j]
    ans-=(DP[b[j]-1])*b[j]
    DP[c[j]-1]+=DP[b[j]-1]
    DP[b[j]-1]=0

    print(ans)