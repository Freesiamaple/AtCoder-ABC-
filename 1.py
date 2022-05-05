import collections
n=int(input())
A=list(map(int, input().split()))
A=collections.deque(A)
B=collections.deque()
for i in range(n):
    if i%2==0:
        B.append(A.popleft())
    else:
        B.appendleft(A.popleft())
if n%2==1:
    B.reverse()
print(*B)