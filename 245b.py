n=int(input())
A=list(map(int, input().split()))

for i in range(10**6):
    if i not in A:
        print(i)
        exit()