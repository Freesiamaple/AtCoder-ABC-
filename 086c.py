import collections
n,k=map(int, input().split())
A=list(map(int, input().split()))
c= collections.Counter(A)
values, counts = zip(*c.most_common())
num=0
for i in range(k,len(counts)):
    num+=counts[i]
print(num)