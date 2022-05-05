import math
n=int(input())
for i in range(n):
    a,s=map(int, input().split())
    A=bin(a)
    S=bin(s)
    tmp=0
    L=len(A)
    for j in range(2,L):

        if A[j]=="1":
            tmp+=2*(L-2)*2
    print(tmp)