n=int(input())
A=list(map(int, input().split()))
num=0
B=[]#Aiの箱
C=[]#Aiに対して何通り?

count=0
for i in range(n-1):
    num=0
    if A[i] in B:
        L=len(A[:i+1])
        M=C[B.index(A[i])]-L+(A[:i+1].count(A[i]))
        count+=M
        print(A[i],M,C[B.index(A[i])])
        continue
    for j in range(i,n):
        if A[i]!=A[j]:
            num+=1
    B.append(A[i])
    C.append(num)
    count+=num
    print(A[i],num,C[B.index(A[i])])
print(count)
print(B)
print(C)