x=[i for i in input()]
L=0
for i in x:
    L+=int(i)
if L%9==0:
    print("Yes")
else:
    print("No")