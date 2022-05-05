n,m=map(int, input().split())
K = [list(map(int, input().rstrip('\n').split())) for _ in range(m)]
D=[[0] for _ in range(m)]

index = [*range(len(K))]
sorted_index = sorted(index, key=lambda i: K[i])
sorted_K = [K[i] for i in sorted_index]

count=1
for j in range(m):
    if j>=1:
        if sorted_K[j][0]!=sorted_K[j-1][0]:
            count=1
        else:
            count+=1
    number_1=str(sorted_K[j][0])
    number_2=str(count)
    D[sorted_index[j]]=number_1.zfill(6)+number_2.zfill(6)
for k in range(m):
    print(D[k])