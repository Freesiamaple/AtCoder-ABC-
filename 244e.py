n,m,k,s,t,x=map(int, input().split())
s-=1
t-=1
x-=1

mod=998244353

edge=[]

for i in range(m):
    u,v=map(int,input().split())
    u-=1
    v-=1
    edge.append((u,v))
print(edge)
dp = [[[0] * n for i in range(k + 1)] for X in range(2)]

dp[0][0][s]=1

for i in range(k):
    for u,v in edge:
        for X in range(2):
            dp[X][i + 1][v] += dp[x ^ (v == x)][i][u]
            if dp[X][i + 1][v] >= mod:
                dp[X][i + 1][v] -= mod
            dp[X][i + 1][u] += dp[x ^ (u == x)][i][v]
            if dp[X][i + 1][u] >= mod:
                dp[X][i + 1][u] -= mod
print(dp[0][k][t])