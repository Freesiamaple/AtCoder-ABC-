X=list(map(int,input().split()))
for i in range(5):
    if i+1!=X[i]:
        print(i+1)
        exit()