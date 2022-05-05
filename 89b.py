n=int(input())
A=list(map(str, input().split()))
B=list(set(A))
if len(B)==3:
    print("Three")
else:
    print("Four")