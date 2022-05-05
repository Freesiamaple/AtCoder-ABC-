from re import X


n= int(input())
A = list(map(int, input().split()))
count=0
for i in range(n-1):
    x=A[i]
    x_=A[i+1]
    if i+1==x:
       A[i]=x_
       A[i+1]=x 
       count+=1
       for i in range(n-1):
           x=A[i]
           x_=A[i+1]
           if i+1==x:
               A[i]=x_
               A[i+1]=x 
               count+=1
if A[-1]==n:
    count+=1
print(count)