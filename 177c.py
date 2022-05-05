n=int(input())
A=list(map(int, input().split()))
Sa=sum(A)
naname=0
for i in range(n):
    naname+=A[i]**2
ans=Sa**2-naname
print(ans//2%(10**9+7))