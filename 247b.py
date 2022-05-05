n=int(input())
ab = [map(str, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]
L=[]
c=a+b
for i in range(n):
    if a[i]==b[i]:
        num=2
    else:
        num=1
    if c.count(a[i])==num:
        L.append(i)
        continue
    if c.count(b[i])==num:
        L.append(i)
        continue

if len(L)==n:
    print("Yes")
else:
    print("No")