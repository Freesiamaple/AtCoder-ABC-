n=int(input())
A=list(map(int, input().split()))

for i in range(n-1):
    now=A[i]
    if now>=A[i+1]:
        print(now)
        exit()
print(A[-1])