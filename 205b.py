n=int(input())
A=list(map(int,input().split()))

L=list(set(A))
L.sort()

if len(L)!=n:
    print("No")
    exit()
for i in range(n):
    if i+1!=L[i]:
        print("No")
        exit()
print("Yes")