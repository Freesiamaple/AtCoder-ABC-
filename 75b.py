h,w=map(int, input().split())
S=[[0]*w for _ in range(h)]
L=[[0]*(w+2) for _ in range(h+2)]
for i in range(h):
    r = input()
    S[i] = [str(c) for c in r]
    S[i].insert(0,"$")
    S[i].insert(len(S[i]),"$")
S.insert(0,["$"]*(w+2))
S.insert(len(S),["$"]*(w+2))
for i in range(h+2):
    for j in range(w+2):
        if S[i][j]=="#":
            L[i][j]="#"
        if S[i][j]==".":
            if S[i+1][j]=="#":
                L[i][j]+=1
            if S[i-1][j]=="#":
                L[i][j]+=1
            if S[i][j+1]=="#":
                L[i][j]+=1
            if S[i][j-1]=="#":
                L[i][j]+=1

            if S[i+1][j+1]=="#":
                L[i][j]+=1
            if S[i-1][j+1]=="#":
                L[i][j]+=1
            if S[i+1][j-1]=="#":
                L[i][j]+=1
            if S[i-1][j-1]=="#":
                L[i][j]+=1
for i in range(1,len(L)-1):
    for j in range(1,len(L[i])-1):
        print(L[i][j],end="")
    print("\n",end='')