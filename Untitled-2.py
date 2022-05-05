import collections
S=input()
L=len(S)
A=collections.deque(S)
if L%2!=0:
    A.pop()
    L-=1
while True:
    A.pop()
    A.pop()
    L-=2
    l=L/2
    if ([*A][0:int(l)])==([*A][int(l):]):
        break
print(L)