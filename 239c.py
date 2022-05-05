x1,y1,x2,y2=map(int, input().split())

if abs(x2-x1)>10 or abs(y2-y1)>10:
    print("No")
    exit()

for i in range(-10,10):
    for j in range(-10,10):
        if i**2+j**2==5 and (abs(x2-x1)-i)**2+(abs(y2-y1)-j)**2==5:
            print("Yes")
            exit()
print("No")