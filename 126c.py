import math
n,k=map(int, input().split())
ans=0
for i in range(1,n+1):
    if i>=k:
        ans+=1/n
        continue
    x=math.ceil(math.log(k/i,2))
    if x>=0:
        ans+=(1/n)*(1/2)**x
print(ans)
    
