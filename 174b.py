n,d=map(int,input().split())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]
count=0
for i in range(n):
    if a[i]**2+b[i]**2<=d**2:
        count+=1
print(count)