n=int(input())
S=[i for i in input()]
Q=int(input())
count=True
for i in range(Q):
    T,a,b=map(int, input().split())
    if T==1:
        if count:
            S[a-1],S[b-1]=S[b-1],S[a-1]
        else:
            S[(n+a-1)%(n*2)],S[(n+b-1)%(n*2)]=S[(n+b-1)%(n*2)],S[(n+a-1)%(n*2)]
            
    else:
        if count:
            count=False
        else:
            count=True
if count==False:
    S=S[n:]+S[:n]
print(*S,sep="")
