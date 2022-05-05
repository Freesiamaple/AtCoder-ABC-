n,m,k=map(int,input().split())
for a in range(n+1):
    for b in range(m+1):
        if k==a*b+(abs(n-a)*(m-b)):
            print("Yes")
            exit()
print("No")