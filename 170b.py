X,Y=map(int,input().split())
for a in range(101):
    for b in range(101):
        if a+b==X and 2*a+4*b==Y:
            print("Yes")
            exit()
print("No")