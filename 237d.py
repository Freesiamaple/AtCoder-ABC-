n=int(input())
s=input()
L=[]
R=[]

for i in range(n):
    if s[i]=="R":
        L.append(i)
    else:
        R.append(i)
print(*(L+[n]+R[::-1]))