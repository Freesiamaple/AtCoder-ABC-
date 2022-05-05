n=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=list(map(int, input().split()))
L=[0]*n
ans=0
for i in range(n):
    L[B[C[i]-1]-1]+=1

for i in range(n):
    ans+=L[A[i]-1]
print(ans)