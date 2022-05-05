n,m=map(int,input().split())
def kaijo(x):
    count=1
    for i in range(1,x+1):
        count*=i
        if count>10**5:
            count%=10**9+7
    return count

if n==m+1:
    print(kaijo(n)*kaijo(m)%(10**9+7))
    exit()
if m==n+1:
    print(kaijo(n)*kaijo(m)%(10**9+7))
    exit()
if n==m:
    print((kaijo(n)*kaijo(m)*2)%(10**9+7))
    exit()
print(0)