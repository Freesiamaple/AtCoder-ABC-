n,k,x=map(int, input().split())
A=list(map(int, input().split()))

L=[]
R=[]
for i in range(n):
    if A[i]>=x:
        L.append(A[i])
    else:
        R.append(A[i])


count=k
for j in range(len(L)):
    if count>=L[j]//x:
        count-=L[j]//x
        L[j]=L[j]%x
    else:#クーポン足りないとき
        L[j]-=count*x
        N=L+R
        print(sum(N))
        exit()


N=L+R

N.sort(reverse=True)


for k in range(min(count,len(N))):
    N[k]=0
print(sum(N))