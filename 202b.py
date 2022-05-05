s=input()
z=[]
for i in s:
    if i=="6":
        z.append(9)
        continue
    if i=="9":
        z.append(6)
        continue
    z.append(i)
for j in z[::-1]:
    print(j,end="")