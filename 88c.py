K = [list(map(int, input().rstrip('\n').split())) for _ in range(3)]
flag=False
for a1 in range(101):
    for a2 in range(101):
        for a3 in range(101):
            b1=K[0][0]-a1
            if K[0][1]-b1!=a2:
                continue
            if K[0][2]-b1!=a3:
                continue

            b2=K[1][0]-a1
            if K[1][1]-b2!=a2:
                continue
            if K[1][2]-b2!=a3:
                continue
            
            b3=K[2][0]-a1
            if K[2][1]-b3!=a2:
                continue
            if K[2][2]-b3!=a3:
                continue
            flag=True
if flag==True:
    print("Yes")
else:
    print("No")