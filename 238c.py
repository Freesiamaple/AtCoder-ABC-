n=int(input())

L=len(str(n))
k=L-1
mod=998244353


ans=0
for i in range(k):#1個下の桁まで
    r=9*10**i
    R=r%mod
    ans+=int(R*(R+1)//2)
    ans%=mod


p=10**k

x=(n-p+1)%mod



ans+=(x%mod)*((x+1)%mod)//2%mod

print(ans%mod)