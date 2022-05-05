x=[i for i in input()]
y=[i for i in input()]
z=[]
for i in reversed(x):
    z.append(i[::-1])

if y==z:
    print("YES")
else:
    print("NO")