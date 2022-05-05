w,h,n=map(int, input().split())
xya = [map(int, input().split()) for _ in range(n)]
x,y,a = [list(i) for i in zip(*xya)]

DP=[[1]*(h) for _ in range(w)]

for x,y,a in zip(x,y,a):

    if a==1:
        for i in range(x):
            for j in range(h):
                DP[i][j]=0
                
    if a==2:
        for i in range(x,w):
            for j in range(h):
                DP[i][j]=0
    if a==3:
        for i in range(w):
            for j in range(y):
                DP[i][j]=0
    if a==4:
        for i in range(w):
            for j in range(y,h):
                DP[i][j]=0

count=0
for i in range(w):
    count+=sum(DP[i])
print(count)