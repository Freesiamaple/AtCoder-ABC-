import math
n=int(input())
X=math.ceil((-1+(1+8*n)**(1/2))/2)
num=int(X*(X+1)/2)
x=num-n

for i in range(X):
    if i+1!=x:
        print(i+1)