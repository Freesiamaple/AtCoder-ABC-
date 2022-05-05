n=int(input())
A=list(map(int, input().split()))
count=1
A.sort()
if A[0]==0:
    print(0)
    exit()

for i in range(n):
    count*=A[i]
    if count>10**18:
        print(-1)
        exit()
print(count)