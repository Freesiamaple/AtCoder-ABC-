n=int(input())
T=[i for i in input()]

hougaku="W"
zahyo_x=0
zahyo_y=0

for i in range(n):
    if T[i]=="S":
        if hougaku=="W":
            zahyo_x+=1
        if hougaku=="E":
            zahyo_x-=1
        if hougaku=="S":
            zahyo_y-=1
        if hougaku=="N":
            zahyo_y+=1
    if T[i]=="R":
        if hougaku=="W":
            hougaku="S"
            continue

        if hougaku=="E":
            hougaku="N"
            continue

        if hougaku=="S":
            hougaku="E"
            continue
        if hougaku=="N":
            hougaku="W"
            continue

print(zahyo_x,zahyo_y)


