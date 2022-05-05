s=input()
for i in s:
    if i=="O" or i=="D":
        print(0,end="")
        continue
    if i=="I":
        print(1,end="")
        continue
    if i=="Z":
        print(2,end="")
        continue
    if i=="S":
        print(5,end="")
        continue
    if i=="B":
        print(8,end="")
        continue
    print(i,end="")
print("\n",end='')

