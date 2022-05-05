n,x=map(int, input().split())
S=[i for i in input()]
s=[i for i in bin(x)][2:]
for i in range(n):
    if S[i]=="U":
        s.pop(-1)
    if S[i]=="R":
        s.append('1')
    if S[i]=="L":
        s.append('0')
X="".join(s)
print(int(X,2))