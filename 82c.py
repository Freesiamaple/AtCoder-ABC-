import collections
n=int(input())
A=list(map(int, input().split()))
c = collections.Counter(A)
count=0
for a in c:
    if a==c[a]:
        continue
    if a>c[a]:
        count+=c[a]
    else:
        count+=c[a]-a
print(count)