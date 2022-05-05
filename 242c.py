n=int(input())
mod=998244353
G=[2,3,3,3,3]
#1 or 9,2 or 8 ,3 or 7 ,4 or 6 ,5



for i in range(n-2):
    flag=False
    
    a=G[0]
    b=G[1]
    if a+b>mod:
        flag=True
    c=G[2]
    d=G[3]
    e=G[4]
    if flag:
        A=[(a+b)%mod,(a+b+c)%mod,(b+c+d)%mod,(c+d+e)%mod,(2*d+e)%mod]

    else:
        A=[a+b,a+b+c,b+c+d,c+d+e,2*d+e]
    G=A
print((sum(G)*2-G[4])%mod)
        

