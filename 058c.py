import collections
from collections import defaultdict
d = defaultdict(int)
n=int(input())
S=input()
c = collections.Counter(S)
values, counts = zip(*c.most_common())
for values,counts in zip(values,counts):
        d[values]=counts
for i in range(n-1):
    S=input()
    c = collections.Counter(S)
    values, counts = zip(*c.most_common())
    for values,counts in zip(values,counts):
        for j in range(97,123):
            d[chr(j)]=min(d[chr(j)],c[chr(j)])
for k in range(97,123):
    if d[chr(k)]!=0:
        for l in range(d[chr(k)]):
            print(chr(k),end="")