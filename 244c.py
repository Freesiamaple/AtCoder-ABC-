n=int(input())


DP=[True for _ in range(2*n+1)]

for i in range(2*n+1):
    for j in range(2*n+1):
        if DP[j]:
            DP[j]=False
            print(j+1)
            s=int(input())
            if s==0:
                exit()
            DP[s-1]=False
            continue
