n=int(input())
from collections import deque
d = deque()
ans=0
for i in range(n):
    A=list(map(str, input().split()))
    num=A[0]
    if num=="1":
        d.append([int(A[1]),int(A[2])])

    if num=="2":
        l=int(A[1])
        Q=d.popleft()

        ans=0
       

        while l>0:
            if l>=Q[1]:#lが取り出したやつより多い(まだとりだすあとで)
                ans+=Q[0]*Q[1]
                l-=Q[1]
                if d:
                    Q=d.popleft()
            else:#もうとりださない
                ans+=Q[0]*l
                Q[1]-=l
                l=0
                d.appendleft(Q)#dequeにもどす
        print(ans)
        ans=0
 