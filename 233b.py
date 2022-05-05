a,b=map(int, input().split())
S=input()

for i in range(a-1):
    print(S[i],end="")
for j in range(b-1,a-2,-1):
    print(S[j],end="")

for k in range(b,len(S)):
    print(S[k],end="")
