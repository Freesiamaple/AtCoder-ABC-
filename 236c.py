n,m=map(int, input().split())
A=list(map(str, input().split()))
B=list(map(str, input().split()))
C=A+B
import collections

c = collections.Counter(C)

for i in A:
    if c[i]==2:
        print("Yes")
    else:
        print("No")