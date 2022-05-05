n,k=map(int,input().split())
count=0
for i in range(n):
    for j in range(k):
        count+=100*(i+1)+j+1
print(count)