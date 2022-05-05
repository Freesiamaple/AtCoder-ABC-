n,k=map(int,input().split())
for i in range(k):
    if n%200==0:
        n//=200
    else:
        n=str(n)
        n+="200"
        n=int(n)
print(n)