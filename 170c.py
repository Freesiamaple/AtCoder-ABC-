x,n=map(int, input().split())
P=list(map(int, input().split()))
L=x
R=x
for i in range(100):
    if L not in P and R not in P:
        print(min(L,R))
        exit()
    if L not in P:
        print(L)
        exit()
    if R not in P:
        print(R)
        exit()
    L-=1
    R+=1
