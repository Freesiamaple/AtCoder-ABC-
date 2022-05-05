n=int(input())
S=[1]
for i in range(n-1):
    S=S+[i+2]+S
print(*S)