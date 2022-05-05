s=[i for i in input()]
for i in s:
    if i=="1":
        print("9",end="")
        continue
    if i=="9":
        print("1",end="")
        continue
    print(i,end="")