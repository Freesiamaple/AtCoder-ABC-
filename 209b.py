n,x=map(int, input().split())
A=list(map(int,input().split()))
count=0
for i in range(n):
    if i%2==1:
        count+=A[i]-1
    else:
        count+=A[i]
if x>=count:
    print("Yes")
else:
    print("No")