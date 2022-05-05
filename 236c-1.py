n,m=map(int, input().split())
A=list(map(str, input().split()))
B=set(map(str, input().split()))
for a in A:
    if a in B:
        print("Yes")
    else:
        print("No")