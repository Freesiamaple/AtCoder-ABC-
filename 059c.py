n=int(input())
A=list(map(int, input().split()))
L=sum(A)//n
R=L+1
ans_L=0
ans_R=0
for i in range(n):
    ans_L+=(A[i]-L)**2
    ans_R+=(A[i]-R)**2
print(min(ans_L,ans_R))