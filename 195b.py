a,b,w=map(int,input().split())
u=0
d=99999999
flag=False
for i in range(1000001):
    if a*i<=1000*w and 1000*w<=b*i:
        u=max(i,u)
        d=min(i,d)
        flag=True

if flag==True:
    print(d,u)
else:
    print("UNSATISFIABLE")