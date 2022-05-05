n=int(input())
A=list(map(int, input().split()))
A.sort()
ans=0


from collections import defaultdict
d = defaultdict(int)

for key in A:
    d[key] += 1

for i in d:
    for j in d:
        if i<j:
            ans+=(i-j)**2*d[i]*d[j]
print(ans)