n,m=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=list(map(int, input().split()))
D=list(map(int, input().split()))

zip_AB=zip(A,B)
zip_AB=sorted(zip_AB)
A,B=zip(*zip_AB)
zip_CD=zip(C,D)
zip_CD=sorted(zip_CD)
C,D=zip(*zip_CD)

used = [False] * n
cho=0

for i in range(m):#はこ
    if used[cho]:#すでに大丈夫なちょこ
            continue
    if A[cho]<=C[i] and B[cho]<=D[i]:
        used[cho]=True
        cho+=1
    if cho==n:
        print("Yes")
        exit()


print("No")
