n,k=map(int,input().split())

X= [list(map(int, input().rstrip('\n').split())) for _ in range(n)]
X.sort()
print(X)
num=k
for i in range(n):
    if num<