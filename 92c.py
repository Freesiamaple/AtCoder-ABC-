n=int(input())
A=list(map(int, input().split()))
count=0

for i in range(n-1):
    count+=abs(A[i+1]-A[i])


for j in range(n):
    if j==0:
        sa=abs(A[j+1]-A[j])
        print(count-sa)
        continue
    if j==n-1:
        sa=abs(A[j]-A[j-1])
        print(count-sa)
    else:
        sa=abs(A[j+1]-A[j-1])-(abs(A[j]-A[j-1])+abs(A[j]-A[j+1]))
        print(count-sa)