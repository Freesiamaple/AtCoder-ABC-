N=int(input())
A=list(map(int, input().split()))
X=int(input())
A_sum=sum(A)
P=divmod(X,A_sum)
count=0

for i in range(N):
    count+=A[i]
    if P[1]<count:
        num=i
        break
print(P[0]*N+num+1)