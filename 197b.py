a,b=map(int, input().split())
A=list(map(int, input().split()))
count=0
A.sort()
for i in range(b):
    count+=A[i]
print(count)