s=input()
X=[]
for i in s:
    if i=="B":
        if len(X)>0:
            del X[-1]
    if i=="0":
        X.append(i)
    if i =="1":
        X.append(i)
print("".join(X))