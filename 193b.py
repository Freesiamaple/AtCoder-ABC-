n=int(input())
K = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]
ans=10**10
flag=False
for i in range(n):
    if K[i][0]<K[i][2]-0.5:
        ans=min(K[i][1],ans)
        flag=True
if flag==False:
    print(-1)
    exit()
print(ans)