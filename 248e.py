n,k=map(int, input().split())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]
from collections import defaultdict

d = defaultdict(int)
if k==1:
    print("Infinity")
    exit()
for i in range(n):
    x1=a[i]
    y1=b[i]

    for j in range(i+1,n):
        x2=a[j]
        y2=b[j]
        #傾き
        l=x2-x1
        if l==0:
            katamuki=10**19
        else:
            katamuki=(y2-y1)/l
            if katamuki==0:
                katamuki=0

        #切片
        if katamuki==0:
            seppen=y2-y1
        else:
            seppen=y2+(katamuki)*x2
        katamuki=str(katamuki)
        seppen=str(seppen)

        d[str(str(katamuki)+","+str(seppen))]+=1


count=0
for c in d:
    if d[c]>=k-1:
        count+=1
print(count)