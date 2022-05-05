h,w=map(int, input().split())
K=[['.']*(w+2)]

for i in range(h):
    K+=[['.']+[a for a in input()]+['.']]

K+=[['.']*(w+2)]


for i in range(1,h+1):
    for j in range(1,w+1):
        if K[i][j]==".":
            continue
        else:
            if K[i+1][j]== "." and K[i-1][j]== "." and K[i][j+1]=="." and K[i][j-1]==".":
                print("No")
                exit()
print("Yes")

