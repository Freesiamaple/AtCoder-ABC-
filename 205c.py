a,b,c=map(int, input().split())
if c%2==0:
    if abs(a)==abs(b):
        print("=")
    if abs(a)>abs(b):
        print(">")
    if abs(a)<abs(b):
        print("<")
else:
    if abs(a)==abs(b):
        if a>=0:
            if b>=0:
                print("=")
            else:
                print(">")
        else:
            if b>=0:
                print("<")
            else:
                print("<")
    if abs(a)>abs(b):
        print("<")
    if abs(a)<abs(b):
        print(">")