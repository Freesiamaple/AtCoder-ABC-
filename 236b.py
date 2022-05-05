n=int(input())
A=list(map(int, input().split()))
import collections
c = collections.Counter(A)
print(c.most_common()[-1][0])
