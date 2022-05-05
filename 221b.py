r = input()
s = [str(c) for c in r]
S=sorted(s,reverse=True)
if len(S)==1:
    print(S[0])
    exit()


Zero=[]
while '0' in S:
    Zero.append(S.pop(-1))

R=[]
L=[]
ans=0
for bit in range(2**(len(S))):
    R=[]
    L=[]
    for i in range(len(S)):
        if (bit>>i)&1:
            R.append(S[i])
        else:
            L.append(S[i])
    if len(R)>0:
        R_num = int("".join([str(n) for n in R]))
    else:
        R_num=0
    if len(L)>0:
        L_num = int("".join([str(n) for n in L]))
    else:
        L_num=0
    ans=max(ans,R_num*L_num*10**len(Zero))
print(ans)