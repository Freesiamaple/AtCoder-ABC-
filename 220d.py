n=int(input())
A=list(map(int,input().split()))
L_new=[0]*10
L_old=[0]*10
L_old[A[0]]+=1
count=0
for i in range(1,len(A)):
    L_new=[0]*10
    for j in range(10):
        if L_old[j]>0:
            tasizan=(j+A[i])%10
            kakezan=(j*A[i])%10
            L_new[tasizan]+=L_old[j]
            L_new[kakezan]+=L_old[j]
    L_old=L_new
for i in range(10):
    print(L_old[i]%998244353)