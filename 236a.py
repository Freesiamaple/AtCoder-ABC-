x=[i for i in input()]
a,b=map(int, input().split())
g=x[a-1]
x[a-1]=x[b-1]
x[b-1]=g
for i in x:
    print(i,end="")