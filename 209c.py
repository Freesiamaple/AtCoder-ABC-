n=int(input())
A=list(map(int, input().split()))
A.sort()
mod=10**9+7

count=1

for i in range(n):
    if A[i]-i==0:
        count*=0
        print(0)
        exit()
    else:
        count*=A[i]-i
        count%=mod
print(count)