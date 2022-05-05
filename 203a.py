a,b,c=map(int, input().split())
if a==b:
    print(c)
    exit()
if a==c:
    print(b)
    exit()
if b==c:
    print(a)
    exit()
print(0)
