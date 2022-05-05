n=int(input())
A=list(map(int, input().split()))
B=[0]
for i in range(n):
    B=[(n+A[i])%360 for n in B]
    B.append(0)
B.sort()

ans=0
for j in range(n-1):
    ans=max(ans,B[j+1]-B[j])

ans=max(ans,360-B[-1])
print(ans)