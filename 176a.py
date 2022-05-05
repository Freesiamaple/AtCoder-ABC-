n,x,t=map(int, input().split())
count=n//x*t
if n%x!=0:
    count+=t
print(count)