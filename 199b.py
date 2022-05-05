n=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
L=0
R=9999999999999999999999999999999999
for i in range(n):
    L=max(L,A[i])
    R=min(R,B[i])
print(max(R-L+1,0))