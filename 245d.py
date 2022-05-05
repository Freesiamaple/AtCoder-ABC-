import numpy as np
n,m=map(int, input().split())
A=list(map(int, input().split()))
C=list(map(int, input().split()))
A.reverse()
C.reverse()

C= np.array(C)
A = np.array(A)
B=list(np.polydiv(C,A)[0])
B.reverse()
for i in B:
    print(int(i),end=" ")