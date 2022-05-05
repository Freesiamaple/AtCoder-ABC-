n,m,k=map(int, input().split())
dp = [[0] * (k+1) for _ in range(n)]
dp[0][0] = 1#何通りか
mod=998244353
#n=0のとき
for i in range(m):
    dp[0][i]=1


for i in range(1,n):#i番目
    for j in range(1,k+1):#今の値
        for r in range(1,m+1):#1~mの値をためす
            if j+r<=k:
                dp[i][j+r-1]+=dp[i-1][j-1]


            else:
                continue

            
ans=0
for d in dp[-1]:
    ans+=d
    if ans>=mod:
        ans%=mod
print(ans)