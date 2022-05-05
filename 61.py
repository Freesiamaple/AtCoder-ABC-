n,k=map(int,input().split())
L = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]
L.sort()
count=0
for i in range(len(L)):
    count+=L[i][1]
    if count>=k:
        print(L[i][0])
        exit()
