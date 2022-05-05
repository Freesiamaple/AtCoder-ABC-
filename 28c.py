A=list(map(int,input().split()))
L=[]
for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            ans=A[i]+A[j]+A[k]
            L.append(ans)
L.sort(reverse=True)
print(L[2])