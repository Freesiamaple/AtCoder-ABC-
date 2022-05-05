n=[i for i in input()]
s=list(reversed(n))
if s==n:
    print("Yes")
    exit()
for i in range(10):
    n.insert(0,"0")
    s=list(reversed(n))
    if s==n:
        print("Yes")
        exit()
print("No")