a,b,c,d=map(int, input().split())

if a<c:
    print("Takahashi")
    exit()
if a>c:
    print("Aoki")
    exit()

if a==c:
    if b>d:
        print("Aoki")
        exit()
    else:
        print("Takahashi")
        exit()
