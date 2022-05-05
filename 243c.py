n=int(input())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]
S=[i for i in input()]

from collections import defaultdict
d = defaultdict(lambda: defaultdict(list))


for i in range(n):
    d[b[i]][S[i]].append(a[i])


for j in d:

    if len(d[j])==2:
        L=max(d[j]['L'])
        R=min(d[j]['R'])

        if L>R:
            print("Yes")
            exit()

print("No")